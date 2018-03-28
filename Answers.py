from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

f = open('result.txt', 'w')
d = dict()

for i in range(30):
    driver = webdriver.Chrome('C:\Users\Hao\Desktop\chromedriver.exe')
    driver.get("http://xxjs.dtdjzx.gov.cn/")
    try:
        startbtn = driver.find_element_by_xpath('//a[@href="monidati.html"]')
    except:
        print 'Cannot find element!'
    startbtn.click()
    driver.implicitly_wait(10)
    # Enter Mock Test Page
    for i in range(19):
        question = driver.page_source
        soup = BeautifulSoup(question)
        res = soup.find_all('span',{'class':re.compile('^w_fz18$')})
        q_text = res[2*i+1].text.encode('utf-8')
        print q_text
        res = soup.findAll('div', {'class' : 'W_ml45'})
        q_answer = res[5*i]['answer']
        print q_answer
        if q_text in d:
            print 'exist'
        else:
            d[q_text] = q_answer
            f.write(q_text+'\n')
            f.write(q_answer+'\n')

        driver.find_element_by_name('ra_'+str(i)).click() # Randomly choose one option
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_class_name('w_btn_tab_down').click()
        except:
            print 'Cannot proceed to the next page'
    driver.close()
f.close()