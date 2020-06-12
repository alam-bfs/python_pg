from selenium import webdriver

driver = webdriver.Chrome()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://www.facebook.com")

driver.find_element_by_id("email").send_keys("avalanche1492@gmail.com")
driver.find_element_by_id("pass").send_keys("sep022014")
driver.find_element_by_id("u_0_b").click()

print(session_id)
print(executor_url)

driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver2.session_id = session_id
driver2.get("https://www.google.com")
print(driver2.session_id)
driver2.get("https://www.facebook.com")
print(driver2.current_url)
