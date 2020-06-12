import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
