import socket,time,math

def conta(s):
	s = s.strip('\n')
	eq = s.rsplit(':',1)[1]
	a = eq.split('/')[0].replace(' ','')
	b = eq.split('/')[1].replace(' ','')
	
	raiz = math.sqrt(int(a))
	resposta = format(float(raiz)*int(b),'.2f')
	return 'PRIVMSG Candy :!ep1 -rep '+resposta+'\r\n'
#use round 
#"""
net = 'irc.root-me.org'
porta = 6667
channel = '#root-me_challenge'
bot = 'candy'
nick = 'admiral_benson'
#http://www.devshed.com/c/a/Python/Python-and-IRC/

ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ms.connect((net,porta))
ms.send('NICK %s\r\n' %(nick) )
ms.send('USER %s balestra oursaulo :benson\r\n' %(nick))
time.sleep(3)
ms.send('JOIN #root-me_challenge\n')
time.sleep(2)
ms.send('PRIVMSG Candy :!ep1\r\n')
while 1:
	data = ms.recv(1024)
	print data

        if 'PRIVMSG admiral_benson' in data and not 'You dit it!' in data:
	    ms.send(conta(data)) 
        elif 'PRIVMSG admiral_benson' in data and 'You dit it!' in data:
	    break
ms.close()
