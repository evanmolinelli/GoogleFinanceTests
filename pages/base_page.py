# this Base class is serving basic attributes for every single page inherited from Page class
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver, base_url='https://www.google.com'):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, *locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_element(self, *locator) -> None:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()