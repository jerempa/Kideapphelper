from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import ElementNotInteractableException
import chromedriver_binary
import time
import datetime

def main():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.get("https://kide.app/events/367c5cdc-62e2-44fb-88ef-7501a026ba9e") #open the right web page
    try:
        #deny_location(wd)
        #sign_in = sign_in_element(wd)
        #log_in = log_in_element(wd)
        #write_credentials_and_sign_in(wd)
        #refresh_tickets(wd)
        time.sleep(10)
        #tickets_expire_from_others_carts(wd)
    except NoSuchElementException:
        time.sleep(1) #wait for a moment if the page hasn't been loaded
    while(True):
        pass

def sign_in_element(wd):
    element = wd.find_element("xpath", "/html/body/header/o-toolbar/o-toolbar__controls/o-menu[2]/o-menu-button/o-action-chip")
    element.click()
    #find the element for signing in and click it

def log_in_element(wd):
    time.sleep(0.25)
    element = wd.find_element("xpath", "/html/body/o-menu-container/o-menu-content/o-menu-item[6]")
    element.click()
    #find the element for opening log in screen and click it


def write_credentials_and_sign_in(wd):
    username = wd.find_element(By.ID, 'username')
    username.send_keys("email")
    time.sleep(0.05)
    password = wd.find_element(By.ID, 'password')
    password.send_keys("password")
    #click_remember_me = wd.find_element("xpath", "/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/o-input-checkbox/label/o-accent").click()
    sign_in = wd.find_element("xpath", "/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/button/span").click()
    #write credentials and sign in to the website

def deny_location(wd):
    time.sleep(8)
    element = wd.find_element("xpath", "/html/body/header/o-consent/o-content/o-material/o-material__footer/button[2]")
    element.click()
    #find the element for location and deny it

def refresh_tickets(wd):
    time.sleep(2)
    try:
        element = wd.find_element(By.CSS_SELECTOR, 'span[ng-bind="::origin.localization.productDetailsReload.format(product.productType.variant.name.casual.plural)"]')
        wd.execute_script("arguments[0].scrollIntoView();", element) #find refresh tickets -element and scroll to it
    except NoSuchElementException:
        pass
    while True:
        try:
            ticket = wd.find_element(By.CLASS_NAME, 'o-align-items--flex-start')  #if ticket element is found then break the loop and call another function to click it
            break
        except NoSuchElementException:
            try:
                time.sleep(0.25)
                element.click() #if the add to cart -element isn't on the page then keep refreshing it
            except StaleElementReferenceException:
                break
    find_and_click_product(wd)
    #selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document


def find_and_click_product(wd):
    element = wd.find_element(By.CLASS_NAME, 'o-align-items--flex-start')
    #r = requests.post('https://kide.app/events/32f06dd5-47db-4018-8cb5-63141e2f82c4', data={'key': 'value'})
        #element = wd.find_elements("xpath", '//*[text() = "60,00 €"]') #exact match, insert string into quotes
        #element = wd.find_element("xpath", '//*[text()[contains(., "T 17.40")]]') #text contains certain string
        # for i in element:
        #     if i.get_attribute('class') == '': #this needed if using € and there is the price element on the left that isn't clickable -> differentiates between it and the ticket
        #         pass
        #     element = i
            #element = i.find_element("xpath", '//*[text()[contains(., "klo 15:45")]]')  # if there is many elements with same price you can specify e.g. which time you want
    try:
        element.click()
    except ElementNotInteractableException:
        wd.find_element(By.CLASS_NAME, 'o-align-items--flex-start').click()
    # except ElementClickInterceptedException:
    #     # try:
    #     #     wd.find_element("xpath", '//*[text() = "EI-JÄSEN LIPPU klo 16:00"]').click()
    #     #except NoSuchElementException:
    #     wd.find_element(By.CLASS_NAME, 'o-align-items--flex-start').click() #try-except for if the program clicks the wrong element e.g. item is sold out
    quantity_of_items(wd)

def quantity_of_items(wd):
    num_of_tickets = int(1)
    try:
        element = wd.find_element(By.CSS_SELECTOR, 'select[ng-model="variantForm.quantity"]')
        id_num = element.get_attribute("id")
        element.click() #try to find element for selecting quantity
        try:
            quantity = wd.find_element("xpath", f'//*[@id="{id_num}"]/option[{num_of_tickets}]')
            quantity.click()  # click the quantity element and select as many tickets as mentioned in the num_of_tickets integer
            element.click()
        except NoSuchElementException:
            quantity = wd.find_element("xpath", f'//*[@id="{id_num}"]/option[1]')  # try-except for if there is a quantity drop down list, but the only option is 1
    except NoSuchElementException:
        pass #if there isn't a possiblity to change quantity then pass
    time.sleep(0.1)
    #checkout = wd.find_element(By.CLASS_NAME, "o-button o-button--accent" )
    continue_shopping = wd.find_element("xpath","/html/body/o-dialog__container/o-dialog/form/o-dialog__footer/o-dialog__footer__content/button[2]") #(adds them to cart, otherwise it doesn't)
    #checkout = wd.find_element("xpath", "/html/body/o-dialog__container/o-dialog/form/o-dialog__footer/o-dialog__footer__content/button[1]")
    continue_shopping.click() #continue to checkout

def tickets_expire_from_others_carts(wd):
    #element = wd.find_element("xpath", '//*[text()[contains(., "€")]]')
    #element = wd.find_element(By.CLASS_NAME, '"o-align-items--flex-start')
    element = wd.find_element("xpath", '//*[text()[contains(., "Fully booked")]]')
    cart = wd.find_element("xpath", '//*[text()[contains(., "€")]]')
    value = True
    while value:
        time.sleep(0.5)
        wd.refresh()
        try:
            cart = wd.find_element("xpath", '//*[text()[contains(., "Polin appro 10.11.")]]').click()
            value = False
        except ElementClickInterceptedException:
            print("testi")
            wd.refresh()
        # if wd.find_element("xpath", '//*[text()[contains(., "Sold out")]]'):
        #     break
        # if cart:
        #     cart.click()
        #     break -> menee aina näiden iffien sisään
        # try:
        #     wd.find_element(By.CLASS_NAME, '"o-align-items--flex-start').click()
        #     break
        # except InvalidSelectorException:
        #     pass
        # try:
        #     element.click()
        #     break
        # except (ElementClickInterceptedException, StaleElementReferenceException):
        #     pass
    # try:
    #     wd.find_element(By.CLASS_NAME, '"o-align-items--flex-start').click()
    # except (InvalidSelectorException):
    #     pass
    quantity_of_items(wd)


main()

