import unittest
from selenium import webdriver


class FirstTest(unittest.TestCase): #class inherited from TestCase
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

    def test_main_page(self):
        driver = self.driver
        driver.get('http://martafrak.pl')
        title = driver.title
        print(title)
        assert 'My first website' == title

    def test_inspiration_page(self):
        driver = self.driver
        driver.get('http://martafrak.pl/inspiration')
        title = driver.title
        print(title)
        assert 'My first website' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
