#import random as r
import pprint


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
# level o                       [B1]
#                             /      \
#                   root.l   /         \    root.r
#                           /            \
# level 1                 [??]            [B3]
#                         /  \             / \
#           root.l.l    /     \  r     l  /    \    root.r.r
#                     /        \          /       \
# level 2            [B4]      [B5]      [??]      [B7]
#                   / \        / \        / \        / \
#      root.l.l.l  /  \ r   l /   \r    l /   \ r  l /   \    root.r.r.r
#                 /   \      /     \      /    \     /     \
# level 3      [B8]  [??] [B10]  [B11] [B12] [B13] [??]   [B15]
#
#
#
#

# # level 0 (root)
# root = Tree("B1")
# # level 1
# root.left = Tree("??")
# root.right = Tree("B3")
# # level 2
# root.left.left = Tree("B4")
# root.left.right = Tree("B5")
# root.right.left = Tree("??")
# root.right.right = Tree("B7")
# # level 3
# root.left.left.left = Tree("B8")
# root.left.left.right = Tree("??")
# root.left.right.left = Tree("B10")
# root.left.right.right = Tree("B11")
# root.right.left.left = Tree("B12")
# root.right.left.right = Tree("B13")
# root.right.right.left = Tree("??")
# root.right.right.right = Tree("B15")

# TEST!
# Edw bazw anti gia Bx se kathe node, ena dictionary pou periexei
# ena synolo apo blocks (3 gia twra).
# Douleyei, alla to meionektima einai oti logw tis symperiforas Typwnw
# dictionaries stin python, otan diavaseis ena dictionary, epistrefei
# ta zeygi key : value se anakatemeni seira. <-- TODO


# level 0 (root)
root = Tree({"B1" : "aa", "B2" : "ab", "B3" : "??"})
# level 1
root.left = Tree({"B2" : "fa", "B3" : "??", "B4" : "fd"})
root.right = Tree({"B5" : "a", "B6" : "b", "B7" : "??"})
# level 2
root.left.left = Tree({"B8" : "kd", "B9" : "od", "B10" : "di"})
root.left.right = Tree({"B11" : "ut", "B12" : "sb", "B13" : "lm"})
root.right.left = Tree({"B15" : "??", "B16" : "bc", "B17" : "gg"})
root.right.right = Tree({"B18" : "kl", "B19" : "??", "B20" : "ml"})
# level 3
root.left.left.left = Tree({"B21" : "as", "B22" : "??", "B23" : "le"})
root.left.left.right = Tree({"B24" : "an", "B25" : "kb", "B26" : "??"})
root.left.right.left = Tree({"B27" : "da", "B28" : "bs", "B29" : "nb"})
root.left.right.right = Tree({"B30" : "??", "B31" : "lf", "B32" : "dc"})
root.right.left.left = Tree({"B33" : "lk", "B34" : "op", "B35" : "??"})
root.right.left.right = Tree({"B36" : "hr", "B37" : "nu", "B38" : "de"})
root.right.right.left = Tree({"B39" : "sk", "B40" : "??", "B41" : "cs"})
root.right.right.right = Tree({"B42" : "??", "B43" : "qw", "B44" : "bi"})

# Typwnw tin lista me ola ta paths
print "========================================"
print "=                Paths                 ="
print "========================================"
print "\n"
paths = makeList(root)
print paths
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
    for i in range(45):
        block = "B" + str(i)
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
