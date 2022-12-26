import unittest
import random
import string
from json import JSONDecodeError
from kideapp_helper import Functionality

test_object = Functionality("random_url")


random_id = ''.join(random.choice(string.ascii_lowercase) for i in range(50))
random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
random_price = random.randint(100, 250000)
random_availability = random.randint(0, 500)
test_dict = [{"inventoryId": random_id, "pricePerItem": random_price, "availability": random_availability, "name": random_name}]

correct_output = {random_id: [random_name, random_price, random_availability]}

class TestHelperMethods(unittest.TestCase):


    def test_return_url(self):
        self.assertEqual("random_url", test_object.return_url(), "The url isn't correct!")

    # def test_with_invalid_url(self):
    #     self.assertRaises(JSONDecodeError, test_object.get_request())

    def test_inventoryIds(self):
        test_object.variants = test_dict
        test_object.loop_through_variants()
        self.assertEqual(correct_output, test_object.return_inventoryIds(), "The values are not equal!")

    def test_variants(self):
        test_object.variants = test_dict
        self.assertEqual(test_dict, test_object.return_variants(), "The values are not equal!")

    def test_faulty_post_request(self):
        self.assertEqual(False, test_object.post_request(5, "test_bearer"), "The boolean should be false!")

if __name__ == '__main__':
    unittest.main()