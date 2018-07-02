class BST(object):
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.root = None
        self.count = 0
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.root == None

    def insert(self, key, value):
        root = self.__insert(self.root, key, value)

    # private
    def __insert(self, root, key, value):
