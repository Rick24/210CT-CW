#Implement Dijkstra’s algorithm for a weighted graph data structure
#(you have to update your previous data structure so that it can deal
#with weights)

class Node(object):

    def __init__(self, name):
        """initialises a node with a name and list of adjacent nodes as
           the nodes attributes"""
        self.name = name
        self.adjacent = []

    def addadjacent(self, adjacent, weight):
        """joins 2 nodes together and sorts it"""
        if adjacent not in self.adjacent:
            self.adjacent.append((adjacent, weight))
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

    def addedge(self, addleft, addright, weight):
        """adds edge to 2 nodes in both directions"""
        #create a variable for an index of a node
        if self.finder(addleft) == None:
            self.addnode(Node(addleft))
        if self.finder(addright) == None:
            self.addnode(Node(addright))
        dexleft = self.finder(addleft)
        dexright = self.finder(addright)
        #adds edges to the nodes in both directions
        self.nodes[dexleft].addadjacent(addright, weight)
        self.nodes[dexright].addadjacent(addleft, weight)

    def breadthfirst(self, node):
        """attempt"""
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
        """attepmt"""
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

    def dijkstras(self, start, end):
        """serches the shortest path between 2 given nodes being a start and end node"""
        path = []
        history = []
        #loop which will set the weight to infinity
        #when a node has been checked it will be added to history list and
        #the weight will be re assigned to the actual weight
        #as the loop continues the history will save the nodes and values
        

    def addnode(self, node):
        """appends nodes to the nodes list"""
        self.nodes.append(node)

    def printgraph(self):
        """prints each nodes name and adjacent node to it"""
        for i in self.nodes:
            print(i.name, i.adjacent)

graph = Graph()

edges = ['AC', 'AB', 'BE', 'CF', 'CD', 'FI', 'DI', 'EH', 'HI', 'IG', 'JG', 'DB']
weights = ['AC2', 'AB3', 'BE7', 'CF8', 'CD10', 'FI1', 'DI8', 'EH7', 'HI2', 'IG3', 'JG6', 'DB1']


#edges = ['AB', 'AD', 'DC', 'BC']
#for i in edges:
#   graph.addedge(i[:1], i[1:])

for i in weights:
    graph.addedge(i[0],i[1],i[2])

graph.printgraph()
#graph.breadthfirst(graph.nodes[0])
#graph.depthfirst(graph.nodes[0])
#start = graph.nodes['A']
#end = graph.nodes['G']
#print(graph.dijkstras(start, end))
        
    
