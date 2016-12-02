#You either use an adjacency matrix or an adjacency list approach.
#Also, write a function to add a new node and a function to add an edge.
#Following that, implement the graph you have designed in the
#programming language of your choice.
#You may use your own linked list from previous labs, the STL LL,
#or use a simple fixed size array (10 elements would be fine)

class Node(object):

    def __init__(self, name):
        """initialises a node with a name and list of adjacent nodes as
           the nodes attributes"""
        self.name = name
        self.adjacent = []

    def addadjacent(self, adjacent):
        """joins 2 nodes together and sorts it"""
        if adjacent not in self.adjacent:
            self.adjacent.append(adjacent)
            self.adjacent.sort()

class Graph(object):

    def __init__(self):
        """initialises the graph and saves them in a list"""
        self.nodes = [] #list of nodes

    def finder(self, value):
        """looks at the index of node list and returns the index"""
        for i in range(len(self.nodes)):
            if self.nodes[i].name == value:
                return i

    def addedge(self, addleft, addright):
        """adds edge to 2 nodes in both directions"""
        #create a variable for an index of a node
        if self.finder(addleft) == None:
            self.addnode(Node(addleft))
        if self.finder(addright) == None:
            self.addnode(Node(addright))
        dexleft = self.finder(addleft)
        dexright = self.finder(addright)
        self.nodes[dexleft].addadjacent(addright)
        self.nodes[dexright].addadjacent(addleft)


    def addnode(self, node):
        """appends nodes to the nodes list"""
        self.nodes.append(node)

    def printgraph(self):
        """prints each nodes name and adjacent node to it"""
        for i in self.nodes:
            print(i.name, i.adjacent)

graph = Graph()

edges = ['AC', 'AB', 'BE', 'CF', 'CD', 'FI', 'DI', 'EH', 'HI', 'IG', 'JG', 'DB']
#edges = ['AB', 'AD', 'DC', 'BC']
for i in edges:
    graph.addedge(i[:1], i[1:])

graph.printgraph()

    
        
    
