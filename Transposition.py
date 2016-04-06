import numpy as np
class Transposition(object):
	def __init__(self):
		#hash-map
		self.dict = {}
	
	#Return the already calculated node or None
	def addAndCheck(self,board,node):
		obj = self.dict.get(str(board))
		if(obj == node):
			return None
		if(obj == None):
			self.dict[str(board)] = node
			return None
		else:
			return obj


trans = Transposition()
a = np.zeros((6, 7), dtype=np.uint8)
b = object()
c = object()

print (str(trans.addAndCheck(a,b)))
print (str(trans.addAndCheck(a,c)))
print (str(trans.addAndCheck(a,b)))
a[0][1] = 1
print (str(trans.addAndCheck(a,c)))

