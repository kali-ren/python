import socket, zlib, base64,time

def decompress_me(msg):
    return 'PRIVMSG Candy :!ep4 -rep ' + zlib.decompress(base64.b64decode(msg))
    
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
ms.send('PRIVMSG Candy :!ep4\r\n')

while 1:
    data = ms.recv(1024)
    print data

    if 'PRIVMSG admiral_benson' in data and not 'You dit it!' in data:
        ms.send(decompress_me(data.split(':')[2])+'\r\n')

    elif 'You dit it!' in data:
	break

ms.close()    
