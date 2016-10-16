'''
Binary Tree Implementation

'''

class Node(object):
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self,val,node):
        if val < node.val :
            if (node.left != None):
                self._add(val,node.left)
            else:
                node.left = Node(val)
        else:
            if (node.right != None):
                self._add(val,node.right)
            else:
                node.right = Node(val)

    def find(self,val):
        if (self.root != None):
            return self._find(val,self.root)
        else:
            return None

    def _find(self, val, node):
        if (val == node.val):
            return node
        elif (val < node.val and node.left != None):
            return self._find(val, node.left)
        elif (val > node.val and node.right != None):
            return self._find(val, node.right)

    def deleteTree(self):
        # Garbage collector handles this
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print (str(node.val) + ' ')
            self._printTree(node.right)





tree = BinaryTree()

tree.add(10)
tree.add(22)
tree.add(3)
tree.add(107)
tree.add(4)
tree.printTree()
print('')
print(tree.find(4).val)
