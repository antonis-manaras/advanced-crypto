import math
import random

class BinaryTree():    
	def __init__(self,rootid):      
		self.left = None      
		self.right = None      
		self.rootid = rootid    

	def getLeftChild(self):        
		return self.left    

	def getRightChild(self):        
		return self.right    

	def setNodeValue(self,value):        
		self.rootid = value    

	def getNodeValue(self):        
		return self.rootid    

	def insertRight(self,newNode):        
		if self.right == None:            
			self.right = BinaryTree(newNode)        
		else:            
			tree = BinaryTree(newNode)            
			tree.right = self.right            
			self.right = tree    

	def insertLeft(self,newNode):        
		if self.left == None:            
			self.left = BinaryTree(newNode)        
		else:            
			tree = BinaryTree(newNode)            
			self.left = tree            
			tree.left = self.left

	def printTree(self,tree):        
		if tree != None:            
			self.printTree(tree.getLeftChild())            
			print(tree.getNodeValue())            
			self.printTree(tree.getRightChild())

class Oram:
	#MAX ORAM SIZE
 	w, h = 10, 10
 	#STASH
 	stash = [] 
 	#POSITION MAP
	position_map = [[0 for x in range(w)] for y in range(h)] 
	L = 4 #We set L = 4
	# *******************************************************************
	# ********************* CREATE ORAM TREE ****************************

	def create_tree(self):
		myTree = BinaryTree("B0")    
		myTree.insertLeft("B1")    
		myTree.insertRight("B2")
		myTree.printTree(myTree)

	# *******************************************************************
	# *********************** ACCESS ORAM *******************************

	def access_oram(self, op, pos, data):
		#[STEP1] store current position
		x = pos 
		#[STEP2] change this pos to random (0...2^L-1)
		new_pos = random.randint(0, math.pow(2,self.L-1)) 
		#print("[DEBUG] random pos: " + str(new_pos))		


		#[STEP3] something with stack and buckets
		for i in range(0, self.L):
			print("TODO")

		#[STEP4] data = block at position (pos) from stack 
		data = self.stash[pos]
		
		#[STEP5] check if op is write
		if op == "write":
			print("[DEBUG] op: Write")
						
		#[STEP6] CHANGE POSITION OF BLOCK
		for i in range(self.L, 0):
			print("TODO")

	# *******************************************************************
	# ****************** RUN DEBUG FUNCTIONS ****************************



print("")
print("**************************************************")
print("PATH-ORAM by Antonis Manaras & Vasilis Kouliaridis")
print("**************************************************")
print("")

oram = Oram()
oram.create_tree()
print("")
oram.access_oram("read","1","B1")
print("")
