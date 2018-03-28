from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# print driver.page_source

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re


driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://xxjs.dtdjzx.gov.cn/")
try:
    startbtn = driver.find_element_by_xpath('//a[@href="monidati.html"]')
except:
    print 'Cannot find element!'
startbtn.click()

# Enter Mock Test Page
for i in range(19):

    question = driver.page_source
    soup = BeautifulSoup(question)
    text = soup.find_all('span',{'class':re.compile('^w_fz18$')})
    q_text = text[0]
driver.find_element_by_name('ra_0').click() # Randomly choose one option
driver.implicitly_wait(10)
try:
    driver.find_element_by_class_name('w_btn_tab_down').click()
except:
    print 'Cannot proceed to the next page'
print driver.page_source
