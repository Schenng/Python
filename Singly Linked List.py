'''
Single Linked List
Each node has some cargo
Each node has a reference to the next node
'''

# Making the node
class Node(object):

    def __init__(self,data = None,next=None):
        self.data = data
        self.next_node = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_text):
        self.next_node = new_text

class LinkedList (object):
    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        new_node = (Node(data)) #create a new node for the list
        new_node.set_next(self.head) #set the next node to head (real head only on the first time)
        self.head = new_node #change the head to newly created node

    def size(self):
        current = self.head
        count = 0;
        while current:
            count += 1
            current = current.get_next()
        return count

    def search (self,data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if (current is None):
            raise ValueError("Data not found in list")
        return current

    def delete (self,data):
        current = self.head
        previous = None
        found = False

        while current and found == False:
            if (current.get_data() == data):
                found = True
            else:
                previous = current
                current = current.get_next();
        if current is None:
            raise ValueError("Data not found in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

''' Testing '''

list = LinkedList() # Creating List

size = list.size() # Getting Size
print(size) # 0

list.insert('Simon')
list.insert('Liz')
list.insert('Caroline')

print(list.size()) # 3

node = list.search('Liz') # Finds the node with the data 'Liz' and returns the node
print(node.data)

list.delete(('Liz')) # Delete the node with Liz as data

print(list.size()) # 2

