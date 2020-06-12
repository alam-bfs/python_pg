import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class PageNavigation(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.google.com/")

    def test_search_cheese(self):
        element = self.driver.find_element_by_css_selector("input.gLFyf.gsfi")
        element.send_keys("Cheese")
        element.send_keys(Keys.RETURN)

        print(len(self.driver.find_elements_by_xpath(".//a")))
        print(len(self.driver.find_elements_by_tag_name("a")))

        print(len(self.driver.find_elements_by_tag_name("h2")))
        print(len(self.driver.find_elements_by_tag_name("p")))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()