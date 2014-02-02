from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.duckduckgo.com')

# search for bacon
search_box = driver.find_element_by_id('search_form_input_homepage')
search_box.send_keys('bacon')
driver.find_element_by_id('search_button_homepage').click()