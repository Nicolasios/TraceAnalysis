from HelpClass.Node import Node


class AVTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def LRHeightDiff(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def NodeBalance(self, node):
        if not node:
            return True
        diff = self.LRHeightDiff(node)
        if abs(diff) > 1:
            return False
        return self.NodeBalance(node.left) and self.NodeBalance(node.right)

    def RootBalance(self):
        return self.NodeBalance(self.root)

    def InOrderTravese(self, node, keys):
        if not node:
            return
        self.InOrderTravese(node.left, keys)
        keys.append(node.key)
        self.InOrderTravese(node.right, keys)

    def isBst(self):
        keys = []
        self.InOrderTravese(self.root, keys)
        for i in range(1, len(keys)):
            if keys[i-1] > keys[i]:
                return False
        return True

    def getNode(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self.getNode(node.left, key)
        else:
            return self.getNode(node.right, key)

    def LeftRotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = max(self.getHeight(y.left),
                       self.getHeight(y.right))+1
        x.height = max(self.getHeight(x.left),
                       self.getHeight(x.right))+1
        return x

    def RightRotate(self, y):
        x = y.right
        y.right = x.left
        x.left = y
        y.height = max(self.getHeight(y.left),
                       self.getHeight(y.right))+1
        x.height = max(self.getHeight(x.left),
                       self.getHeight(x.right))+1
        return x

    def add(self, node, key, value):
        if not node:
            self.size += 1
            return Node(key, value)
        if node.key == key:
            return node
        if node.key > key:
            node.left = self.add(node.left, key, value)
        else:
            node.right = self.add(node.right, key, value)
        node.height = max(self.getHeight(node.right),
                          self.getHeight(node.left))
        diff = self.LRHeightDiff(node)
        if diff > 1 and self.LRHeightDiff(node.left) >= 0:
            return self.RightRotate(node)
        if diff < -1 and self.LRHeightDiff(node.right) <= 0:
            return self.LeftRotate(node)
        if diff > 1 and self.LRHeightDiff(node.left) <= 0:
            node.left = self.LeftRotate(node.left)
            return self.RightRotate(node)
        if diff < -1 and self.LRHeightDiff(node.right) > 0:
            node.right = self.RightRotate(node.right)
            return self.LeftRotate(node)
        return node

    def addToTree(self，key, value):
        self.root = self.add(self.root, key, value)

    def minimum(self, node):
        if not node.left:
            return node
         return self.minmum(node.left)

    def remove(self, node, key):
        if not node:
            return
        if node.key > key:
            node.left = self.remove(node.left, key)
            ret_node = node
        elif node.key < key:
            node.right = self.remove(node.right, key)
            ret_node = node
        else:
            if not node.left:
                right_node = node.right
                node.right = None
                self.size -= 1
                ret_node = right_node
            elif not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node
            else:
                successor = self.minimum(node.right)
                successor.right = self.remove(node.right, successor.key)
                successsor.left = node.left
                node.left = node.right = None
                ret_node = successor
        if not ret_node:
            return
        ret_node.height = max(self.getHeight(ret_node.left),
                              self.getHeight(ret_node.right))
        diff = self.LRHeightDiff(ret_node)
        if diff > 1 and self.LRHeightDiff(ret_node.left) >= 0:
            return self.RightRotate(ret_node)
        if diff < -1 and self.LRHeightDiff(ret_node.right) <= 0:
            return self.LeftRotate(ret_node)
        if diff > 1 and self.LRHeightDiff(ret_node.left) < 0:
            ret_node.left = self.LeftRotate(ret_node.left)
            return self.RightRotate(ret_node)
        if diff < -1 and self.LRHeightDiff(ret_node.right) > 0:
            ret_node.right = self.RightRotate(ret_node.right)
            return self.LeftRotate(ret_node)
        return ret_node

    def removeFromTree(self,key):
        node = self.getNode(self.root,key)
        if node:
            self.root = self.remove(self.root,key)

    def updateWeight(self,node):
        if not node:
            return 0
        else:
            if node.left:
                node.weight += updateWeight(node.left)
            if node.right:
                node.weight += updateWeight(node.right)
