#!/usr/bin/python

import crypt,os
#a simple dictionary atttack for unix pass
def dec(enc):
	salt = enc[0:2]
	arquivo = open('/usr/share/dirb/wordlists/common.txt','r')


	for line in arquivo.readlines():
		line = line.strip('\n')
		eline = crypt.crypt(line,salt)
		if (eline == enc):
			print '[+] found password: '+line+'\n'
			return
	print '[-] password not found\n'
	return

def main():
	encoded = 'loMYfQLo.I1lY'
	dec(encoded)	

if __name__ == '__main__':
	main()
