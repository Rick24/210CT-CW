#Implement TREE_SORT algorithm in a language of your choice,
#but make sure that the INORDER function is implemented iteratively. 

class BinTreeNode(object):

    def __init__(self, value):
        """initialisation of nodes and attributes"""
        self.value=value
        self.left=None
        self.right=None

def tree_insert( tree, item):
    """inserts a node into a tree"""
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    """travseres the tree postorder"""
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  
#original recursive function
#def in_order(tree):
#    if(tree.left!=None):
#        in_order(tree.left)
#    print(tree.value)
#    if(tree.right!=None):
#        in_order(tree.right)

#iteratively
def in_order(tree):
    """traverses the graph in ascending order and prints it"""
    stack = []
    trv = False #boolean value represtents if the tree is traversed
    while(trv == False):
        if tree != None:
            stack.append(tree)
            tree = tree.left
        else:
            if (len(stack) > 0):
                tree = stack.pop()
                print(tree.value)
                tree = tree.right
            else:
                trv = True

def tree_sort(list1):
    """makes a tree for given values and traverses them with in_order function"""
    #makes first node the root of the tree
    t = tree_insert(None, list1[0])
    for i in list1:
        #for element in the list insert into the tree
        tree_insert(t, i)
        #orders the tree once created
    in_order(t)

if __name__ == '__main__':
#initialises function calls
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  #postorder(t)
  in_order(t)
  list1 = [2, 5, 8, 1, 5, 9, 7, 0]
  tree_sort(list1)

