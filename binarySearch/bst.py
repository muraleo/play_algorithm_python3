from collections import deque

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

    # DFS --- Depth First Search
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
    
    # BFS --- Breadth First Search, always need a queue
    def levelOrder(self, node):
        q = deque()
        q.append(self.root)

        while q.count != 0:
            temp = Node(q[-1])
            print(temp.value)

            if temp.left is not None:
                q.appendleft(temp.left)
            if temp.right is not None:
                q.appendleft(temp.right)

    # find the minimum node in this tree
    def minimum(self):
        if self.count == 0:
            return None
        else:
            return self.__minimum(self, self.__root)

    # find the maximum node in this tree
    def maximum(self):
        if self.count == 0:
            return None
        else:
            return self.__maximum(self, self.__root)


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

    def __minimum(self, node):
        if node.left is not None:
            return self.__minimum(node.left)
        return node

    def __maximum(self, node):
        if node.right is not None:
            return self.__maximum(node.right)
        return node