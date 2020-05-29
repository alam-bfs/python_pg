import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FbAddRemoveItemMp(unittest.TestCase):

    USERNAME = "Unknown"
    PASSWORD = "Unknown"

    def setUp(self):
        options = Options()
        options.headless = False
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
        self.driver.find_element_by_id("u_0_b").click()

        # Go to Market Place
        market_place_elm = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Marketplace')))
        market_place_elm.click()

        # Logout
        login_anchor_elm = self.wait.until(EC.element_to_be_clickable((By.ID, 'pageLoginAnchor')))
        login_anchor_elm.click()
        elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span._54nh')))
        for elm in elements:
            if elm.text == "Log Out":
                elm.click()
        assert "Facebook - Log In or Sign Up" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        FbAddRemoveItemMp.PASSWORD = sys.argv.pop()
        FbAddRemoveItemMp.USERNAME = sys.argv.pop()
    unittest.main()
