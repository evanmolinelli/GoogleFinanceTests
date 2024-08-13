import unittest
from abc import ABC, abstractmethod


class BaseTestStep(ABC, unittest.TestCase):
    def __init__(self, finance_page):
        super().__init__()
        self.finance_page = finance_page

    @abstractmethod
    def execute(self):
        pass
