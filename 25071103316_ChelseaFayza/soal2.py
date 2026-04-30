stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

for x in stok_gadget:
    harga, merk, tipe = x

def filter_harga(data, min_harga, max_harga):
    if 6000000>= harga <=20000000 : 
        input (f"{harga}masukkan rentang harga:")
    else:
         print(f"{harga}Tidak ada gadget dalam rentang harga tersebut")

