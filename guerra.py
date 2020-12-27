#!/usr/bin/env python3
from random import shuffle
from random import randint

class Carta:
	semi = ["Cuori","Quadri","Fiori","Picche"] #REGOLA DEL GIOCO: I SEMI SONO IN ORDINE DI GRANDEZZA: ES. PICCHE > FIORI ETC.
	valori = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Donna","Re","Asso"]
	def __init__(self,valore,seme):
		self.valore = valore
		self.seme = seme
	def __repr__(self):
		v = self.valori[self.valore] + " di " + self.semi[self.seme]
		return v
	def stampa(self):
		p = self.valori[self.valore] + " di " + self.semi[self.seme]
		return p
	def __lt__(self,altra):
		if self.valore < altra.valore:
			return True
		if self.valore > altra.valore:
			return False
		if self.seme < altra.seme:
			return True
		return False

class Mazzo:
	def __init__(self):
		self.lista = []
	def aggiungi_carta(self,carta):
		self.lista.append(str(carta))
	def rimuovi_carta(self,carta):
		self.lista.pop(self.lista.index(str(carta)))
	def mischia(self):
		shuffle(self.lista)
	
class Gioco:
	def __init__(self):
		g1 = input("Inserisci il nome del giocatore 1: ")
		g2 = input("Inserisci il nome del giocatore 2: ")
		self.puntig1=0
		self.puntig2=0
		self.turni=0
		self.mazzo = Mazzo()
		for i in range(2,15):
			for j in range(0,4):
				self.mazzo.aggiungi_carta(Carta(i,j))
		self.mazzo.mischia()
		while True:
			print("")
			pescatag1 = self.pesca()
			pescatag2 = self.pesca()
			print(g1 + " ha pescato " + str(pescatag1))
			print(g2 + " ha pescato " + str(pescatag2))
			if pescatag1 < pescatag2:
				self.puntig2 = self.puntig2 + 1
				print("Questo turno è stato vinto da "+ g2)
				self.turni = self.turni + 1
			else:
				self.puntig1 = self.puntig1 + 1
				print("Questo turno è stato vinto da "+ g1)
				self.turni = self.turni + 1
			if self.turni == 26:
				break
			else:
				print("")
				input("Premi qualsiasi tasto per continuare...")
		print("")
		print("")
		if self.puntig1 > self.puntig2:
			print("Congratulazioni " + g1 + " hai vinto! [{}-{}]".format(self.puntig1,self.puntig2))

		if self.puntig2 > self.puntig1:
			print("Congratulazioni " + g2 + " hai vinto! [{}-{}]".format(self.puntig1,self.puntig2))
		
		if self.puntig2 == self.puntig1:
			print("La partita finisce con un pareggio! [{}-{}]".format(self.puntig1,self.puntig2))
		print("")
		print("")
	def pesca(self):
		while True:
			try:
				x = Carta(randint(2,15),randint(0,4))
				y = x.stampa()
				if y in self.mazzo.lista:
					self.mazzo.rimuovi_carta(x)
					return x
					break
			except:
				pass
while True:
	x = input("Inserisci 'gioca' per giocare o 'esci' per uscire: ")
	if x == "gioca":
		gioco = Gioco()
	if x == "esci":
		break