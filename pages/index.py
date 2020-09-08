from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from files import ref

class Shopper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    # Fetch the e-commerce page
    def set_up(self):
        self.driver.get(ref.url)
        self.driver.maximize_window()

    # Insert the search item in the search bar
    def search_item(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ref.search_box)))
        self.driver.find_element_by_css_selector(ref.search_box).send_keys(ref.search_item)

    # Click the search button
    def click_search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ref.search_box)))
        self.driver.find_element_by_css_selector(ref.search_button).click()

    # Select an item from the result
    def pick_an_item(self):
        self.driver.find_element_by_css_selector(ref.search_result).click()
