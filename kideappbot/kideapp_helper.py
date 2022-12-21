#from selenium import webdriver
#import chromedriver_binary
import time
import requests
import datetime

def main():
    #wd = webdriver.Chrome()
    #wd.maximize_window()
    #wd.get("https://kide.app/events/a696a71b-b6ec-4852-bafa-6678aa03b3b4") #open the right web page
    #synchronize_time()
    inventoryIds = get_request()
    itemId = choose_correct_item(inventoryIds)
    adding_to_cart = post_request(itemId)
    if adding_to_cart == True:
        print("Ticket succesfully added to your cart!")
    else:
        print(f"Adding ticket to cart failed. Error code: {adding_to_cart}")

def synchronize_time():
    pass #thought about making a function for syncing computer time but haven't implemented it yet



def get_request():
    event_url = str(input("Insert event url, the address after 'events/': "))
    url = f"https://api.kide.app/api/products/{event_url}"
    target_time = datetime.time(hour=19, minute=53, second=10)
    # while True:
    #     now = datetime.datetime.now()
    #     time = now.time()
    #     time_without_microseconds = time.replace(microsecond=0)
    #     if time_without_microseconds == target_time:
    #         break #loop until the tickets go on sale and we have information about the item ids
    response = requests.get(url)
    data = response.json()
    key = data['model']
    variants = key['variants']
    while len(variants) == 0:
        time.sleep(0.25)
        response = requests.get(url)
        data = response.json()
        key = data['model']
        variants = key['variants']
    inventoryIds = loop_through_variants(variants)
    print(inventoryIds) #print the dict so user knows what to choose
    return inventoryIds #return the ids, their name, price and availability

def loop_through_variants(variants):
    inventoryIds = dict() #process the request and get value that we want
    for i in variants:
        info_list = []
        inventoryId = i['inventoryId']
        name = i['name']
        info_list.append(name)
        price = i['pricePerItem']
        info_list.append(price)
        availability = i['availability']
        info_list.append(availability)
        inventoryIds[inventoryId] = info_list #add values to the dictionary that contain id, price, name and availability
    return inventoryIds

def choose_correct_item(inventoryIds):
    itemId = str()
    for key, value in inventoryIds.items():
        right_item = str(input("Identify the right item, e.g name, price etc.: "))
        if right_item.isnumeric():
            right_item = int(right_item)
        while right_item not in value:
            right_item = str(input("The input was incorrect: "))
            if right_item.isnumeric():
                right_item = int(right_item) #loop until the user gives a item that is available
        itemId = key
        if right_item in value and value[2] != 0:
            break #break the loop if the item is correct and available, availability != 0
    return itemId #return the itemId to the main function

def post_request(itemId):
    headers = {'Authorization': 'Bearer xyz', 'Content-Type': 'application/json; charset=UTF-8'}
    data = {"toCreate":[{"inventoryId":itemId,"quantity":1,"productVariantUserForm":None}], "toCancel": []}
    url = "https://api.kide.app/api/reservations"
    response = requests.post(url, headers=headers, json=data) #make a post request with correct data and headers
    if response.status_code == 200:
        return True #if the response status code is 200, this means the request was successful
    else:
        return response.status_code #else return the error code

main()

