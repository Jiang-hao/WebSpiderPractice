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
import requests

word = raw_input('请输入你要翻译的汉语(Type \'exit\' to exit)：  ')
# print person


while(word != 'exit'):
    url = 'http://www.youdao.com/w/' + word
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    res = soup.find_all('a',{
        'href':re.compile('^.*#keyfrom=E2Ctranslation$')
    })

    trans=[]
    for k in res:
        trans.append(k.string.encode('utf-8'))

    print trans
    word = raw_input('请输入你要翻译的汉语：  ')