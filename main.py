filename = "example1.yaml"



from transitions import Transition
from machine import Machine



with open(filename, "r") as file:
            lines= file.read().splitlines()
            
   

        
for line in lines:
    print(line)



transicion1= Transition(initialState="q1",tapeInput='a',finalState="q2",tapeDisplacement='R')
transicion1.printTransition()
maquinita = Machine(alphabet=['a','b'],states=["q1","q2","q3"], initialState="q1",acceptanceStates=["q3"],tapeAlphabet=["1","0"] , tape="aabb")


    
    