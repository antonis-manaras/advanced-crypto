class Oram:
	#MAX ORAM SIZE
	oram_size = 60;
 	#STASH
 	w, h = oram_size, oram_size
 	stash = [[0 for x in range(w)] for y in range(h)] 
 	#POSITION MAP
 	w, h = oram_size, oram_size
	position_map = [[0 for x in range(w)] for y in range(h)] 

	# *******************************************************************
	# ********************* CREATE ORAM TREE ****************************

	def create_oram(self):
		node_id = 0
		print("[DEBUG] Creating DEMO tree with nodes")
		for i in range (3):
			for j in range (i*3):
				self.position_map[node_id][0] = "B"+str(node_id)
				self.position_map[node_id][1] = str(j)
				print("[" + str(self.position_map[node_id][0]) + "," + str(self.position_map[node_id][1]) + "]")
				node_id+=1

	# *******************************************************************
	# *********************** ACCESS ORAM *******************************

	def access_oram(self, op, pos, data):
		x = pos #store current position
		bucket = []
		print("[DEBUG] Printing nodes with pos in path: " + str(pos))

		for l in range (0, 9): #for l - 0(root) until leaf level (9)
			if self.position_map[l][1] == pos: #and get all blocks from server P(x) in this position
				bucket.append(self.position_map[l][0])
				self.stash.append(self.position_map[l][0]) #set stash = stash U P(x) since i'm inside this loop

		if op == "write": #if operation is write
			print("writing process") #DEBUG

		print("Bucket: " + str(bucket)) #print full path (bucket)
		#TODO
		#if |S| < bucketsize add dummies
		#print("Updated Position Map: " + str(self.position_map)) #print updated position map

	# *******************************************************************
	# ****************** RUN DEBUG FUNCTIONS ****************************

oram = Oram()
oram.create_oram()
oram.access_oram("read","1","")
