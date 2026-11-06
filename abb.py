#Definción  de las estructuras de datos

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None 

    def print(self):
        print(self.key)

class ABB:
    def __init__(self):
        self.root = None

    def insertSubTree(self,root:Node, new:Node):
        if new.key <= root.key:
            if root.left is None:
                root.left = new
            else: 
                self.insertSubTree(root.left,new)

        else: 
            if root.right is None:
                root.right = new
            else:
                self.insertSubTree(root.right,new)

tree = ABB()
node = Node(50)
tree.insert(node)
node = Node(80)
tree.insert(node)
node = Node(30)
tree.insert(node)
node = Node(90)
tree.insert(node)
node = Node(40)
tree.insert(node)
node = Node(70)
tree.insert(node)
node = Node(20)
tree.insert(node) 