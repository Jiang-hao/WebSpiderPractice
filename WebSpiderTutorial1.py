#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import random
from urllib import urlopen
from bs4 import BeautifulSoup
import sched, time
import smtplib
#
#
# def sendemail(from_addr, to_addr_list, cc_addr_list,
#               subject, message,
#               login, password,
#               smtpserver='smtp.gmail.com:587'):
#     header = 'From: %s\n' % from_addr
#     header += 'To: %s\n' % ','.join(to_addr_list)
#     header += 'Cc: %s\n' % ','.join(cc_addr_list)
#     header += 'Subject: %s\n\n' % subject
#     message = header + message.encode('utf-8')
#
#     server = smtplib.SMTP(smtpserver)
#     server.starttls()
#     server.login(login, password)
#     problems = server.sendmail(from_addr, to_addr_list, message)
#     server.quit()
#     return problems
#
#
#
# #
# s = sched.scheduler(time.time, time.sleep)
# # while True:
# #     print 'Repeat!'
#
#
#
#
# ep_num = 42
#
# while True:
#
#     url = "http://cn.lovetvshow.info/2017/12/cn171218-list.html"
#
#     html = urlopen(url).read().decode('utf-8')
#     soup = BeautifulSoup(html,'lxml')
#     ep_list = soup.find_all('a',{
#         "href":re.compile("^.*cn171218-e.*$")
#     })
#     if len(ep_list) > ep_num:
#         ep_num = len(ep_list)
#         sendemail(from_addr='jiangh0313@gmail.com',
#                   to_addr_list=['jiangh0313@gmail.com'],
#                   cc_addr_list=[''],
#                   subject='琅琊榜2更新啦',
#                   message= u'来自管理员' + '\n' + u'琅琊榜2最新一集: '+ep_list[0].string+'\n'+u'传送门: '+ep_list[0]['href'],
#                   login='jiangh0313@gmail.com',
#                   password='hao920313')
#         sendemail(from_addr='jiangh0313@gmail.com',
#                   to_addr_list=['jsjjcyj@gmail.com'],
#                   cc_addr_list=[''],
#                   subject='琅琊榜2更新啦',
#                   message= u'来自管理员' + '\n' + u'琅琊榜2最新一集: '+ep_list[0].string+'\n'+u'传送门: '+ep_list[0]['href'],
#                   login='jiangh0313@gmail.com',
#                   password='hao920313')
#         print 'email sent'
#
#     else:
#         print 'No update'
#
#     str = '================================\n'+ u'来自管理员' + '\n' + u'琅琊榜2最新一集: '+ep_list[0].string
#     print str
#     time.sleep(60*20)

# -*- coding: utf-8 -*-
'''
网络爬虫之用户名密码及验证码登陆：爬取知乎网站
'''
import json

import requests
import ConfigParser

# def create_session():
#     cf = ConfigParser.ConfigParser()
#     cf.read('config.ini')
#     cookies = cf.items('cookies')
#     cookies = dict(cookies)
#     from pprint import pprint
#     pprint(cookies)
#     email = cf.get('info', 'email')
#     password = cf.get('info', 'password')
#
#     session = requests.session()
#     login_data = {'email': email, 'password': password}
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#         'Host': 'www.lovetvshow.com'
#     }
#     # r = session.post('http://www.renren.com/', data=login_data, headers=header)
#     r = session.get('http://www.lovetvshow.com/',headers=header)
#     print r
#     print json.loads(r.content.encode(('utf-8-sig')))
#     if r.json()['r'] == 1:
#         print 'Login Failed, reason is:',
#         for m in r.json()['data']:
#             print r.json()['data'][m]
#         print 'So we use cookies to login in...'
#         has_cookies = False
#         for key in cookies:
#             if key != '__name__' and cookies[key] != '':
#                 has_cookies = True
#                 break
#         if has_cookies is False:
#             raise ValueError('请填写config.ini文件中的cookies项.')
#         else:
#             # r = requests.get('http://www.zhihu.com/login/email', cookies=cookies) # 实现验证码登陆
#             r = session.get('http://www.zhihu.com/login/email', cookies=cookies) # 实现验证码登陆
#
#     with open('login.html', 'w') as fp:
#         fp.write(r.content)
#
#     return session, cookies
#
#
# if __name__ == '__main__':
#     requests_session, requests_cookies = create_session()
#
#     # url = 'http://www.zhihu.com/login/email'
#     url = 'http://www.zhihu.com/topic/19552832'
#     # content = requests_session.get(url).content # 未登陆
#     # content = requests.get(url, cookies=requests_cookies).content # 已登陆
#     content = requests_session.get(url, cookies=requests_cookies).content # 已登陆
#     with open('url.html', 'w') as fp:
#         fp.write(content)

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'refer':'https://visaonline.thaiembassy.sg/index.php',
    'host':'visaonline.thaiembassy.sg'
}
payload = {'users': 'jianghaohao','password':'hao920313','action':'user1_menu2'}
cookie = {
    '__cfduid':'d1c8e11b1fcca7dabae6a095e9e1064a81517558292',
    'SESS5041847d1f16d349f9a2f9db79240a31':'e795a19e7fdbc0c20f189bba77f30040',
    '__utma' :'85345244.546690475.1517558294.1517558294.1517558294.1',
    '__utmc':'85345244',
    '__utmz':'85345244.1517558294.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmb':'85345244.2.10.1517558294',
    'PHPSESSID':'5cb434ba4fdbc309778e233d7cc98cd4'
}
url = 'https://visaonline.thaiembassy.sg/index.php/'
r = requests.post(url,data=payload,cookies = cookie)
# html = r.text
# soup = BeautifulSoup(html)
print r.text