class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print_ll_elements(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.get_next()

    def reverse_list(self, node, prev):
        #Reverse list using recursion
        
        if self.head is None:
            return

        if node.get_next() is None: 
            self.head = node          
            node.set_next(prev)
            return 
        
        prevNode = node 
        
        nextNode = node.get_next()
    
        node.set_next(prev)      

        self.reverse_list(nextNode, prevNode)
       

# 1 -> 2 -> 3 -> 4

newList = LinkedList()
newList.add_to_head(1)
newList.add_to_head(2)
newList.add_to_head(3)
newList.add_to_head(4)
newList.add_to_head(5)
# newList.print_ll_elements()
newList.reverse_list(newList.head, None)

