def registrasi_gadget (merk, tipe, harga, sn) :
    if harga > 1000000:
      print ("harga ga valid")
      return None
    if len(sn) < 5:
       print ("serial number tdk valid")
       return None
    return {
       "merk" : merk,
       "tipe" : tipe,
       "harga": harga,
       "sn"   : sn,   
     }

for i in range (3):
    merk = input ("merk gadget:")
    tipe = input ("tipe gadget")
    harga = int(input("harga gadget"))
    sn = input ("serial number gadget")
    gadget = registrasi_gadget (merk, tipe, harga, sn)

print(registrasi_gadget)