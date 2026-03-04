# a
stok_barang = [15, 40, 30, 10, 25]
stok_barang[3]= 50

# b
stok_barang.append(5)

stok_barang.sort (reverse=True)
print(stok_barang)

# c
jumlah= sum(stok_barang)
print(jumlah)

# d
rata = jumlah/len (stok_barang)
print ("aman") if rata>20 else print ("waspada")
