#buat Node (Buku)
class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


# Binary Search Tree
class BST:
    def __init__(self):
        self.root = None

    # membuat fungsi insert utk menambahkan buku baru
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.id > current.id:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")
            else:
                self._insert_recursive(current.right, new_node)
    #pake insert recursive agar proses memasukkan data ke BST bisa “menyusuri” tree sampai ketemu posisi yang tepat secara otomatis.

    # fungsi searh
    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id:
            return current
        elif id_buku < current.id:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)

    # fungsi inorder traversal 
    # Menampilkan semua koleksi buku secara urut dari ID terkecil ke terbesar
    def traversal_inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self._inorder(node.right)

    # fungsi get min (menemukan buku dgn ID terkecil)
    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    # fungsi get max (menemukan buku dgn ID terbesar)
    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    # height (Menghitung total ketinggian (height) dari tree yang terbentuk)
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # biar sesuai contoh (height root = 0)
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1


# MAIN PROGRAM
print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst = BST()

# input data
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# memanggil fungsinya
bst.traversal_inorder()

# search
print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

# MIN & MAX
min_buku = bst.get_min()
max_buku = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

# HEIGHT
print(f"[INFO] Tinggi (Height) Tree: {bst.height()}")

print("=========================================")
print("Simulasi Selesai!")