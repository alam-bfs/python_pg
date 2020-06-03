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

    # elements locators
    sell_something_btn = "i._3-8_.img.sp_IlF0F1XJPC__2x.sx_7e9c9f"
    selling_edit_box = "._2t_f ._58al"
    save_draft_btn = "._1mf7._4jy0._4jy3._517h._51sy._42ft"
    delete_btn = ".__fn>button._4jy0._4jy3._517h._51sy._42ft"

    def setUp(self):
        options = Options()
        options.headless = False
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=options)
        # self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://www.facebook.com/")
        # Login
        self.driver.find_element_by_id("email").send_keys(self.USERNAME)
        self.driver.find_element_by_id("pass").send_keys(self.PASSWORD)
        self.driver.find_element_by_id("u_0_b").click()

        # Login with existing session
        executor_url = self.driver.command_executor._url
        session_id = self.driver.session_id

        self.remote_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        self.remote_driver.session_id = session_id
        self.wait = WebDriverWait(self.remote_driver, 20)

    def test_add_remove_item(self):

        # Go to Market Place
        market_place_elm = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Marketplace')))
        market_place_elm.click()

        # add items and delete items
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sell_something_btn))).click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Item for Sale'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selling_edit_box))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selling_edit_box))).send_keys("lamp for sale")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.save_draft_btn))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delete_btn))).click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'OK'))).click()

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
