
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes) + " -> None")
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
ll = LinkedList()
ll.append(15)
ll.append(30)
ll.append(23)
ll.append(45)
ll.append(34)
ll.display() 
ll.reverse()
ll.display() 