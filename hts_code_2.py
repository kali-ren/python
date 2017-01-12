#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from PIL import Image
#hack this site programming 2
def decode_morse(code):
	code = code.split(' ')
	ans = ''
	morse = {'a':'.-',	'b':'-...',	'c':'-.-.',	'd':'-..',	'e':'.', 
		 'f':'..-.',	'g':'--.',	'h':'....',	'i':'..',	'j':'.---',
		 'k':'-.-',	'l':'.-..',	'm':'--',	'n':'-.',	'o':'---',
		 'p':'.--.',	'q':'--.-',	'r':'.-.',	's':'...',	't':'-',
		 'u':'..-',	'v':'...-',	'w':'.--',	'x':'-..-',	'y':'-.--',
		 'z':'--..',	'0':'-----',	'1':'.----',	'2':'..---',	'3':'...--',
		 '4':'....-',	'5':'.....',	'6':'-....',	'7':'--...',	'8':'---..',
		 '9':'----.'}
	for c in code:
		for k,v in morse.items():
			if c == v:
				ans += k
	return ans

ip = 'https://www.hackthissite.org/user/login'
ip2 = 'https://www.hackthissite.org/missions/prog/2/'
ip3 = 'https://www.hackthissite.org/missions/prog/2/index.php'
payload = {'username':'','password':''}
referer = {'referer':'https://www.hackthissite.org/missions/prog/1/'}


with requests.Session() as r:
	login = r.post(ip,data=payload,headers=referer)
	html = r.get(ip2).content 
	sopa = BeautifulSoup(html,'lxml')
	tag = sopa.find_all('img')
	img = r.get('https://www.hackthissite.org'+tag[11]['src'],headers=referer).content
	my_img = open('my_image.png','w')
	my_img.write(img)
	my_img.close() 
	f = Image.open('my_image.png','r')
	pixels = f.load()
	off_new = 0#attention offset started 0
	off_old = 0
	code = ''
	for i in range(f.size[1]):
		for j in range(f.size[0]):
			if f.getpixel((j,i)) == 1:
				code += chr(off_new-off_old)
				off_old = off_new
				off_new += 1 
			else:
				off_new += 1
	f.close()
	subbmit = r.post(ip3,data={'solution':decode_morse(code),'submitbutton':'submit'},headers=referer)
	print subbmit.text#save and open in browser
