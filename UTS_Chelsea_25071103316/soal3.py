#soal 3 
#oop
class Pengunjung:
    jumlah = 0 

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.jumlah += 1

        def get_id(self):
            return self.__id
    
        def get_nama(self):
            return self.__nama
    
        def get_kategori(self):
            return self.__kategori
    
        def tampilkan_info(self):
            print("ID      :", self.__id)
            print("Nama    :", self.__nama)
            print("Kategori:", self.__kategori)

        @staticmethod
        def hitung_pengunjung():
            return Pengunjung.jumlah
        
class PengunjungPrioritas:
    jumlah = 0 

    def__init__(self,id,nama,kategori,prioritas):
    super ().__init__(id, nama, kategori, prioritas)
        self.prioritas = prioritas 
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas:",self.prioritas)

    if self.prioritas == "mendesak":
            print("LAYANI SEGERA!")

#maaf bang dh buntu jd mau print2 aja
print("ID : M001")


