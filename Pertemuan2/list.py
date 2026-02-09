# Membuat List Biasa
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0]) # ini digunakan untuk ngeprint atau akses elemen pertama di list

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Ini untuk print berapa aja item di list tsb

# Tipe data
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
print(list1)
# di python kita bisa anyimpan banyak tipe data di list

# mengubah item di list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# ini mengganti item dari indeks 1 sampai 2 dan 3 ga termasuk

# Insert Item 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # Guna insert item ini adalah utk memasukkan elemen ke dalam indeks

# Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #Pake extend utk menambahkan

# Remove List Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Untuk menghapus elemen kedua yaitu banana
print(thislist) 

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Loop list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) # utk mengurutkan angka dari yg terbesar 
print(thislist) 

# Copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)