from selenium.webdriver.common.by import By

#Locator tuples for web elements on the Google Finance Page
class GooglePageLocators(object):
    FINANCE_WATCHLIST_DIV = (By.CLASS_NAME, "H8Ch1")
    WATCHLIST_HEADING = (By.ID, "smart-watchlist-title")
    STOCK_ICONS_CLASS_DIV = (By.CLASS_NAME, "COaKTb")
