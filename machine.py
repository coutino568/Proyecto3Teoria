

from transitions import Transition

class Machine(object):
	def __init__(self,**kwargs):


		self.errors =[]

		##Captura los errores al leer la definicion de la MT y si hay errores criticos no deberia avanzar el programa
		if 'states' in kwargs:
			self.states= kwargs['states']
		else:
			self.errors.append("En la definicion de la MT falto un listado de estados")
			self.states=[]

		if 'initialState' in kwargs:
			self.initialState=kwargs['initialState']
		else:
			self.errors.append("En la definicion de la MT falto un estado inical")

		

		if 'transitions' in kwargs:
			self.transitions = kwargs['transitions']
		else:
			self.errors.append("En la definicion de la MT falto la definicion de las transiciones")


		if 'alphabet' in kwargs:
			self.alphabet = kwargs['alphabet']
		else:
			self.errors.append("En la definicion de la MT falto la definicion del alfabeto")


		if 'tapeAlphabet' in kwargs:
			self.tapeAlphabet = kwargs['tapeAlphabet']
		else:
			self.errors.append("En la definicion de la MT falto la definicion del alfabeto de la cinta")



		if 'acceptanceStates' in kwargs:
			self.acceptanceStates = kwargs['acceptanceStates']
		else:
			self.errors.append("En la definicion de la MT falto la definicion de estados de aceptacion")

		if 'tape' in kwargs:
			self.tape = kwargs['tape']
		else:
			self.errors.append("En la definicion de la MT falto la definicion de la cinta que leera")



		print(self.acceptanceStates)




		self.currentState=self.initialState
		self.currentTapeIndex=0
		self.currentTapeInput = ""
		self.memorycache=""
		self.running = True


		print("TAPE : " + str(self.tape))
		print(len(self.tape))



		self.printID()


		while self.currentTapeIndex<len(self.tape)-1:

			if self.running:
				self.applyChange()
				self.printID()



		if self.currentState in self.acceptanceStates:
			print("FELICIDADES LA CINTA FUE ACEPTADA")

		else:
			print("LASTIMA LA CINTA NO FUE ACEPTADA")




	def printID(self):
		print("\nCurrent state:" + str(self.currentState))
		print("Current pointer on tape:" + str(self.currentTapeIndex))
		print("Current character on tape :" +str(self.tape[self.currentTapeIndex]) )
		print("Current data on cache : " + str(self.memorycache))




	#revisa en el conjunto de transiciones si encutnra un match
	def applyChange(self):
		self.currentTapeInput= self.tape[self.currentTapeIndex]
		for transition in self.transitions:
			if self.transitionMatches(transition):
				print("Encontre una transicion que hace match con los parametros actuales. HARE LOS CAMBIOS -->")

				self.currentState = transition.finalState
				self.memorycache = transition.memCacheValue
				#para evitar out of bounds
				if transition.tapeDisplacement=="R":
					self.currentTapeIndex = min(self.currentTapeIndex+1, len(self.tape)-1)
				else:
					self.currentTapeIndex = max(self.currentTapeIndex-1,0)
				



				#si llega al final de la cinta y el displacement es a la derecha, signifca que termino de leer

				if self.currentTapeIndex==len(self.tape)-1 and transition.tapeDisplacement=="R":
					self.running = False
				break



	#Funcion para validar si una descripcion hace match con la entrada de alguna transicion
	def transitionMatches(self, transition):

		if self.currentState== transition.initialState:
			if self.currentTapeInput== transition.tapeInput:
				if self.memorycache== transition.memCacheValue:
					return True

		return False