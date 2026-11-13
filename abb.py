from os import system
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

    def insert(self, new: Node):
        if self.root is None:
            self.root = new
        else:
            self.insertSubTree(self.root,new)
                    
    def insertSubTree(self, root: Node, new: Node):
        if new.key <= root.key:
            if root.left is None:
                root.left = new
            else:
                self.insertSubTree(root.left, new)
        else:
            if root.right is None:
                root.right = new
            else:
                self.insertSubTree(root.right, new)
                
    
    def remove(self, key: int):
        parent = None
        current = self.root

        # Buscar nodo
        while current and current.key != key:
            parent = current
            current = current.left if key <= current.key else current.right

        if current is None:
            return None

        removed = current

        # Buscar reemplazo si tiene dos hijos
        if current.left and current.right:
            successorParent = current
            successor = current.right

            while successor.left:
                successorParent = successor
                successor = successor.left

            if successorParent != current:
                successorParent.left = successor.right
                successor.right = current.right

            successor.left = current.left
            replacement = successor

        else:
            replacement = current.left or current.right

        # Actualizar enlace del padre o la raíz
        if parent is None:
            self.root = replacement
        elif parent.left == current:
            parent.left = replacement
        else:
            parent.right = replacement

        # Desvincular nodo eliminado
        removed.left = removed.right = None

        return removed
    
    def preorden(self):
        result = []
        self.preordenSubTree(self.root, result)
        print(result)

    def preordenSubTree(self, root: Node, result: list):
        if root is not None:
            result.append(root.key)
            self.preordenSubTree(root.left, result)
            self.preordenSubTree(root.right, result)
    
    def inorden(self):
        result = []
        self.inordenSubTree(self.root, result)
        print(result)

    def inordenSubTree(self, root: Node, result: list):
        if root is not None:
            self.inordenSubTree(root.left, result)
            result.append(root.key)
            self.inordenSubTree(root.right, result)
            
    def postorden(self):
        result = []
        self.postordenSubTree(self.root, result)
        print(result)

    def postordenSubTree(self, root: Node, result: list):
        if root is not None:
            self.postordenSubTree(root.left, result)
            self.postordenSubTree(root.right, result)
            result.append(root.key)
            
    # --- FUNCIÓN DE IMPRESIÓN VERTICAL / ROTADA ---
    def display(self):
        if self.root is None:
            print("El árbol está vacío.")
            return

        def _print_tree(node, level=0):
            if node is not None:
                # Imprime primero el subárbol derecho (queda arriba)
                _print_tree(node.right, level + 1)
                
                # Imprime el nodo actual con su indentación según la profundidad
                prefix = "Raíz: " if level == 0 else "│   " * level + "└── "
                print(f"{prefix}{node.key}")
                
                # Imprime el subárbol izquierdo (queda abajo)
                _print_tree(node.left, level + 1)

        print("--- Estructura del Árbol ABB (Vertical) ---")
        _print_tree(self.root)
        print("------------------------------------------")

    def search(self, key: int):
        return self.searchSubTree(self.root, key)

    def searchSubTree(self, root: Node, key: int):

        if root is None:
            return None

        if key == root.key:
            return root

        if key < root.key:
            return self.searchSubTree(root.left, key)

        return self.searchSubTree(root.right, key)


# --- PRUEBA ---
tree = ABB()
for val in [50, 80, 30, 90, 40, 70, 20]:
    tree.insert(Node(val))
tree.display()
tree.preorden()
tree.inorden()
tree.postorden()
buscado=tree.search(100)
buscado.print() if buscado else print("Nodo no encontrado!...")