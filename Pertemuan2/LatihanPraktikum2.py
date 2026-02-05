#Soal1
thislist = [15, 50, 75, 30, 25, 40, 100]

thislist.sort()
print(thislist)

rata_rata = sum(thislist) / len(thislist)
print(rata_rata)


#Soal 2
# Diberikan tuple barang
barang = ("B001", "Laptop Gaming", 15000000)

#Akses dan tampilkan harga barang dari tuple
harga_barang = barang[2]
print("Harga barang:", harga_barang)

#Menggunakan teknik unpacking
kode, nama, harga = barang

print("Kode barang:", kode)
print("Nama barang:", nama)
print("Harga barang:", harga)


#Soal 3
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL","NodeJS"}

irisan = tim_frontend.intersection(tim_backend)
backend_only = tim_backend.difference(tim_frontend)
union_skill = tim_frontend | tim_backend

print(f"Irisan: {irisan}")
print(f"Skill Tim Backend: {backend_only}")
print(f"Skill Gabungan: {union_skill}")

#Soal4
nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

nilai_siswa["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90
}

print("Nilai Akhir Siswa > 80")
for x in nilai_siswa.values():
    final = (x["tugas"] * 0.2) + (x["uts"] * 0.3) + (x["uas"] * 0.5)
    if (final > 80):
        print(f"{x["nama"]}: {final}")
