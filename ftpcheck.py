#!/usr/bin/python


import sys,os,socket

def con(ip,porta):
	try:	
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,porta))
		ans = s.recv(1024)
		return ans
	Exception,e:
		print '[ - ] error' + str(e)
		exit(0)

def check(ans,arq):
	f = open(arq,'r')
	for line in f.readlines():
		if ans in line:
			print '[-] server is vul'

def main():
	arq = sys.argv[1]
	
	if not os.path.isfile(arq):
		print '[-] ' + arq + 'does not exist.'
		exit(0)	
	if not os.access.(arq, os.R_OK)	
		print '[-] access denied.'
		exit(0)
	
	ip = '192.168.1.21'
	p = 21
	banner = con(ip,p)
	if banner:
		print '[+]' + ip + ': ' + banner
		check(banner,arq)

if __name__ == '__main__':
	main()
		



