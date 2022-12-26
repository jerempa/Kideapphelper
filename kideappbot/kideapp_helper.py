import time
import requests
import datetime

class Functionality:
    def __init__(self, url):
        self.url = str(url)
        self.variants = list()
        self.inventoryIds = dict()
        self.items = list()
        self.name = None
        self.itemId = str()
        self.get_request()
        self.loop_through_variants()

    def return_url(self):
        return self.url

    def return_variants(self):
        return self.variants

    def return_inventoryIds(self):
        return self.inventoryIds

    def return_itemId(self):
        return self.itemId

    def return_chosen_item(self):
        return self.name

    def return_list_of_items(self):
        for key, value in self.inventoryIds.items():
            self.items.append(value)
        return self.items

    def get_request(self):
        url = f"https://api.kide.app/api/products/{self.url}"
        #target_time = datetime.time(hour=12, minute=00, second=1)
        # while True:
        #     now = datetime.datetime.now()
        #     time = now.time()
        #     time_without_microseconds = time.replace(microsecond=0)
        #     if time_without_microseconds == target_time:
        #         break #loop until the tickets go on sale and we have information about the item ids
        try:
            response = requests.get(url)
            data = response.json()
            key = data['model']
            self.variants = key['variants']
        except requests.exceptions.JSONDecodeError:
            pass
        # while len(self.variants) == 0:
        #     response = requests.get(url)
        #     data = response.json()
        #     key = data['model']
        #     self.variants = key['variants'] #probably not needed anymore as there is timer for making the request

    def loop_through_variants(self):
        if len(self.variants) > 0:
            for i in self.variants:
                info_list = []
                inventoryId = i['inventoryId']
                name = i['name']
                info_list.append(name)
                price = i['pricePerItem']
                info_list.append(price)
                availability = i['availability']
                info_list.append(availability)
                self.inventoryIds[inventoryId] = info_list #add values to the dictionary that contain id, price, name and availability

    def choose_correct_item(self, name):
        for key, value in self.inventoryIds.items():
            if str(value[0]) == name:
                self.itemId = key #change variable based on what ticket user chose

    def get_name_of_chosen_item(self, sender, dict):
        for key, value in dict.items():
            if sender == value:
                self.name = key #get the name of the ticket user chose

    def post_request(self, itemId, bearer_token):
        headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json; charset=UTF-8'}
        data = {"toCreate":[{"inventoryId":self.itemId,"quantity":1,"productVariantUserForm":None}], "toCancel": []}
        url = "https://api.kide.app/api/reservations"
        response = requests.post(url, headers=headers, json=data) #make a post request with correct data and headers

        if response.status_code == 200:
            return True #if the response status code is 200, this means the request was successful
        else:
            return False



