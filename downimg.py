#!/usr/bin/python
import requests,sys,os
from bs4 import BeautifulSoup

#******************************
# Download images from website  
#******************************

def retrieve(ip):
	r = requests.get(ip).content
	sopa = BeautifulSoup(r,'lxml')
	img = sopa.findAll('img')
	return img

def download(ip,imgt):
	try:
		print '[+] Downloading images...'
		src = imgt['src']
		new = requests.get(src).content
		filename = os.path.basename(src)
		newimage = open(filename,'wb')
		newimage.write(new)
		newimage.close()
		print 'file '+ filename +' downloaded'
	except:
		pass

def main():
	if len(sys.argv) != 2:
		print 'modo de uso: %s site' % sys.argv[0]
		exit(0)

	ip = sys.argv[1]
	imgs = retrieve(ip)
	dir_name = ip.split('.')[1] 
	os.makedirs(dir_name)
	os.chdir(dir_name)

	for i in range(0,len(imgs)):
		download(ip,imgs[i])

if __name__ == '__main__':
	main()
