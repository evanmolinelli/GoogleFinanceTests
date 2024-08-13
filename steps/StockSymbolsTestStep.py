from steps.base_test_step import BaseTestStep


class StockSymbolsTestStep(BaseTestStep):
    def __init__(self, finance_page, data):
        super().__init__(finance_page)
        self.data = data

    def execute(self):
        # Retrieve stock symbols
        stock_symbols: list[str] = self.finance_page.get_stock_symbols()

        # Compare with test data
        # Find symbols from section but not in test data
        symbols_not_in_test: list[str] = self.compare_symbols_not_in_test_date(stock_symbols=stock_symbols, data=self.data)
        print(f"Stock symbols in section but not in test data: {symbols_not_in_test}")

        # Find symbols in test data
        symbols_not_in_page: list[str] = self.symbols_in_test_data(stock_symbols=stock_symbols, data=self.data)
        print(f"Stock symbols in test data: {symbols_not_in_page}")

    def compare_symbols_not_in_test_date(self, stock_symbols: list[str], data: list[str]) -> list[str]:
        # Compare with test data
        # Find symbols from section but not in test data
        return [symbol for symbol in stock_symbols if symbol not in data]

    def symbols_in_test_data(self, stock_symbols: list[str], data: list[str]) -> list[str]:
        # Find symbols in test data
        return [symbol for symbol in stock_symbols if symbol in data]