from threading import Thread
import sys
import socket
import requests

rock  = open('wordlist','r')
ip    = ''
check = True

class Rock(Thread):
	def __init__(self, name, begin, end, thread_list):
		Thread.__init__(self)
		self.name 		 = name
		self.begin 		 = begin
		self.end 		 = end
		self.thread_list = thread_list
		
	def gen_list(self):
		print '[+] generating list for %s...' %(self.name) 
		
		rock.seek(0)
		for i in rock.readlines()[self.begin:self.end]:
			self.thread_list.append(i.strip())
			
		print '[+] done!'
		
	def run(self):
		global check
		
		for i in self.thread_list:
			if check == False: break
			
			payload = {}
			cookies = {}
			r = requests.post(ip,data=payload,cookies=cookies).text
			
			if not 'some string' in r:
				print '%s :)'%(self.name)
				print '[+] found it '+i.strip()
				print r			
				check = False
				break
			
		print '[*] %s exiting...'%(self.name)

def main():		
	a_list = []
	b_list = []
	c_list = []
	d_list = []
	
	a = Rock('Thread_a', start, end, a_list)
	b = Rock('Thread_b', start, end, b_list)
	c = Rock('Thread_c', start, end, c_list)
	d = Rock('Thread_d', start, end,d_list)
	
	a.gen_list()
	b.gen_list()
	c.gen_list()
	d.gen_list()

	l= [a,b,c,d]
	
	print '[+] cracking...'
	for t in l:
		thread = t
		thread.start()
		
main()
