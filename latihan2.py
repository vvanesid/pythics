total_hari = int(input("Masukkan total hari: "))
tahun = total_hari // 365
sisa_hari = total_hari % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30
print("\n---Hasil Konversi---")
print(f"Lama proyek dikerjakan adalah: {tahun} tahun, {bulan} bulan, dan {hari} hari.")