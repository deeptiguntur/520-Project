import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_signup(self):
        # Test signup endpoint
        data = {
            'user_type': 'customer',
            'email': 'test@example.com',
            'username': 'test_user',
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Main St',
            'phone': '123-456-7890',
            'password': 'test_password'
        }

        response = self.app.post('/signup', json=data)
        result = json.loads(response.data.decode('utf-8'))
        print("Response:", result)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['res'], 'True')
        self.assertEqual(result['msg'], 'Signup successfull!')

    def test_login(self):
        # Test login endpoint
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        response = self.app.post('/login', json=data)
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['res'], 'True')
        self.assertEqual(result['user_type'], 'customer')

    def test_add_product(self):
        # Test add-product endpoint for seller
        data = {
            'name': 'Test Product',
            'price': 19.99,
            'quantity': 10
        }

        response = self.app.post('/seller/add-product', json=data)
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['res'], 'True')
        self.assertTrue('msg' in result)

    def test_get_all_products(self):
        # Test get-all-products endpoint
        response = self.app.get('/product/all-products')
        products = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(products, list)

if __name__ == '__main__':
    unittest.main()
