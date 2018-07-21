
def remove_accents(s):
	l = ['.',',','\n',':',';',' ']
	for c in l:
		try:
			s = s.replace(c,'')
		except:
			pass
	print s

s="""
I was angry with my friend; 
I told my wrath, my wrath did end. 
I was angry with my foe: 
I told it not, my wrath did grow. 

And I waterd it in fears, 
Night and morning with my tears: 
And I sunned it with smiles, 
And with soft deceitful wiles. 

And it grew both day and night. 
Till it bore an apple bright. 
And my foe beheld it shine, 
And he knew that it was mine. 

And into my garden stole, 
When the night had veild the pole; 
In the morning glad I see; 
My foe outstretched beneath the tree.
hnrvrossonero
"""
#hnrv cry 200
s2="""
Ero adirato col mio amico,
Dissi la mia ira, la mia ira fini;
ero adirato col mio nemico,
non la dissi, la mia ira crebbe.
E l ho bagnata di timori,
notte e giorno con le mie lacrime,
e le ho dato il sole di sorrisi
e dolci ingannevoli astuzie.
 
Ed e cresciuta sia di giorno che di notte,
finche ha portato una mela luminosa;
ed il mio nemico la vide risplendere,
e seppe che era mia.
 
E penetro nel mio giardino
quando la notte aveva velato il cielo;
nella mattina lieto vedo
il mio nemico steso morto sotto l albero.
hnrvapoisontreeviakasiski
"""
remove_accents(s2.lower())

