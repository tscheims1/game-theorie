
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
a = [1,2,3,4]
print (str(trans.addAndCheck(a,a)))
print (str(trans.addAndCheck(a,1)))
print (str(trans.addAndCheck(a,a)))


