from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
driver.get('http://martafrak.pl')

title = driver.title
print(title)