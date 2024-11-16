

class Transition(object):
	def __init__(self,**kwargs):

		self.errors = []
		##Definicion de los componentes necesarios para una transicion, y de hacer falta 
		if 'initialState' in kwargs:
			# print("Si hay initialState")
			self.initialState=kwargs['initialState']
		else:
			self.errors.append("TRANSICION SIN ESTADO INICIAL")

		##no necesario, se asume que estaria vacio
		if 'memCacheValue' in kwargs:
			# print("Si hay memCacheValue")
			self.memCacheValue=kwargs['memCacheValue']
		else:
			# errors.add("TRANSICION SIN memCacheValue")
			self.memCacheValue=""


		##campo necesario
		if 'tapeInput' in kwargs:
			# print("Si hay tapeInput")
			self.tapeInput=kwargs['tapeInput']
		else:
			self.errors.append("TRANSICION SIN tapeInput")

		##campo necesario
		if 'finalState' in kwargs:
			# print("Si hay finalState")
			self.finalState=kwargs['finalState']
		else:
			self.errors.append("TRANSICION SIN finalState")


    	##campo necesario
		if 'newMemCacheValue' in kwargs:
			# print("Si hay newMemCacheValue")
			self.newMemCacheValue=kwargs['newMemCacheValue']
		else:
			self.errors.append("TRANSICION SIN newMemCacheValue")
			self.newMemCacheValue=""




		##campo necesario
		if 'tapeOutput' in kwargs:
			# print("Si hay tapeOutput")
			self.tapeOutput=kwargs['tapeOutput']
		else:
			self.errors.append("TRANSICION SIN tapeOutput")
			self.tapeOutput=""


		##campo necesario
		if 'tapeDisplacement' in kwargs:
			# print("Si hay tapeDisplacement")
			self.tapeDisplacement=kwargs['tapeDisplacement']
		else:
			self.errors.append("TRANSICION SIN tapeDisplacement")



		# if(len(self.errors)>0):
		# 	print(self.errors)


    	
	def printTransition (self):

		print("THIS TRANSITION IS DEFINED THIS WAY:")
		print("INITIAL STATE : "+ str(self.initialState))
		print("TAPE INPUT :" + str( self.tapeInput))
		print("MEM CACHE VALUE :" + str( self.memCacheValue))
		print("NEW STATE : " + str(self.finalState))
		print("TAPE OUTPUT :" + str( self.tapeOutput))
		print("TAPE DISPLACEMENT :" + str( self.tapeDisplacement))
		print("NEW MEM CACHE VALUE: "+ str (self.newMemCacheValue))

    	