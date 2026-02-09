# Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

# dengan adanya dua elemen yg sama, jadinya yg tercetak hanya 1 saja
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Bedanya sets dan yg lain adalah, ketika di print outputnya tdk berurutan
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


# Access Sets
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# Add sets items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# menggabungkan thisset dan mylist
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# remove item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#remove menggunakan pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Menggunakan clear untuk menghapus semua elemen
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets
#Union 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# bisa juga pake |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


