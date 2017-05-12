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
		bucket = []
		print("[DEBUG] Printing nodes with pos in path: " + str(pos))

		for i in range (0, 8): #Check position map array
			if self.position_map[i][1] == pos: #and add nodes with this position to bucket
				bucket.append(self.position_map[i][0])

		if op == "write": #if operation is write
			print("writing process") #DEBUG

		print(bucket) #print full path (bucket)

	# *******************************************************************
	# ****************** RUN DEBUG FUNCTIONS ****************************

oram = Oram()
oram.create_oram()
oram.access_oram("read","1","")
