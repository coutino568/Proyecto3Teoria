filename = "example1.yaml"
filename2= "example2.yaml"


from transitions import Transition
from machine import Machine
from parser import Parser



parser = Parser(filename2)
debug=False


# transicion1= Transition(initialState="q1",tapeInput='a',finalState="q2",tapeDisplacement='R')
# transicion2= Transition(initialState="q1",tapeInput='b',finalState="q4",tapeDisplacement='R')
# transicion3= Transition(initialState="q2",tapeInput='a',finalState="q2",tapeDisplacement='R')
# transicion4= Transition(initialState="q2",tapeInput='b',finalState="q3",tapeDisplacement='R')

# transicion5= Transition(initialState="q3",tapeInput='a',finalState="q5",tapeDisplacement='R')
# transicion6= Transition(initialState="q3",tapeInput='b',finalState="q3",tapeDisplacement='R')

# transicion7= Transition(initialState="q4",tapeInput='a',finalState="q4",tapeDisplacement='R')
# transicion8= Transition(initialState="q4",tapeInput='b',finalState="q4",tapeDisplacement='R')

# transicion9= Transition(initialState="q5",tapeInput='a',finalState="q5",tapeDisplacement='R')
# transicion10= Transition(initialState="q5",tapeInput='b',finalState="q4",tapeDisplacement='R')


# transicion1.printTransition()



# maquinita = Machine(alphabet=['a','b'],
# 	states=["q1","q2","q3","q4","q5"],
# 	 initialState="q1",
# 	 acceptanceStates=["q5"],tapeAlphabet=["1","0"] ,
# 	  tape="aabbbaab",
# 	   transitions=[transicion1,transicion2,transicion3,transicion4,transicion5,transicion6,transicion7,transicion8,transicion9,transicion10])


    
#     


maquinita = Machine(alphabet=parser.alphabet,
	states=[parser.states],
	 initialState=parser.initialState,
	 acceptanceStates=parser.acceptanceState,
	 tapeAlphabet=parser.tapeAlphabet ,
	  tapes=parser.strings,
	  transitions=parser.transitions,
	  debug=debug)


    
