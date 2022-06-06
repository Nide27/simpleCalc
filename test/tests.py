import requests
import unittest


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        response = requests.get('http://127.0.0.1:5000/api/add?num1={}&num2={}'.format(5, 8))
        self.assertEqual(response.text, "13")

    def test_subtract(self):
        response = requests.get('http://127.0.0.1:5000/api/subtract?num1={}&num2={}'.format(6, 3))
        self.assertEqual(response.text, "3")

    def test_multiply(self):
        response = requests.get('http://127.0.0.1:5000/api/multiply?num1={}&num2={}'.format(6, 2))
        self.assertEqual(response.text, "12")

    def test_divide(self):
        response = requests.get('http://127.0.0.1:5000/api/divide?num1={}&num2={}'.format(6, 2))
        self.assertEqual(response.text, "3.0")


if __name__ == '__main__':
    unittest.main()


