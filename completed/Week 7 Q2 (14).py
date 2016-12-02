#Implement BFS and DFS traversals for the above graph.
#Save the nodes traversed in sequence to a text file. 

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

    def breadthfirst(self, node):
        queue = []
        visited = []
        queue.append(node)
        while len(queue):
          currentnode = queue.pop(0)
          print(type(currentnode))
          if currentnode not in visited:
            visited.append(currentnode)
            for i in currentnode.adjacent:
                print(type(i))
                queue.append(i)
        print(visited)

    def depthfirst(self, node):
        visited = []
        stack = [node]
        while len(stack):
          currentnode = stack.pop(0)
          currentnode.reverse()
          if currentnode not in visited:
            visited.append(currentnode)
            for i in temp:
              stack = [self.nodes[i]] + stack
        print(visited)





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
#graph.breadthfirst(graph.nodes[0])
#graph.depthfirst(graph.nodes[0])

        
    
