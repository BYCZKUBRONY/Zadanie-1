import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgSearch(unittest.TestCase):

    def tearUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def open_website(self):
        self.browser.get("https://duckduckgo.com")
        field = self.browser.find_element_by_name('q')
        field.clear()
        field.send_keys('the biggest python software house')
        btn = self.browser.find_element_by_id('search_button_homepage')
        btn.click()
        firstscore = self.browser.find_element_by_class_name("result__a")
        firstscore.click()

    def test_test(self):
        self.tearUp()
        self.open_website()
        assert "STX Next" in self.browser.page_source
        self.tearDown()


if __name__ == "__main__": unittest.main()
