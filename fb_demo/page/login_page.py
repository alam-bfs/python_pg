from fb_demo.page.base_page import BasePage


class LoginPage(BasePage):

    def is_title_matches(self):
        return "Facebook - Log In or Sign Up" in self.driver.title

    def login(self, username, password):
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_id("u_0_b").click()

