import unittest
import requests

class RoleBookTest (unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.new_book_dict = {'title': 'TNT', 'author': 'ddddo', 'id': 2}
        self.new_book = requests.post((self.base_url + 'books/'), data=self.new_book_dict)
        self.book_id = self.new_book.json()['id']

    def test_new_book (self):
        self.assertEqual(self.new_book.status_code,201)
        self.assertNotEqual(self.new_book.json()['author'],None)

    def test_refresh (self):
        self.new_book_dict ['title'] = 'Napalm'
        new_book_refresh = requests.put((self.base_url + 'books/'+ str(self.book_id) + '/'), data = self.new_book_dict)
        self.assertEqual(new_book_refresh.status_code,200)
        self.assertEqual(self.new_book_dict['title'],'Napalm')

    def test_kill (self) :
        kill_new_book = requests.delete(self.base_url + 'books/'+ str(self.book_id) + '/')
        self.assertEqual(kill_new_book.status_code,204)
        self.assertEqual(requests.get(self.base_url + 'books/'+ str(self.book_id) + '/').status_code,404)
        self.assertNotEqual(requests.get(self.base_url + 'books/' + str(self.book_id) + '/').status_code, 200)

    def test_wrong (self):
        wrong_dict = {'title': 'TNT', 'author': 'ddddo', 'id': '00iou090hj'}
        new_book = requests.post((self.base_url + 'books/'), data=wrong_dict)
        self.assertEqual(new_book.status_code,404)

    def tearDown(self):
        requests.delete(self.base_url)


if __name__ == '__main__':
    unittest.main(verbosity=2)