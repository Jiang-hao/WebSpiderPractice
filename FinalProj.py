
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def JoeyFunc(html):
    print 'Joey is not ready'

# f = open('result.txt', 'w')
# d = dict()

#driver = webdriver.Chrome('C:\Users\Hao\Desktop\chromedriver.exe')
driver = webdriver.PhantomJS()
driver.get("https://alcoholpolicy.niaaa.nih.gov/")
question = driver.page_source
soup = BeautifulSoup(question)
res = soup.find_all('a',{'class':re.compile('^policyListing$')})
titles=[]
for title in res:
    titles.append(title.text)

driver.find_element_by_link_text('Beer Taxes').click()
driver.find_element_by_id('ctl00_ctl05_ctl00_ASPxPageControl1_T2T').click()
select = Select(driver.find_element_by_id('ctl00_ctl05_ctl00_selectPolicyTopic'))
select.select_by_index(0)
select = Select(driver.find_element_by_id('ctl00_ctl05_ctl00_selectPolicyTopic'))
print
for i in range(0,len(select.options)):
    select.select_by_index(i)
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "ctl00_ctl05_ctl00_ASPxPageControl1_policyData_range1_specificPolicy_ASPxGridView1_tccell38_17"))
    )
    select = Select(driver.find_element_by_id('ctl00_ctl05_ctl00_selectPolicyTopic'))
    if((len( select.first_selected_option.get_attribute('value')) == 0)):
        # Ignore
        pass
    else:
        # Parse
        JoeyFunc(driver.page_source)



# for r in res:
#     driver.implicitly_wait(100)
#     if r.text == 'Beer Taxes':
#         pass
#     else:
#         title = r.text
#         select = Select(driver.find_element_by_id('ctl00_ctl05_ctl00_selectPolicyTopic'))
#         select.select_by_visible_text(title)
#         driver.implicitly_wait(100)
#         JoeyFunc(driver.page_source)

# for i in range(1,4):
#     select.select_by_index(i)
#     driver.implicitly_wait(100)
#     JoeyFunc(driver.page_source)
    # if select.first_selected_option.get_attribute("value") is not "":
    #     JoeyFunc(driver.page_source)
# driver.find_element_by_xpath('//select[@id="ctl00_ctl05_ctl00_selectPolicyTopic"]/option[text()='+res[1].text+']').click()
# for r in res:
#     if r.text == 'Beer Taxes':
#         pass
#     else:
#         title = r.text
#         select.select_by_visible_text('Wine Taxes')
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ctl05_ctl00_ASPxPageControl1_policyData_range1_specificPolicy_ASPxGridView1_tccell38_17"))
#         )
#
#         JoeyFunc(driver.page_source)
driver.close()























    # try:
    #     startbtn = driver.find_element_by_xpath('//a[@href="monidati.html"]')
    # except:
    #     print 'Cannot find element!'
    # startbtn.click()
    # driver.implicitly_wait(10)
    # # Enter Mock Test Page
    # for i in range(19):
    #     question = driver.page_source
    #     soup = BeautifulSoup(question)
    #     res = soup.find_all('span',{'class':re.compile('^w_fz18$')})
    #     q_text = res[2*i+1].text.encode('utf-8')
    #     print q_text
    #     res = soup.findAll('div', {'class' : 'W_ml45'})
    #     q_answer = res[5*i]['answer']
    #     print q_answer
    #     if q_text in d:
    #         print 'exist'
    #     else:
    #         d[q_text] = q_answer
    #         f.write(q_text+'\n')
    #         f.write(q_answer+'\n')
    #
    #     driver.find_element_by_name('ra_'+str(i)).click() # Randomly choose one option
    #     driver.implicitly_wait(10)
    #     try:
    #         driver.find_element_by_class_name('w_btn_tab_down').click()
    #     except:
    #         print 'Cannot proceed to the next page'

# f.close()