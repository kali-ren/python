import socket,time


def drot13(s):
	cipher = ''
	for i in s:
		if i.isupper():
			cipher += chr((ord(i)+13-65) % 26+65)
		elif i.islower():
			cipher += chr((ord(i)+13-97) % 26+97)
		else:
			cipher += i
	return 'PRIVMSG Candy :!ep3 -rep '+cipher
				


net = 'irc.root-me.org'
porta = 6667
channel = '#root-me_challenge'
bot = 'candy'
nick = 'admiral_benson'

ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ms.connect((net,porta))
ms.send('NICK '+nick+'\r\n')
ms.send('USER '+nick+' myhost myserver :python chall\r\n')
time.sleep(3)
ms.send('JOIN '+channel+'\r\n')
time.sleep(2)
ms.send('PRIVMSG Candy :!ep3\r\n')

while 1:
	data = ms.recv(1024)
	print data

	if 'PRIVMSG admiral_benson' in data and not 'You dit it!' in data:
		ms.send(drot13(data.split(':')[2])+'\r\n')

	elif 'You dit it!' in data:
		break

ms.close()
