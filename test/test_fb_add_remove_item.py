import sys
import unittest
from fb_demo.page.login_page import LoginPage


class FbAddRemoveItem(unittest.TestCase):
    USERNAME = "Unknown"
    PASSWORD = "Unknown"

    def setUp(self):
        self.loginPage = LoginPage

    def test_facebook_page_title(self):
        self.loginPage.is_title_matches()

    def tearDown(self):
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        FbAddRemoveItem.PASSWORD = sys.argv.pop()
        FbAddRemoveItem.USERNAME = sys.argv.pop()
    unittest.main()
