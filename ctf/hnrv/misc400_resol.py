#!/usr/bin/python

from PIL import Image

def flag(bina):
	flag = ''
	for i in range(0,len(bina),8):
		flag += chr(int(bina[i:i+8],2))
	print flag

a=Image.open('48d663725fa68ef6fce4d37ec5158921.png','r')
l=[]
bina = ''

for i in range(0,a.size[1]):
	#print list(a.getpixel((0,i)))#opcional debug
	if list(a.getpixel((0,i)))[1] == 1:
		bina += '1'
	else:
		bina += '0'
flag(bina)
	
	
