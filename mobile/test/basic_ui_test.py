import unittest
from appium import webdriver
from time import sleep


class HomePageTest(unittest.TestCase):
    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '13.5'
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['app'] = '/Users/kaiseralam/python_pg/mobile/app/TableSearch.app'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):
        print('----------->' + self.driver.find_element_by_name('Birthdays').text)
        sleep(5)


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
