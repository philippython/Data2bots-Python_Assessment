import json
import unittest
from main import value__mapper

class TestValueMapper(unittest.TestCase):

    """recieves key and data type to be chekced as parameters"""
    def checker(self, key, type):
        value__mapper('test_data/string_test.json', 'test_data/string_output.json')
        with open('test_data/string_output.json') as file:
            result = json.load(file)[key]
            self.assertEqual(result["type"], type)        

    """test to check string type """
    def test_string(self):
        self.checker(key="key_one", type="string")

    """test to check integer type """
    def test_integer(self):
        self.checker(key="key_two", type="integer")

    """test to check invalid enum type"""
    def test_invalid_enum(self):
        self.checker(key="key_three", type=None)


    """test to check valid enum type"""
    def test_valid_enum(self):
        self.checker(key="key_four", type="enum")


    """test to check array type"""
    def test_valid_array(self):
        self.checker(key="key_five", type="array")

    
    """test to check boolean type"""
    def test_boolean(self):
        self.checker(key="key_six", type=None)
    


if __name__ == "__main__":
    unittest.main()