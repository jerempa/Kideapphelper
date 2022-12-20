import unittest
import random
import string
import kideapp_helper as helper


class TestHelperMethods(unittest.TestCase):

    def test_variants(self):
        random_id = ''.join(random.choice(string.ascii_lowercase) for i in range(50))
        random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        random_price = random.randint(100, 250000)
        random_availability = random.randint(0, 500)
        test_dict = [{"inventoryId": random_id, "pricePerItem": random_price, "availability": random_availability, "name": random_name}]

        correct_output = {random_id: [random_name, random_price, random_availability]}
        program_output = helper.loop_through_variants(test_dict)
        self.assertEqual(correct_output, program_output, "The values are not equal!")



if __name__ == '__main__':
    unittest.main()