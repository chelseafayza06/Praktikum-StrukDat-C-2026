# Tuples
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Acces tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # untuk mengakses elemen terakhir makanya -1

# Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Update tuples dengan menambahkan suatu elemen baru
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange") 
thistuple = tuple(y) 

# Update tuples untuk meremove suatu elemen
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Unpack Tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join tuples
tuple1 = (1,2,3,4)
tuple2 = ("apel", "pisang", "ceri", "nenas")

tuple3 = tuple1 + tuple2 
print(tuple3)

#multiple tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)