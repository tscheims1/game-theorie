import sys
class Node:

	def __init__(self):
		self.children = []
		self.value = sys.maxsize
	def __str__(self):
		if len(self.children) ==0:
			return str(self.value)
		
		return str(self.value)+"(" + ", ".join([str(child) for child in self.children]) + ")"
	
	def list_to_tree(self,l):
		if(isinstance(l,list)):
			for ele in l:
				node = Node()
				node.list_to_tree(ele)			
				self.children.append(node)
		else:
			self.value = l
		

class MinMax:
	def __init__(self,tree):
		self.tree = tree
	
	def run(self):
		return self._run(self.tree,1)
		
	def _run(self,node,deep):
		if(len(node.children)==0):	
			return node.value		# base case -> terminal reached
		
		if(deep%2 == 0):bestVal = sys.maxsize
		else: bestVal = -sys.maxsize
		
		for child in node.children:
			value = self._run(child,deep+1)
			
			if(deep%2 == 0): bestVal = min(bestVal,value)
			else: bestVal = max(bestVal,value)
						
		return bestVal

class NegaMax:
	def __init__(self,tree):
		self.tree = tree
	
	def run(self):
		return self._run(self.tree,1,1)
		
	def _run(self,node,deep,color):
		if(len(node.children)==0):	
			return node.value*color		# base case -> terminal reached
		
		bestVal = -sys.maxsize
		for child in node.children:
			value = -self._run(child,deep+1,-color)
			bestVal = max(bestVal,value)
					
		return bestVal
		
		
if __name__ == "__main__":
	root = Node()
	tree =  [ [ [ [10, 11] , [9,12] ] , [ [14,15] , [13,14] ] ] , [ [ [5,2] , [4,1] ] , [ [3,22] , [20,21] ] ] ]

	root.list_to_tree(tree)
	#print (root)
	minmax = MinMax(root)
	print (minmax.run())
	negamax = NegaMax(root)
	print(negamax.run())



