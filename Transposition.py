import numpy as np
class Transposition(object):
	def __init__(self):
		#hash-map
		self.dict = {}
	
	#Return 0 if the node can clipped
	def addAndCheck(self,board,node):
		obj = self.dict.get(str(board))
		if(obj == node):
			return 1
		if(obj == None):
			self.dict[str(board)] = node
			return 1
		else:
			return 0


trans = Transposition()
a = np.zeros((6, 7), dtype=np.uint8)
b = object()
c = object()
a[0][1] = 1
print (str(trans.addAndCheck(a,b)))
print (str(trans.addAndCheck(a,c)))
print (str(trans.addAndCheck(a,b)))
a[0][1] = 1
print (str(trans.addAndCheck(a,b)))

