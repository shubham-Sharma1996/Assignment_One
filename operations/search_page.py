import logging
from selenium.webdriver.support import expected_conditions as EC
from data.locators import SearchPageLocators


class SearchPage():

    def make_a_search(self,driver,wait):
        self.driver = driver
        self.wait =wait
        self.locator = SearchPageLocators
        self.driver.get('https://www.amazon.in/')
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys('iphone 13')
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS_ITEMS))
        result_items = driver.find_elements(*self.locator.RESULTS_ITEMS)
        for x in result_items:
            print(x.text)
        if len(result_items) >= 4:
            fourth_item = result_items[3]
            fourth_item.click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        self.wait.until(EC.presence_of_element_located(self.locator.BUY_NOW)).click()
        self.wait.until(EC.presence_of_element_located(self.locator.EMAIl)).send_keys('shubhamshrm1996@gmail.com')
        self.driver.find_element(*self.locator.CONTINUE).click()
        self.wait.until(EC.presence_of_element_located(self.locator.PASS)).send_keys('pass')
        self.driver.find_element(*self.locator.FINAL_SIGN_IN).click()
        error_message = self.wait.until(
            EC.presence_of_element_located(self.locator.ALERT))
        logging.info(f"The value is: {error_message.text}")
        return error_message.text








