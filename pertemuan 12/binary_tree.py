#buat class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#preorder
def preorder(node):
    """Pre-Order: Root → Kiri → Kanan"""
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#inorder
def inorder(node):
    """In-Order: Kiri → Root → Kanan"""
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

#post order
def postorder(node):
    """Post-Order: Kiri → Kanan → Root"""
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# leaf node
def get_leaf_nodes(node):
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [node.data]

    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)


# membuat Tree 
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F


# Output 
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")

print("[INFO] Struktur berhasil dibuat.\n")

print("HASIL AUDIT:")

print()
print("1. Pre-Order  :", end=" ")
preorder(A)

print()
print("2. In-Order   :", end=" ")
inorder(A)

print()
print("3. Post-Order :", end=" ")
postorder(A)

print()
print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(get_leaf_nodes(A)))
print("======================================")
print("Audit Selesai!")


