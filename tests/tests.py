from src import app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.get('/api/add?num1={}&num2={}'.format(5, 8))
        self.assertEqual(response.text, "13")

    def test_subtract(self):
        response = self.app.get('/api/subtract?num1={}&num2={}'.format(6, 3))
        self.assertEqual(response.text, "3")

    def test_multiply(self):
        response = self.app.get('/api/multiply?num1={}&num2={}'.format(6, 2))
        self.assertEqual(response.text, "12")

    def test_divide(self):
        response = self.app.get('/api/divide?num1={}&num2={}'.format(6, 2))
        self.assertEqual(response.text, "3.0")


if __name__ == '__main__':
    unittest.main()
