#!/usr/bin/python

import sys,urllib2,os
from bs4 import BeautifulSoup
def ordem(s):
	l = []
	s2 = s.replace(' ','')
	l = s2.split(',')
	l.sort()
	print l
	s3 = ','.join(l)
	return s3
def ret(ip):
	try:
		urlconteudo = urllib2.urlopen(ip).read()
		sopa = BeautifulSoup(urlconteudo,'lxml')
		imgtags = sopa.findAll('textarea')
		tag = imgtags[0].string
#		print tag.string		
		ordem(str(tag))
	except Exception, e:
		print e

ip = sys.argv[1]
ret(ip)
