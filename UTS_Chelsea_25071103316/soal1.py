#soal 1
pengunjung_hari_ini = [{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False}, 
                       {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
                       {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False}, 
                       {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
                        {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False}, 
                        {"id": "M006", "nama": "Bagas","usia": 22, "kategori": "Hukum", "kembali": False},]

def tampilkan_pengunjung ():
    print("=== DATA PENGUNJUNG ===")
    print("NO | ID | NAMA | USIA | KATEGORI | STATUS KEMBALI")
    print("---+------+-------+------+----------+-------------")
    
    for i in range(len(pengunjung_hari_ini)): #looping
        n = pengunjung_hari_ini[i]  
        status = "sudah kembali" if n["kembalikan"] else "Belum kembali"
        print(f"{i+1} | {n['id']} | {n['nama']} | {n['usia']} | {n['penyakit']} | {status}")

def filter_belum_kembali(): 
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["sudah"]]

    for p in pengunjung_hari_ini: #loop
        if not p["kembalikan"]:
            belum.append(p["nama"]) #list comprehension

#ngesorting A-Z
    belum.sort()

    print("\n==== PENGUNJUNG BELUM MENGEMBALIKAN =====")
    for i in range(len(belum)):
        print(f"{i+1}. {belum[i]}")

    print("TOTAL YANG BELUM MENGEMBALIKAN:", len(belum))
    return belum 

tampilkan_pengunjung()
filter_belum_kembali()

"=================================================================="


    



    