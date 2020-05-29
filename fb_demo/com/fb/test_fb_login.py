import sys
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class FbAddRemoveItemMp(unittest.TestCase):

    USERNAME = "Unknown"
    PASSWORD = "Unknown"

    def setUp(self):
        options = Options()
        options.headless = True
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.facebook.com/")

    def test_add_remove_item(self):
        # Login
        self.driver.find_element_by_id("email").send_keys(self.USERNAME)
        self.driver.find_element_by_id("pass").send_keys(self.PASSWORD)

        assert "Facebook - Log In or Sign Up" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        FbAddRemoveItemMp.PASSWORD = sys.argv.pop()
        FbAddRemoveItemMp.USERNAME = sys.argv.pop()
    unittest.main()
