import sys
class Node:

	def __init__(self,no,parent):
		self.children = []
		self.value = sys.maxsize
		self.nodeNo = no
		self.parent = parent

	def __str__(self):
		if len(self.children) ==0:
			return str(self.value)
		
		return str(self.value)+"(" + ", ".join([str(child) for child in self.children]) + ")"
	
	def list_to_tree(self,l):
		if(isinstance(l,list)):
			for ele in l:
				nodeNo = ""
				if(self.nodeNo ==""): nodeNo = (str(len(self.children)+1))	
				else: nodeNo = str(self.nodeNo)+"."+(str(len(self.children)+1))	

				node = Node(nodeNo,self)
				node.list_to_tree(ele)			
				self.children.append(node)
		else:
			self.value = l
	def getHeuristicValue(self):
		return self.value
		
	def getNodeInfo(self):
		return str(self.nodeNo)

class MinMax:
	def __init__(self,tree):
		self.tree = tree
	
	def run(self):
		return self._run(self.tree,1)
		
	def _run(self,node,deep):
		if(len(node.children)==0):	
			return node.getHeuristicValue()		# base case -> terminal reached
		
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
			return node.getHeuristicValue()*color		# base case -> terminal reached
		
		bestVal = -sys.maxsize
		for child in node.children:
			value = -self._run(child,deep+1,-color)
			bestVal = max(bestVal,value)
					
		return bestVal

class AlphaBeta:
	def __init__(self,tree):
		self.tree = tree
	def run(self):
		return self._run(self.tree,10,-sys.maxsize,sys.maxsize,1)

	def _run(self,node,depth,alpha,beta,isMaxPlayer):
		if depth == 0 or len(node.children) == 0:
			return node.getHeuristicValue()
			
		v = -sys.maxsize
		if(isMaxPlayer == 1):
			for child in node.children:
				v = max(v,self._run(child,depth-1,alpha,beta,0))
				alpha = max(alpha,v)
				if(beta <= alpha):
					print (" beta cutoff at depht"+str(depth)+" #"+node.getNodeInfo())
					break
			return v
		else:
			v = sys.maxsize
			for child in node.children:
				v = min(v,self._run(child,depth-1,alpha,beta,1))
				beta = min(beta,v)
				if( beta <= alpha):
					print ("alpha cuttof at depth"+str(depth)+" #"+node.getNodeInfo())
					break
			return v
	
		
		
if __name__ == "__main__":
	root = Node("",None)
	tree =  [ [ [ [10, 11] , [9,12] ] , [ [14,15] , [13,14] ] ] , [ [ [5,2] , [4,1] ] , [ [3,22] , [20,21] ] ] ]

	root.list_to_tree(tree)
	#print (root)
	minmax = MinMax(root)
	print (minmax.run())
	negamax = NegaMax(root)
	print(negamax.run())
	alphabeta = AlphaBeta(root)
	print(alphabeta.run())


