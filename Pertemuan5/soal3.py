ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print(ukm_coding)

coding_only = ukm_coding.difference(ukm_robotik)
print ("mahasiswa daftar di ukm coding:", coding_only)

salah_satu = ukm_coding.union(ukm_robotik) 
print ("daftar mahasiswa unik:", salah_satu)

# cek andi 
print ("Andi" in ukm_robotik)


