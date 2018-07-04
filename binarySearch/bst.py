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

    # remove min key node
    def removeMin(self):
        if root is None:
            return None

        __removeMin(self, self.root)

    # remove max key node
    def removeMax(self):
        if root is None:
            return None
        
        __removeMax(self, self.root)

    # remove node with key
    def remove(self, key):
        return self.__remove(self, key, self.root)



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

    def __removeMin(self, node):
        if node.left == None:
            return node.right # two situations: right is null or a tree
        else:
            node.left = self.__removeMin(node.left)
            return node.left

    def __removeMax(self, node):
        if node.right == None:
            return node.left
        else:
            node.right = self.__removeMax(node.right)
            return node.right

    def __remove(self, key, node):
        if node is None:
            return None #this node doesn't exist

        if key < node.key:
            node.left = self.__remove(self, key, node.left)
            self.count -= 1
            return node

        elif key > node.key:
            node.right = self.__remove(self. key, node.right)
            self.count -= 1
            return node
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.minimum(node.right)
                
                temp.left = node.left
                temp.right = self._removeMin(self, node.right)
                self.count -= 1
                return temp