from selenium import webdriver

import unittest

from pages.google_finance_page import GoogleFinancePage
from steps.StockSymbolsTestStep import StockSymbolsTestStep
from steps.finance_page_test_steps import FinancePageTestSteps


class TestFinanceSymbols(unittest.TestCase):

    def setUp(self):
        # ChromeDriver will be found in the PATH env variable
        self.driver = webdriver.Chrome()

        # Initialize page object
        self.finance_page = GoogleFinancePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_finance_page(self):
        # Test steps to go to Google Finance page and verify title and url
        FinancePageTestSteps(finance_page=self.finance_page).execute()

    def test_stock_symbols(self):
        # Test data
        test_data = ["NFLX", "MSFT", "TSLA"]

        # Test steps to go to Google Finance page and verify title and url
        FinancePageTestSteps(finance_page=self.finance_page).execute()

        # Retrieve and compare stock symbols to test data and print results
        StockSymbolsTestStep(finance_page=self.finance_page, data=test_data).execute()


if __name__ == "__main__":
    unittest.main()
