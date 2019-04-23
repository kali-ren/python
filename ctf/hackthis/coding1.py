#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
#hackthis coding1
def ordem(s):#redo in one line
	s = s.replace(' ','')
	l = s.split(',')
	l.sort()
	s2 = ', '.join(l)
	return s2

def ret(ip,ip2):
	payload = { 'username': '', 'password': '' }
	with requests.Session() as s:
		p = s.post(ip,data=payload) 	
		html = s.get(ip2).content
		sopa = BeautifulSoup(html,'lxml')
		tag = sopa.findAll('textarea')	
		ans = ordem(str(tag[0].string))	
		p2 = s.post(ip2,data={'answer': ans})
		print p2.text

ip = 'https://www.hackthis.co.uk/?login'
ip2 = 'https://www.hackthis.co.uk/levels/coding/1'


ret(ip,ip2)
