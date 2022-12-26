from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from kideapp_helper import Functionality

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kide.app helper")
        self.setGeometry(100, 100, 700, 700)
        self.functionality = None
        self.bearer_token = str()
        self.dict_of_tickets = dict()
        self.create_widgets()

    def create_widgets(self):

        self.bearer = QLineEdit(self, placeholderText="Enter your bearer token")
        self.bearer.setFont(QFont('Arial', 11))

        self.bearer.setGeometry(0, 20, 500, 30)

        self.input_box = QLineEdit(self, placeholderText="Enter the url after '/events' and click ok")
        self.input_box.setFont(QFont('Arial', 11))

        self.input_box.setGeometry(0, 50, 500, 30)

        self.button = QPushButton("Ok", clicked=lambda: self.button_press_event())
        self.button.setGeometry(500, 50, 30, 30)
        self.layout().addWidget(self.button)

        self.time = QLabel(self)
        self.time.setFont(QFont("Arial", 15))
        self.time.setGeometry(550, 30, 150, 50)
        self.layout().addWidget(self.time)

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(100) #creating widgets and connecting them to another function if necessary

    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")

        self.time.setText(label_time) #show current time

    def button_press_event(self):
        self.bearer_token = self.bearer.text()
        user_input = self.input_box.text()
        self.functionality = Functionality(user_input)

        self.show_items() #get the values from the user input

    def show_items(self):
        items = self.functionality.return_list_of_items()
        if len(items) == 0:
            self.message_boxes(1, True)
        k = int(50)
        for i in range(len(items)):
            if items[i][2] > 0:
                name = items[i][0]
                price = items[i][1]
                name_and_price = f"{name}, {price / 100} €"
                self.item = QLabel(name_and_price)
                self.choose = QPushButton("Choose ticket", clicked=lambda: self.ticket_chosen())

                self.item.setFont(QFont("Arial", 10))
                self.item.setGeometry(0, 75 + k, 525, 40)

                self.layout().addWidget(self.item)
                self.dict_of_tickets[name] = self.choose

                self.choose.setFont(QFont("Arial", 12))
                self.choose.setGeometry(525, 75 + k, 175, 40)

                self.layout().addWidget(self.choose) #add the ticket types to the GUI
                k += 50

    def ticket_chosen(self):
        self.functionality.get_name_of_chosen_item(self.sender(), self.dict_of_tickets)
        self.functionality.choose_correct_item(self.functionality.return_chosen_item())

        boolean = self.functionality.post_request(self.functionality.return_itemId(), self.bearer_token)

        self.message_boxes(0, boolean) #call functions that update the values

    def message_boxes(self, integer, boolean):
        self.msgbox = QMessageBox()
        self.msgbox.setIcon(QMessageBox.Information)
        self.msgbox.setFont(QFont("Arial", 12))
        self.msgbox.setGeometry(50, 135, 250, 70)
        self.msgbox.setStyleSheet("color: black; background: white")

        self.layout().addWidget(self.msgbox)

        if integer != 0:
            self.msgbox.setText("Items aren't on sale yet!")
        elif boolean:
            self.msgbox.setText(f"Added ticket to your cart!")
        if not boolean:
            self.msgbox.setText("Adding ticket to your cart failed") #notify the user about the success of adding the ticket to cart




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
