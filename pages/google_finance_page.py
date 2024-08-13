from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from util.locators import GooglePageLocators


class GoogleFinancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = GooglePageLocators
        self.wait = WebDriverWait(driver, 30)

    def open_finance_page(self) -> None:
        url = self.base_url + "/finance"
        self.driver.get(url)

    def get_stock_symbols(self) -> list[str]:
        # Wait for 'You may be interested in' section to load
        self.wait_element(*self.locators.WATCHLIST_HEADING)

        # Get the Watchlist div that contains the stock symbols
        watchlist_div: WebElement = self.find_element(*self.locators.FINANCE_WATCHLIST_DIV)

        # Retrieve the stock symbol web elements within the watchlist div
        stock_elements: list[WebElement] = watchlist_div.find_elements(*self.locators.STOCK_ICONS_CLASS_DIV)

        # Return the list stock symbol's text
        return [element.text.strip() for element in stock_elements if element.text.strip()]