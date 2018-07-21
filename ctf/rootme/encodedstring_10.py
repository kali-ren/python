import base64,socket,time

data = 'Um9vdE1l'
print base64.b64decode(data)

def decoded(encoded):
    return 'PRIVMSG Candy :!ep2 -rep '+base64.b64decode(encoded)


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
ms.send('PRIVMSG Candy :!ep2\r\n')

while 1:
    data = ms.recv(1024)
    print data

    if 'PRIVMSG admiral_benson' in data and not 'You dit it!' in data:
        encoded = data.split(':')[2]
        ms.send(decoded(encoded)+'\r\n')

    elif 'PRIVMSG admiral_benson' in data and 'You dit it!' in data:
        break

ms.close()
