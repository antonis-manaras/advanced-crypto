class Oram:
	oram_size = 60;
 	#stash
 	w, h = oram_size, oram_size
 	stash = [[0 for x in range(w)] for y in range(h)]
 	#position map
 	w, h = oram_size, oram_size
	position_map = [[0 for x in range(w)] for y in range(h)]

	def create_oram(self):
		node_id = 0
		for i in range (3):
			for j in range (i*3):
				self.position_map[i][0] = "B"+str(node_id)
				self.position_map[i][1] = str(j)
				print("[" + str(self.position_map[i][0]) + "," + str(self.position_map[i][1]) + "]")
				node_id+=1

oram = Oram()
oram.create_oram()
