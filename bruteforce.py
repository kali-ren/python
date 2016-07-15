#!/usr/bin/python

import crypt,os,sys
#a simple dictionary atttack for unix pass
def dec(enc):
	salt = enc[0:2]
	path = '/usr/share/dirb/wordlists/common.txt' #path for chosen wordlist 
	arquivo = open(path,'r')

	if not os.path.isfile(path):
		print '[-]'+ arquivo + 'does not exist'
		exit(0)
	if not os.access(path,os.R_OK):
		print '[-]' + arquivo + 'access denied'
		exit(0)

	for line in arquivo.readlines():
		line = line.strip('\n')
		eline = crypt.crypt(line,salt)
		if (eline == enc):
			print '[+] found password: '+line+'\n'
			return
	print '[-] password not found\n'
	return

def main():
	encoded = 'loMYfQLo.I1lY' #
	dec(encoded)	

if __name__ == '__main__':
	main()
