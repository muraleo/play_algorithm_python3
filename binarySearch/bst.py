class Node(object):
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST(object):
    def __init__(self):
        self.root = None
        self.count = 0
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.root == None

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    # check if this BST contains this node whose key is key, return True,
    # else return False
    def contain(self, key):
        temp = self.root
        
        while temp is not None:
            if temp.key == key:
                return True
            elif temp.key < key:
                temp = temp.right
            else:
                temp = temp.left
        return False

    # sometime search return:
    #   Node
    #   Value: key must exist
    def search(self, key):
        temp = self.root
        
        while temp is not None:
            if temp.key == key:
                return temp.value
            elif temp.key < key:
                temp = temp.right
            else:
                temp = temp.left
        return None

    def preOrder(self, node):
        temp = self.node
        while node is not None:
            print(node.value)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        temp = self.node
        while node is not None:
            self.preOrder(node.left)
            print(node.value)
            self.preOrder(node.right)

    def postOrder(self, node):
        temp = self.node
        while node is not None:
            self.preOrder(node.left)
            self.preOrder(node.right)
            print(node.value)

    # private
    def __insert(self, node, key, value):
        # Insert node(key, value) into a BST whose root is root
        # Return the root after inserting this node
        if node is None:
            self.count += 1
            return Node(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)
        return node