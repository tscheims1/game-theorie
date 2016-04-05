import numpy as np
class Transposition(object):
	def __init__(self):
		self.dict = {}
	def add(self,board,node):
		if(self.dict[np.array_str(board)] == None)
			self.dict[np.array_str(board)] = board

	def isCalculated(self,board,node):
		obj = self.dict[np.array_str(board)]
		return obj != node and obj !=None

