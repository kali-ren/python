#!/usr/bin/python
import random, threading, Queue

deck=[]

mutex = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)
mutex3 = threading.Semaphore(1)
mutex4 = threading.Semaphore(1)
	
mutexwinner = threading.Semaphore(1)
mutexprint = threading.Semaphore(1)
mutexprint2 = threading.Semaphore(1)

full = threading.Semaphore(2)
full2 = threading.Semaphore(2)
full3 = threading.Semaphore(2)
full4 = threading.Semaphore(2)

empty = threading.Semaphore(0)
empty2 = threading.Semaphore(0)
empty3 = threading.Semaphore(0)
empty4 = threading.Semaphore(0)

buff1=Queue.Queue(3)
buff2=Queue.Queue(3)
buff3=Queue.Queue(3)
buff4=Queue.Queue(3)

listabuffer=[buff1,buff2,buff3,buff4]
mutexes=[mutex,mutex2,mutex3,mutex4]
fulls=[full,full2,full3,full4]
emptys=[empty,empty2,empty3,empty4]

winner = 43
mickjagger = 43
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
		self.nome = nome
		self.mao = mao
		self.idd = idd

	def bufferget(self):
		return self.idd

	def buffdrop(self):
		if self.idd == 0:
			return 3
		else:
			r = self.idd - 1
			return r

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
		indice = aux.index(high)
		if high == 4:
			for i in self.mao:
				if i.num != indice and i.num != low:
					return i
                elif high == 3:
 			for i in self.mao:
				if i.num != indice and i.num != low:
					return i
		else:
			a = random.randint(0,4)
			o = self.mao[a]
			return o

	def getcard(self):
		global mutexes
		global emptys
		global fulls
		b = self.bufferget()
		mutexes[b].acquire()
		size = listabuffer[self.bufferget()].qsize()
		if  size == 0:
			print "%s dormiu buffer vazio!" %(self.nome)		
		mutexes[b].release()
		
		fulls[b].acquire()
		mutexes[b].acquire()
		if size == 0:
			print "%s acordou !" % (self.nome)
		a = listabuffer[b].get()
		self.mao.append(a)
		mutexprint.acquire()
		print "i, %s, get " % (self.nome) + str(a) + " %s mao: " %(self.nome)
		for i in range(len(self.mao)):
			print self.mao[i]
		mutexprint.release()
		mutexes[b].release()
		emptys[b].release()
	
	def drop(self):
			global mutexes
			global emptys
			global fulls
			a = self.buffdrop()
			size = listabuffer[a].qsize()
			mutexes[a].acquire()
			if size == 2:
				print "%s dormiu buffer cheio !" % (self.nome)
			mutexes[a].release()
			
			emptys[a].acquire()
			mutexes[a].acquire()

			if size == 2:
				print "%s acordou !" % (self.nome)
			
			b = self.freq()
			try:
				self.mao.remove(b)
			except:
				pass
			mutexprint.acquire()
			print "%s dropped " % (self.nome) + str(b)
			mutexprint.release()
			listabuffer[a].put(b)
			mutexes[a].release()
			fulls[a].release()		
#	def win(self):
		
	def setwinner(self,ide):
		global winner
		global emptys
		global fulls
		mutexwinner.acquire()
		if winner == 43:
			winner = ide
			print 'proxeneta'
			for i in range(4):
				emptys[i].release()
				fulls[i].release()
		mutexwinner.release()

	
	def check(self):
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
		if high == 4:
			return True
		else:
			return False

	def testevenceu(self):
		global winner
		mutexwinner.acquire()
		venceu = winner
		mutexwinner.release()
		if venceu != 43:
			return True
		else:
			return False
	def nome(self,idd):
		print "we have a winner"
		print "%s ganhou" %(listajogadores[idd].nome)
	def run(self):
		global winner
		a=0
		while self.testevenceu()==False:
			self.getcard()	
			self.drop()
			if self.check()==True:
				print "oiiiiiiiiiiiiiii" + self.nome
				self.setwinner(self.idd)	
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
Deck().gerarmao(maocarla)
Deck().gerarmao(maodani)

Deck().gerarbuffer(buff1)
Deck().gerarbuffer(buff2)
Deck().gerarbuffer(buff3)
Deck().gerarbuffer(buff4)

print "////////////////////////depois\n"
for i in deck:
	print i

ana=Jogador('ana',maoana,0)
beto=Jogador('beto',maobeto,1)
carla=Jogador('carla',maocarla,2)
dani=Jogador('dani',maodani,3)
listajogadores=['ana','beto','carla','dani']
ana.start()
beto.start()
carla.start()
dani.start()

ana.join()
beto.join()
carla.join()
dani.join()

if winner != 43:
	print "we have a winner " + str(listajogadores[winner])
