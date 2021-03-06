# https://buptldy.github.io/2016/05/09/2016-05-09-Python%20BST/
class Node:
	def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
	def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent
    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt
    def delete(self, data): 
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
                if children_count == 0:
                    # if node has no children, just remove it
                    if parent:
                        if parent.left is node:
                            parent.left = None
                        else:
                            parent.right = None
                        del node
                    else:
                        self.data = None
                elif children_count == 1:
                      # if node has 1 child
                      # replace node with its child
                    if node.left:
                        n = node.left
                    else:
                        n = node.right
                    if parent:
                        if parent.left is node:
                            parent.left = n
                        else:
                            parent.right = n
                        del node
                    else:
                        self.left = n.left
                        self.right = n.right
                        self.data = n.data
                else:
                    # if node has 2 children
                    # find its successor
                    parent = node
                    successor = node.right
                    while successor.left:
                        parent = successor
                        successor = successor.left
                    # replace node data by its successor data
                    node.data = successor.data
                    # fix successor's parent's child
                    if parent.left == successor:
                        parent.left = successor.right
                    else:
                        parent.right = successor.right