
from steps.base_test_step import BaseTestStep


class FinancePageTestSteps(BaseTestStep):
    def __init__(self, finance_page):
        super().__init__(finance_page)

    def execute(self):
        is_finance_page_open: bool = self.open_finance_page()
        self.assertTrue(is_finance_page_open, f"Not on Google Finance webpage."
                                              f"Title: {self.finance_page.get_title()}")

    def open_finance_page(self) -> bool:
        # Open the webpage www.google.com/finance
        self.finance_page.open_finance_page()

        # Verify the page title
        expected_title: str = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        return expected_title == self.finance_page.get_title()