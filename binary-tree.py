import pprint
import random
import math

# Poly tempeliko gemisma dentrou, alla douleyei i anazitisi tou
# path.
# TODO: Na prosthesoume functionality `parent` sta nodes, gia na ginei
# ligo pio efficient o kwdikas
# nomizw mporei na koumpwsei i synartisi Access() apo katw.
#
# Peiramatizomaste k vlepoume


class Tree:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str_(self):
        return '%s' % self.data

def makeList(tree):
    paths = []
    if not (tree.left or tree.right):
        return [[tree.data]]
    if tree.left:
        paths.extend([[tree.data] + child for child in makeList(tree.left)])
    if tree.right:
        paths.extend([[tree.data] + child for child in makeList(tree.right)])
    return paths

# Gemisma dentrou
# ==================
# Estw oti to dentro einai tis morfis:
# level o                       [  ]
#                             /      \
#                   root.l   /         \    root.r
#                           /            \
# level 1                 [  ]            [  ]
#                         /  \             / \
#           root.l.l    /     \  r     l  /    \    root.r.r
#                     /        \          /       \
# level 2            [  ]      [  ]      [  ]      [  ]
#                   / \        / \        / \        / \
#      root.l.l.l  /  \ r   l /   \r    l /   \ r  l /   \    root.r.r.r
#                 /   \      /     \      /    \     /     \
# level 3      [   ]  [  ] [  ]  [  ]    [  ] [  ] [  ]   [  ]
#
#
#
#

# TEST!
# Edw bazw anti gia Bx se kathe node, ena dictionary pou periexei
# ena synolo apo blocks (3 gia twra).
# Douleyei, alla to meionektima einai oti logw tis symperiforas Typwnw
# dictionaries stin python, otan diavaseis ena dictionary, epistrefei
# ta zeygi key : value se anakatemeni seira.
# Lythike me pprint


tree_length = 46 #ta max nodes tou tree

# level 0 (root)
root = Tree({"B01" : "aa", "B02" : "ab", "B03" : "??"})
# level 1
root.left = Tree({"B04" : "fa", "B05" : "??", "B06" : "fd"})
root.right = Tree({"B07" : "a", "B08" : "b", "B09" : "??"})
# level 2
root.left.left = Tree({"B10" : "kd", "B11" : "??", "B12" : "di"})
root.left.right = Tree({"B13" : "ut", "B14" : "sb", "B15" : "??"})
root.right.left = Tree({"B16" : "??", "B17" : "bc", "B18" : "gg"})
root.right.right = Tree({"B19" : "kl", "B20" : "??", "B21" : "ml"})
# level 3
root.left.left.left = Tree({"B22" : "as", "B23" : "??", "B24" : "le"})
root.left.left.right = Tree({"B25" : "an", "B26" : "kb", "B27" : "??"})
root.left.right.left = Tree({"B28" : "??", "B29" : "bs", "B30" : "nb"})
root.left.right.right = Tree({"B31" : "??", "B32" : "lf", "B33" : "dc"})
root.right.left.left = Tree({"B34" : "lk", "B35" : "op", "B36" : "??"})
root.right.left.right = Tree({"B37" : "hr", "B38" : "??", "B39" : "de"})
root.right.right.left = Tree({"B40" : "sk", "B41" : "??", "B42" : "cs"})
root.right.right.right = Tree({"B43" : "??", "B44" : "qw", "B45" : "bi"})

# Typwnw tin lista me ola ta paths
print "========================================"
print "=                Paths                 ="
print "========================================"
print "\n"
paths = makeList(root)
pprint.pprint(paths)
print "\n"


# Dinw ena id se kathe path
print "\n\n"
print "========================================"
print "=             Give id and              ="
print "=           printing the paths         ="
print "========================================"
print "\n"
def pathId():
    path_dict = {}
    for i,path in enumerate(paths):
        #print "Path " + str(i) + ": " + str(path)
        path_dict.update({ i : path})
        #print path_dict
    return path_dict

# Typwnw me eydiakrito tropo ta paths
def printPaths(pdict):
    pprint.pprint(pdict)

get_paths = pathId()
printPaths(get_paths)

print "\n"

# Typwnw me eydiakrito tropo ta paths




# Dimiourgw kai typwnw to position map
print "========================================"
print "=            Position Map              ="
print "========================================"
print "\n"

position_map = {}

def createPositionMap(path_dict):
    # block = "a5"
    for i in range(tree_length):
        # Here we use zfill(2), in order to get two digits, e.g. 00, 01, 01, etc
        block = "B" + str(i).zfill(2)
        # print block # DEBUG
        for key, value in path_dict.items():
            for element in value:
                found = element.get(block)
                if found:
                    # print "B" + str(i) + ", with value (" + str(found) + ") found in path with id: " + str(key)
                    position_map[block] = key
    # print "\n"
    return pprint.pprint(position_map)
createPositionMap(get_paths)


# Dialegw px to 3o path gia na doylepsw
# Debug: Select path (hardcoded for now)
#
# TODO: Check if block exists in the
# position_map and if yes
# get the correct path

print "\n"
print "========================================"
print "=       Dialegw to path gia            ="
print "=        na to epeksergastw            ="
print "=       Estw to trito ([2])            ="
print "========================================"
print "\n"

selected_path = paths[2]
print selected_path
print "\n"

# TODO: Edw tha mpei to parsing tou path
# gia na paroume to value

# Estw oti thelw to block sti thesi 3
print "========================================"
print "=       Estw oti thelw to              ="
print "=        4o stoixeio, stin             ="
print "=       thesi `selected_path[3]`       ="
print "========================================"
print "\n"

block_for_use = selected_path[3]
print " Bucket pros epeksergasia: " + str(block_for_use)
print "\n"

#TODO ACCESS ORAM

print "========================================"
print "=           ACCESS ORAM                ="
print "=    	   esto zitao B03              ="
print "========================================"
print "\n"

def get_pos(pmap, pos):
    selected_path = 0
    for key in pmap:
        # print key DEBUG
        for value in str(pmap[key]):
            # print value DEBUG
            if pos in key:
                selected_path = value
    return selected_path

# print "Selected path: " + str(get_pos(position_map, 'B05')) # DEBUG

L = 3 #3 nodes vazeis

def access_oram(op, pos, data):
    # [STEP 1]
    x = pos
    # [STEP 2]
    new_pos = random.randint(0, (math.pow(2, L-1)-1))
    print "Random pos: " + str(new_pos)

    # [STEP 3]
    path = get_pos(position_map, pos)
    print "Selected path: " + str(path)

    # [STEP 4]
    for i in range(tree_length):
        for key, value in selected_path[0].items():
        	if key == pos:
        		data = value
        		break
    print("data of " + pos + ": " + data)

    # [STEP 5] [TODO] check if op is write (and remove this block from the stash)
    if op == "write":
		print("Write: [TODO]")

    # [STEP 6] [TODO] CHANGE POSITION OF BLOCK
    print(selected_path[new_pos])
    for key, value in selected_path[new_pos].items():
        if value == '??':
        	print("Writing on dummy Block " + key + " = " + value)
        	#WRITE [TODO]
        	break
    print("Updated bucket: " + str(selected_path[new_pos]))


access_oram('write', 'B03', '')
