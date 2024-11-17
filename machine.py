

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

		if 'tapes' in kwargs:
			self.tapes = kwargs['tapes']
		else:
			self.errors.append("En la definicion de la MT falto la definicion de la cinta que leera")



		if 'debug' in kwargs:
			self.debug = kwargs['debug']
		else:
			self.debug = False


		# print(self.acceptanceStates)




		
		self.activeTape = 0

		# print("TAPE : " + str(self.tape))
		# print(len(self.tape))

		for tape in self.tapes:

			self.currentState=self.initialState
			self.currentTapeIndex=0
			self.currentTapeInput = ""
			self.memorycache=""
			self.running = True

			



			print("----------------------------------------------------------------------------")
			print("\nCINTA ACTIVA :\n" + str (self.tapes [self.activeTape]) + " \n ASI INICIO : ")
			self.printID()


			while self.currentTapeIndex<(len(self.tapes[self.activeTape])-1):

				if self.running:
					self.applyChange()
					# self.printID()

					if self.debug == True:
						self.printID()

			self.applyChange()

			print("\nASI TERMINO : ")
			self.printID()


			if self.currentState in self.acceptanceStates:
				print("FELICIDADES LA CINTA FUE ACEPTADA")

			else:
				print("LASTIMA LA CINTA NO FUE ACEPTADA")

			self.activeTape= self.activeTape +1




	def printID(self):
		print("\nCurrent state:" + str(self.currentState))
		print("Current pointer on tape:" + str(self.currentTapeIndex))
		print("Current character on tape :" +str(self.tapes[self.activeTape][self.currentTapeIndex]) )
		print("Current data on cache : " + str(self.memorycache))




	#revisa en el conjunto de transiciones si encutnra un match
	def applyChange(self):
		
		self.currentTapeInput= self.tapes[self.activeTape][self.currentTapeIndex]
		# print("Trying to aply cahanges")

		# print(self.transitions)
		for transition in self.transitions:
			# print("revisando transicion")





			if self.transitionMatches(transition):
				if(self.debug):
					print("Encontre una transicion que hace match con los parametros actuales. HARE LOS CAMBIOS -->")

				#si llega al final de la cinta y el displacement es a la derecha, signifca que termino de leer
				self.currentState = transition.finalState
				self.memorycache = transition.memCacheValue
				if self.currentTapeIndex==len(self.tapes[self.activeTape])-1 and transition.tapeDisplacement=="R":
					self.running = False
					break

				
				#para evitar out of bounds
				if transition.tapeDisplacement=="R":
					self.currentTapeIndex = min(self.currentTapeIndex+1, len(self.tapes[self.activeTape])-1)
				else:
					self.currentTapeIndex = max(self.currentTapeIndex-1,0)
				

				if len(transition.newMemCacheValue)>0:
					self.memorycache = transition.newMemCacheValue

				if len(transition.tapeOutput)>0:
					self.tapes[self.activeTape[self.currentTapeIndex]]=transition.tapeOutput
				
				break
			# else:
		# self.running = False
		# print("ERROR ; NO HAY UNA TRANSICION DEFINIDA")


	#Funcion para validar si una descripcion hace match con la entrada de alguna transicion
	def transitionMatches(self, transition):
		
		# print("transitionMatches")
		# print("\nCurrent state:" + str(self.currentState))
		# print("Current pointer on tape:" + str(self.currentTapeIndex))
		# print("Current character on tape :" +str(self.tapes[self.activeTape[self.currentTapeIndex]]) )

		if self.currentState== transition.initialState:
			if self.currentTapeInput== transition.tapeInput:
				if self.memorycache== transition.memCacheValue:
					return True

		return False