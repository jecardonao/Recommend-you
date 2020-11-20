class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        if(head ==None):
            self.head = head
        else:
            self.head = Node(head)
            
    def insertByHead(self,element):
        if self.head ==None:
            self.head = Node(element)
        else:
            newNode = Node(element)
            newNode.next = self.head
            self.head = newNode
            
    def toPrint(self):
        current = self.head
        while(current.next!=None):
            print(current.data,"->",end=" ")
            current = current.next
        print(current.data)
        
myList = LinkedList(7)
myList.insertByHead("Hola")
myList.insertByHead([1,2,3])
myList.insertByHead(2)
print("list")
myList.toPrint()
