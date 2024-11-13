

from transitions import Transition

class Machine(object):
	def __init__(self,**kwargs):

		if 'states' in kwargs:
			self.states= kwargs['states']
		else:
			self.errors.append("En la definicion de la MT falto un listado de estados")
			self.states=[]


		self.initialState=""
		self.transitions = []
		self.alphabet=[]
		self.tapeAlphabet=[]
		self.initialState=""
		self.acceptanceStates=[]
		self.currentState=""
		self.currentTapeIndex=0
		self.tape=""
		self.memorycache=""








	def printID(self):
		print("Current state:" + str(self.currentState))
		print("Current pointer on tape:" + str(self.currentTapeIndex))
		print("Current character on tape :" +str(self.tape[currentTapeIndex]) )
		print("Current data on cache : " + str(self.memorycache))





	def applyChange(self):
		for transition in transitions:
			if currentState == transition.innitialState:
				print("Encontre una transicion que hace match con el estado actual")

