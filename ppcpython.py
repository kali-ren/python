#!/usr/bin/python
import random, threading, Queue

deck=[]

mutex = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)

full = threading.Semaphore(2)
full2 = threading.Semaphore(2)

empty = threading.Semaphore(0)
empty2 = threading.Semaphore(0)

mb1=threading.Semaphore(2)
mb2=threading.Semaphore(2)

buff1=Queue.Queue(2)
buff2=Queue.Queue(2)

lmb=[mb1,mb2]
listabuffer=[buff1,buff2]

winner = True
class Card():
	def __init__(self,num,naipe):
		self.num = num
		self.naipe = naipe
	
	def __str__(self):
		return "%d%s" % (self.num,self.naipe)

class Deck():
	global deck
	numeros = [1,2,3,4,5,6]
	naipe = ['A','E','C','P']

	for i in range(6):
		for j in range(4):
			card=Card(numeros[i],naipe[j])
			deck.append(card)

	def shuffle(self,deck):
		random.shuffle(deck)

	def gerarmao(self,mao):
		for i in range(4):
			mao.append(deck[i])

		for i in range(4):
			del deck[0]
	
	def gerarbuffer(self,buff):
		for i in range(2):
			buff.put(deck[i])

		for i in range(2):
			del deck[0] 
 
class Jogador(threading.Thread):
	def __init__(self,nome,mao,idd):
		threading.Thread.__init__(self)#importante !!
		self.nome=nome
		self.mao=mao
		self.idd=idd

	def bufferget(self):
		return self.idd

	def buffdrop(self):
		if self.idd == 0:
			return 1
		else:
			return 0

	def freq(self):
		aux = [0] * 7
		for i in self.mao:
			if i.num == 1:
				aux[1] += 1	
			elif i.num == 2:
				aux[2] += 1
			elif i.num == 3:
				aux[3] += 1
			elif i.num == 4:
				aux[4] += 1
			elif i.num == 5: 
				aux[5] += 1
			elif i.num == 6:
				aux[6] += 1
		high = max(aux)
		low = min(aux)
                if high == 3:
 			for i in self.mao:
				if i.num != high and i.num != low:
					return i
		else:
			a = random.randint(0,4)
			o = self.mao[a]
			return o

	def getcard(self):
		
		mutex.acquire()
		if listabuffer[self.bufferget()].qsize() == 0:
			print "%s dormiu buffer vazio!" %(self.nome)		
		mutex.release()
		
		full.acquire()
		mutex.acquire()
		if listabuffer[self.bufferget()].qsize() == 0:
			print "%s acordou !" % (self.nome)
		listabuffer[self.bufferget()]
		a = listabuffer[self.bufferget()].get()
		self.mao.append(a)
		print "i, %s, get" % (self.nome)
		print a
		print "%s mao: " %(self.nome)
		for i in range(len(self.mao)):
			print self.mao[i]
		listabuffer[self.bufferget()].get()
		mutex.release()
		empty.release()
	
	def drop(self):
			a = self.buffdrop()
			mutex.acquire()
			if listabuffer[a].qsize() == 2:
				print "%s dormiu buffer cheio !" % (self.nome)
			mutex.release()
			
			empty.acquire()
			mutex.acquire()

			if listabuffer[a].qsize() == 2:
				print "%s acordou !" % (self.nome)
			
			b = self.freq()
			try:
				self.mao.remove(b)
			except:
				pass
			print "%s dropped " % (self.nome)
			print b
			listabuffer[a].put(b)
			mutex.release()
			full.release()		
	
	def run(self):
		a=0
		while a < 2:
			self.getcard()	
			a += 1
			self.drop()
Deck().shuffle(deck)
print "////////////////////////antes\n"
for i in deck:
	print i

maoana=[]
maobeto=[]
maocarla=[]
maodani=[]

Deck().gerarmao(maoana)
Deck().gerarmao(maobeto)

Deck().gerarbuffer(buff1)
Deck().gerarbuffer(buff2)
print "////////////////////////depois\n"
for i in deck:
	print i

ana=Jogador('ana',maoana,0)
beto=Jogador('beto',maobeto,1)
ana.start()
beto.start()

ana.join()
beto.join()
