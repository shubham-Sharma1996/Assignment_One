from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-submit-button']")
    RESULTS = (By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]")
    RESULTS_ITEMS = (By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    BUY_NOW = (By.XPATH, "//*[@id='buy-now-button']")
    EMAIl = (By.XPATH, "//*[@id='ap_email']")
    CONTINUE = (By.XPATH,"//*[@id='continue']")
    PASS = (By.XPATH,"//*[@id='ap_password']")
    FINAL_SIGN_IN = (By.XPATH,"//*[@id='signInSubmit']")
    ALERT= (By.XPATH,"//div[@class='a-alert-content']")