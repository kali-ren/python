#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def nova():
	n = []
	for i in range(32,127):
		n.append(chr(i))
	return n

def decry(n,s):
	s = s.split(',')
	answer = ''
	for i in s:
		if i == ' ':
			answer += ' '
		else:
			charoriginal = chr(int(i))
			newindex = n.index(charoriginal)
			posi_charnovo = 94 - newindex
			answer += n[posi_charnovo]
	return answer
				
def crypto(n,s):
	c = []
	for i in s:
		if i == ' ':
			c.append(i)
		else:
			print 'new ascii: '+str(n.index(i))
			v = 94 - n.index(i)
			print 'v: %d' %v                   #debug
			cara = n[v]
			print 'char nessa position: '+cara #debug
			org = ord(cara)
			c.append(str(org))
	print ','.join(c)

def connect(n):#what matters
	payload = { 'username':'','password':'' }
	url = 'https://www.hackthis.co.uk/?login'
	url2 = 'https://www.hackthis.co.uk/levels/coding/2'	
	with requests.Session() as r:
		r.post(url,data=payload)
		html = r.get(url2).content
		sopa = BeautifulSoup(html,'lxml')
		tag = sopa.findAll('textarea')
		print type(tag[0].string)
		ans = decry(n,str(tag[0].string)) 
		p = r.post(url2,data={ 'answer':ans })
		print p.content

connect(nova())
