#soal 2 
pengunjung_hari_ini = [{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False}, 
                       {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
                       {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False}, 
                       {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
                        {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False}, 
                        {"id": "M006", "nama": "Bagas","usia": 22, "kategori": "Hukum", "kembali": False},]


def info_perpustakaan():
    perpustakaan = (
        "perpustakaan kampus terpadu",
        "Jl. pendidikan No.5, Pekanbaru" ,
        "0761-54321"  
    )

    print("\nInfo Perpustakaan:")
    print("Nama   :", perpustakaan[0])
    print("Alamat :", perpustakaan[1])
    print("Telp   :", perpustakaan[2])

def rekap_kategori ():
    unik= {p["kategori"]for p in pengunjung_hari_ini}

    print("\nkategori buku unik: ", unik)
    print("Jumlah pengunjung: ", len(unik))

    rekap = {}
    for p in pengunjung_hari_ini: 
        buku = p["buku"]
        rekap[buku] = rekap.get(buku, 0) + 1, 

    print("\n rekap perbuku:")
    for k, v in rekap.items():
        print(f"{k} : {v} buku")

    #cari jumlah pengunjung terbanyak
    max_jumlah = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == max_jumlah]

    print("\npengunjung terbanyak:", ", ".join(terbanyak), f"({max_jumlah} pengunjung)")

    info_perpustakaan()
    rekap_kategori() #untuk mnaggil output