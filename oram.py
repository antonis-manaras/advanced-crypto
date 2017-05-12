import math

class Oram:
	#MAX ORAM SIZE
	oram_size = 60;
 	w, h = oram_size, oram_size
 	#STASH
 	stash = [[0 for x in range(w)] for y in range(h)] 
 	#POSITION MAP
	position_map = [[0 for x in range(w)] for y in range(h)] 
	#bucket
	bucket = [0 for y in range(h)] 

	# *******************************************************************
	# ********************* CREATE ORAM TREE ****************************

	def create_oram(self):
		node_id = 0
		print("[DEBUG] Creating DEMO tree with nodes (PATH)")
		for i in range (3):
			for j in range (i*3):
				self.position_map[node_id][0] = "B"+str(node_id) #ID TOU NODE
				self.position_map[node_id][1] = str(j) #PATH TOU NODE
				self.bucket[node_id] = math.pow(2, node_id) #O BUCKET DEN EXEI DOMH, EINAI = 2^L 
				print("[" + str(self.position_map[node_id][0]) + "," + str(self.position_map[node_id][1]) + "] => " + str(self.bucket[node_id]))
				node_id+=1

	# *******************************************************************
	# *********************** ACCESS ORAM *******************************

	def access_oram(self, op, pos, data):
		x = pos #store current position
		print("[DEBUG] Printing bucket and nodes with pos in path: " + str(pos))

		for l in range (0, 9): #for l - 0(root) until leaf level (9)
			if self.position_map[l][1] == pos: #and get all blocks from server P(x) in this position ( min[S,bucketsize] ??? )
				self.stash.append(self.position_map[l][0]) #set stash = stash U P(x) since i'm inside this loop
				print("[NODE]: " + str(self.position_map[l][0]) + " , [BUCKET]: " + str(self.bucket[l])) #[DEBUG] print bucket

		if op == "write": #if operation is write
			print("writing process") #DEBUG

		#TODO
		#set S = STASH - S
		#if |S| < bucketsize add dummies
		#print("Updated Position Map: " + str(self.position_map)) #print updated position map

	print("")
	print("**************************************************")
	print("PATH-ORAM by Antonis Manaras & Vasilis Kouliaridis")
	print("**************************************************")
	print("")

	# *******************************************************************
	# ****************** RUN DEBUG FUNCTIONS ****************************

oram = Oram()
oram.create_oram()
print("")
oram.access_oram("read","1","")
print("")
