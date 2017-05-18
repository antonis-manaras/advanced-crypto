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
 	stash = [[0 for x in range(w)] for y in range(h)] 
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

	def map_client(self):
		#position map
		self.position_map[0][0] = "B0"
		self.position_map[0][1] = "0"
		self.position_map[1][0] = "B1"
		self.position_map[1][1] = "1"
		self.position_map[2][0] = "B2"
		self.position_map[2][1] = "2"

	# *******************************************************************
	# *********************** ACCESS ORAM *******************************

	def access_oram(self, op, pos, data):
		#[STEP0] since pos is block (by rizomiliotis) we must find the path by searching for this block in the stash
		path = 0
		index = 0
		for i in range(0, 3):
			if self.position_map[i][0] == pos:
				path = self.position_map[i][1]
				index = i
		#[STEP1] store current position
		x = pos
		#[STEP2] change this pos to random (0...2^L-1)
		new_pos = 'B'+str(random.randint(0, math.pow(2,self.L-1)))
		#print("[DEBUG] random pos: " + str(new_pos))		


		#[STEP3] We read all blocks from this path
		for i in range(0, self.L):
			if self.position_map[i][1] == path:
				self.stash[i][0] = self.position_map[i][0]
				self.stash[i][1] = path

		#[STEP4] data = block at position (pos) from stack 
		data = self.stash[index][0] #already have this since blocks dont have data in this project but whatever
		
		#[STEP5] check if op is write (and remove this block from the stash)
		if op == "write":
			stash[index][0] = ""
			stash[index][1] = ""
						
		#[STEP6] CHANGE POSITION OF BLOCK
		for i in range(self.L, 0):
			 #must put it in empy blocks TODO
			self.position_map[new_pos][0] = pos #DEMO
			self.position_map[new_pos][1] = path #DEMO
			 

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
oram.map_client()
print("")
oram.access_oram("read","B1","")
print("")
