#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
#hack this site programming 1
def answer(tag):
	f = open('wordlist.txt','r')#wordlist is given
	ans = ''
	for i in range(47,57):
		a = ''.join(sorted(str(tag[i]).replace('<li>','').replace('</li>','')))#parameter in alpha order.
		for word in f.readlines():
			word2 = word.strip()
			if ''.join(sorted(word2)) == a:
				ans += ','+word2 
				f.seek(0)

	return ans.lstrip(',')
		

ip = 'https://www.hackthissite.org/user/login'
ip2 = 'https://www.hackthissite.org/missions/prog/1/'
ip3 = 'https://www.hackthissite.org/missions/prog/1/index.php'
ipp = 'http://localhost/mopa.html'
payload = {'username':'butt-head','password':'554f436a98f6'}
print '[+] running...'
with requests.Session() as r:
	login = r.post(ip,data=payload,headers={'referer':'https://www.hackthissite.org/missions/prog/1/'})
	html = r.get(ip2).content
	sopa = BeautifulSoup(html,'lxml')
	tag = sopa.find_all('li')
	print len(tag)
	ans = r.post(ip3,data={'solution':answer(tag),'submitbutton':'submit'},headers={'referer':'https://www.hackthissite.org/missions/prog/1/'})
	if 'Congrats' in ans.text: print 'Gotcha :)'
