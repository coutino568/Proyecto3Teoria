
from transitions import Transition



class Parser(object):
	def __init__(self,filename):

		with open(filename, "r") as file:
			self.lines= file.read().splitlines()    
		# for line in self.lines:
		# 	print(line)

		self.initialState=""
		self.acceptanceState=""
		self.transitions = []
		self.states =[]
		self.alphabet = []
		self.tapeAlphabet =[]
		self.strings=[]

		self.findStates()
		self.findAlphabet()
		self.findTapeAlphabet()
		self.findTransitions()
		self.findStrings()




	#funcion para encontrar los estados
	def findStates(self):
		qstateskeyword = "q_states"
		listkeyword= "q_list"
		initialkeyword= "initial"
		finalkeyword="final"
		singlequotation="'"

		#Itera en las lineas buscando a partir de donde leer los estados

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if qstateskeyword in self.lines[x]:
				statesindex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break



		for x in range(len(self.lines)):
			# print(self.lines[x])
			if listkeyword in self.lines[x]:
				statelistindex = x
				# print("encontre donde esta qlist, esta en la linea " + str(x))
				break
				

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if initialkeyword in self.lines[x]:
				initialindex = x
				# print("encontre donde esta initial, esta en la linea " + str(x))
				break

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if finalkeyword in self.lines[x]:
				finalindex = x
				# print("encontre donde esta final, esta en la linea " + str(x))
				break



		##iterare en el rango de las lineas donde podria estar el listado de estados

		for y in range(statelistindex,initialindex):
			newstate= self.findSubstring(self.lines[y],singlequotation,singlequotation)
			
			if len(newstate)>0:
				self.states.append(newstate)
		

		self.initialState = self.findSubstring(self.lines[initialindex],singlequotation,singlequotation)
		self.acceptanceState = self.findSubstring(self.lines[finalindex],singlequotation,singlequotation)



		print("STATES READ FORM DOC")
		print(self.states)
		print("ACCEPTANCE : " + self.acceptanceState)
		print("INITIAL : "+ self.initialState)




	#funcion para encontrar donde esta el alfabeto de lay lo guarda
	def findAlphabet(self):
		singlequotation="'"
		alphabetKeyword="alphabet"
		tapeAlphabetKeyword = "tape_alphabet"

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if alphabetKeyword in self.lines[x]:
				alphabetindex = x
				# print("encontre donde esta alphabetlist, esta en la linea " + str(x))
				break


		for x in range(len(self.lines)):
			# print(self.lines[x])
			if tapeAlphabetKeyword in self.lines[x]:
				tapeAlphabetIndex = x
				# print("encontre donde esta tapealphabet, esta en la linea " + str(x))
				break

		for y in range(alphabetindex,tapeAlphabetIndex):
			newCharacter= self.findSubstring(self.lines[y],singlequotation,singlequotation)
			
			if len(newCharacter)>0:
				self.alphabet.append(newCharacter)

		print("ALPHABET READ FROM DOC")
		print(self.alphabet)




	#finds alphabet from tape
	def findTapeAlphabet(self):
		singlequotation="'"
		deltaKeyword="delta"
		tapeAlphabetKeyword = "tape_alphabet"

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if tapeAlphabetKeyword in self.lines[x]:
				tapeindex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if deltaKeyword in self.lines[x]:
				deltaIndex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break


		for y in range(tapeindex,deltaIndex):
			newCharacter= self.findSubstring(self.lines[y],singlequotation,singlequotation)
			
			if len(newCharacter)>0:
				self.tapeAlphabet.append(newCharacter)


		print("TAPE ALPHABET READ FROM DOC")
		print(self.tapeAlphabet)








##define las transiciones
	def findTransitions(self):
		deltaKeyword="delta"
		paramsKeyword="params"
		simulationKeyword = "simulation_strings"
		transitionsIndexes = []

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if deltaKeyword in self.lines[x]:
				deltaIndex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break
		for x in range(len(self.lines)):
			# print(self.lines[x])
			if simulationKeyword in self.lines[x]:
				simulationIndex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break

		##tengo el rango dentro del cual estan las transiciones
		transitionsCount =0

		for x in range(deltaIndex,simulationIndex):
			if paramsKeyword in self.lines[x]:
				transitionsCount = 1+ transitionsCount
				transitionsIndexes.append(x)

		transitionsIndexes.append(simulationIndex)

		# print(transitionsIndexes)


		print("ENCONTRE " + str(transitionsCount) + " TRANSICIONES")


		for i in range(transitionsCount):


			start =transitionsIndexes[i]
			end = transitionsIndexes[i+1]


			# print("LEERE LA TRANSICION NUMERO : " + str(i) + " ; DESDE LA FILA " + str(start) + " HASTA LA FILA "+ str(end))
			newTransitionLines = self.lines[start:end]

			self.generateTransiton(newTransitionLines)


			# newTransition = Transition()
			# self.transitions.append(newTransition)






	#Funcion que recibe un bloque de lineas donde esta la definicion de una transicion y a partir de eso crea una instancia de transicion

	def generateTransiton(self, lines):

		memcount=0
		singlequotation= "'"
		for x in range (len(lines)):
			line = lines[x]


			if "initial_state" in line:
				initialState= self.findSubstring(line,singlequotation,singlequotation)
			if "mem_cache_value" in line and memcount==0 :
				initialMem = self.findSubstring(line,singlequotation,singlequotation)
				memcount= memcount+1
			if "tape_input" in line:
				tapeInput = self.findSubstring(line,singlequotation,singlequotation)
			if "final_state" in line :
				finalState= self.findSubstring(line,singlequotation,singlequotation)
			if "mem_cache_value" in line and memcount==1:
				finalMem = self.findSubstring(line,singlequotation,singlequotation)
			if "tape_output" in line :
				tapeOutput = self.findSubstring(line,singlequotation,singlequotation)
			if "tape_displacement" in line :
				tape_displacement = self.findSubstring(line,singlequotation,singlequotation)


		newTransition = Transition(initialState=initialState,memCacheValue=initialMem,tapeInput=tapeInput,finalState=finalState,newMemCacheValue=finalMem,tapeOutput=tapeOutput,tapeDisplacement=tape_displacement) 
		self.transitions.append(newTransition)












##encuentra las cadenas en el archivo
	def findStrings(self):
		simulationKeyword="simulation_strings"
		

		for x in range(len(self.lines)):
			# print(self.lines[x])
			if simulationKeyword in self.lines[x]:
				simulationIndex = x
				# print("encontre donde esta qstates, esta en la linea " + str(x))
				break




		for y in range(simulationIndex,len(self.lines)):
			if "-" in self.lines[y]:
				newString= self.lines[y][1:len(self.lines[y])]
				self.strings.append(newString)
			


		print("STRINGS READ FROM DOC")
		print(self.strings)






	def findSubstring(self, bigstring, first, last ):
		try:
			start = bigstring.index( first ) + len( first )
			end = bigstring.index( last, start )
			return bigstring[start:end]
		except ValueError:
			return ""
        	#print("no encotre nada con single quotes")


