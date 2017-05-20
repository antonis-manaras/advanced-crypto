#import random as r

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

# level 0 (root)
root = Tree("B1")
# level 1
root.left = Tree("??")
root.right = Tree("B3")
# level 2
root.left.left = Tree("B4")
root.left.right = Tree("B5")
root.right.left = Tree("??")
root.right.right = Tree("B7")
# level 3
root.left.left.left = Tree("B8")
root.left.left.right = Tree("??")
root.left.right.left = Tree("B10")
root.left.right.right = Tree("B11")
root.right.left.left = Tree("B12")
root.right.left.right = Tree("B13")
root.right.right.left = Tree("??")
root.right.right.right = Tree("B15")


# Typwnw tin lista me ola ta paths
print "========================================"
print "=                Paths                 ="
print "========================================"
print "\n\n"
paths = makeList(root)
print paths
print "\n\n"

# Dialegw px to 3o path gia na doylepsw
print "========================================"
print "=       Dialegw to path gia            ="
print "=        na to epeksergastw            ="
print "=       Estw to trito ([2])            ="
print "========================================"
print "\n\n"

selected_path = paths[2]
print selected_path
print "\n\n"

# Estw oti thelw to block sti thesi 3
print "========================================"
print "=       Estw oti thelw to              ="
print "=        4o stoixeio, stin             ="
print "=       thesi `selected_path[3]`       ="
print "========================================"
print "\n\n"

block_for_use = selected_path[3]
print " Block pros epeksergasia: " + str(block_for_use)
print "\n\n"
