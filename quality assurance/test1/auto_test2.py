import unittest
from selenium import webdriver

class FirstTest(unittest.TestCase): #class inherited from TestCase
    def test_main_page(self):
        driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
        driver.get('http://martafrak.pl')
        title = driver.title
        print(title)
        assert 'My first website' == title
        driver.quit()
