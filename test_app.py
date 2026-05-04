import unittest
from app import app

class ItemsApiTestCase(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = app.test_client()
        super().__init__(methodName)

    def setUp(self):
        # Runs before each test. Set up a test client for our Flask app.
        app.testing = True  # put Flask in testing mode

    def test_get_items_status_code(self):
        """GET /items should respond with HTTP 200 OK."""
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    # def test_get_items_returns_list(self):
    #     """GET /items should return a JSON list of items."""
    #     response = self.client.get('/items')
    #     data = response.get_json()  # parse JSON response into Python data
    #     # Verify that the response is a list
    #     self.assertIsInstance(data, list)
    #     # There should be at least one item in the list (we added 2 by default)
    #     self.assertGreaterEqual(len(data), 1)

    # def test_items_have_id_and_name(self):
    #     """Each item in the list should have 'id' and 'name' fields."""
    #     response = self.client.get('/items')
    #     data = response.get_json()
    #     if len(data) > 0:
    #         item = data[0]
    #         # Check that item is a dict with the required keys
    #         self.assertIsInstance(item, dict)
    #         self.assertIn('id', item)
    #         self.assertIn('name', item)

    # def test_sample_item_present(self):
    #     """The default 'Sample Item 1' should be part of the response."""
    #     response = self.client.get('/items')
    #     data = response.get_json()
    #     # Collect all item names from the response
    #     names = [item['name'] for item in data]
    #     # Check that "Sample Item 1" is in the list of names
    #     self.assertIn('Sample Item 1', names)

    # def test_fail(self):
    #     """Just a fail test for pipeline github"""
    #     self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
