#Based on the Python code or the C++ code provided in class as a starting point,
#implement the double linked list node delete function

class Node(object):
      
      def __init__(self, value):
          """initialise the class node and gives it attributes next and previous and value"""
          self.value = value
          self.next = None
          self.prev = None
 
class List(object):
      
      def __init__(self):
          """initalises the list with pointer head and tail"""
          self.head = None
          self.tail = None

      def insert(self, node, x):
          """inserts nodes into list"""
          if node != None:
              x.next = node.next
              node.next = x
              x.prev = node
              if x.next != None:
                  x.next.prev = x              
          if self.head == None:
              self.head = self.tail = x
              x.prev = x.next = None
          elif self.tail == node:
              self.tail = x

      def search(self, node):
            """function searches for the node starting form the head node"""
            #boolean initalises search
            foundnode = False
            currentnode = self.head
            
            while foundnode == False:
                  if currentnode.value == node:
                        return(currentnode)
                  elif currentnode.next != None:
                        currentnode = currentnode.next
                  else:
                        break


      def delete(self, node):
            """deletes nodes from the list"""
            if node == self.head:
                  node.next.prev = node.prev
            elif node == self.tail:
                  node.prev.next = node.next
            else:
                  #the prev node next pointer now points to the next node
                  node.prev.next = node.next # not if first node
                  #the next node now points to the prev npde pointer
                  node.next.prev = node.prev # not if last node

      def display(self):
          """outputs the list"""
          values = []
          node = self.head
          while node != None:
              values.append(str(node.value))
              node = node.next
          print("List: ",",".join(values))
         
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(5))
    l.insert(l.head,Node(9))
    l.insert(l.head,Node(10))
    l.insert(l.head,Node(11))
    l.insert(l.head,Node(1))
    l.insert(l.head,Node(7))
    nodedelete1 = l.search(6)
    nodedelete2 = l.search(11)
    l.delete(nodedelete1)
    l.delete(nodedelete2)
    l.display()
