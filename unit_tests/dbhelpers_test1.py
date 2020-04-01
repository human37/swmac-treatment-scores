import unittest
import sys
sys.path.append('./') # adds dbhelpers.py to namespace
from dbhelpers import new_user, get_user, get_user_by_name
from tinydb import TinyDB

# tests the functions new_user, get_user, and get_user_by_name from dbhelpers.py 

db = TinyDB('./db.json')

class Test1(unittest.TestCase):

    def test1_new_user(self):
        """
        Test that it can add a new user
        """
        username = 'user123'
        password = 'pass123'
        new_user(db, username, password)
        user = get_user(db, username, password)
        self.assertEqual(username, user['username'])

    def test2_get_user(self):
        """
        Test that it can get an existing user
        """
        username = 'user123'
        password = 'pass123'
        user = get_user(db, username, password)
        self.assertEqual(username, user['username'])
    
    def test3_get_user_by_name(self):
        """
        Test that it can get an existing user only by username
        """
        username = 'user123'
        user = get_user_by_name(db, username)
        self.assertEqual(username, user['username'])
    
    
if __name__ == '__main__':
    unittest.main()