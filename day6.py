#print middle element of the linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def add_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

            print("The middle element is: ",slow_ptr.data)

list1 = LinkedList()

list1.add_node(1)
list1.add_node(2)
list1.add_node(3)
list1.add_node(4)
list1.add_node(5)
list1.add_node(6)
list1.add_node(7)
list1.add_node(8)
list1.add_node(9)

list1.printMiddle()



