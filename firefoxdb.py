#!/usr/bin/python

#sniff firefox db 

import sqlite3,os,re,optparse

def rtdw(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('select moz_places.id, moz_places.url, moz_places.title from moz_places, moz_annos where moz_places.id = moz_annos.place_id group by moz_places.url')
	print '[*] --- Downloads found ---'
	for row in c:
		print '[+] id: '+str(row[0]) + ' url: '+str(row[1].encode('utf-8'))+' title: '+str(row[2].encode('utf-8'))

def printcookies(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('select host, name, value from moz_cookies;')
	print '[*] --- cookies found ---'
	for row in c:
		host = str(row[0])
		name = str(row[1])
		value = str(row[2])
		print '[+] host: '+host+' name: '+name+' value: '+value

def printhistory(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('select url, datetime(visit_date/1000000,\'unixepoch\') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id = moz_historyvisits.place_id;')
	print '[*] -- history found --'
	for row in c:
		url = str(row[0])
		date = str(row[1])
		print '[+] url: '+url+' date: '+date

def printgoogle(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('select url, datetime(visit_date/1000000,\'unixepoch\') from moz_places,moz_historyvisits where visit_count > 0 and moz_places.id = moz_historyvisits.place_id order by visit_date;')
	print '[*] -- google search found --'
	for row in c:
		url = str(row[0])
		date = str(row[1])
		if 'https://www.google' in url:
			r = re.findall(r'q=.*',url)
			if r:
				ret = r[0].split('&')
				ret = ret[0].replace('q=','').replace('+',' ')
				print '[+] date: '+date+' search: '+ret				
def main():
	p = ''#file path
	rtdw(p)
#	printcookies(p2)
	printhistory(p)
	printgoogle(p)
if __name__ == '__main__':
	main()
