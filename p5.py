mahasiswa = [
    "Andi",
    "Budi",
    "Citra",
    "Dewi"
]

mata_kuliah = [
    "Matematika",
    "Biologi",
    "Kimia",
    "Fisika"
]

grades = [
    [85, 90, 78, 88],   
    [92, 81, 84, 79],   
    [88, 95, 90, 92],   
    [76, 74, 80, 83]    
]

def tampilkan_data():
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return

    print("\nData Mahasiswa dan Nilai Mata Kuliah:")
    for i, nama in enumerate(mahasiswa):
        nilai_str = ", ".join(f"{mata_kuliah[j]}: {grades[i][j]}" for j in range(len(mata_kuliah)))
        rata = sum(grades[i]) / len(grades[i]) if grades[i] else 0
        print(f"- {nama}: {nilai_str} | Rata-rata: {rata:.2f}")

def cari_mahasiswa_terbaik():
    if not mahasiswa:
        print("Tidak ada mahasiswa untuk dievaluasi.")
        return

    rata_mahasiswa = [sum(nilai) / len(nilai) for nilai in grades]
    index_terbaik = rata_mahasiswa.index(max(rata_mahasiswa))
    mahasiswa_terbaik = mahasiswa[index_terbaik]
    nilai_terbaik = rata_mahasiswa[index_terbaik]
    print(f"\nMahasiswa paling pintar: {mahasiswa_terbaik} dengan rata-rata {nilai_terbaik:.2f}")

def cari_mata_kuliah_terendah():
    if not grades or not mata_kuliah:
        print("Tidak ada data mata kuliah untuk dievaluasi.")
        return

    rata_mata_kuliah = []
    for j in range(len(mata_kuliah)):
        total = sum(grades[i][j] for i in range(len(grades)))
        rata_mata_kuliah.append(total / len(grades))

    index_terendah = rata_mata_kuliah.index(min(rata_mata_kuliah))
    mata_kuliah_terendah = mata_kuliah[index_terendah]
    nilai_mata_kuliah_terendah = rata_mata_kuliah[index_terendah]
    print(f"\nMata kuliah dengan rata-rata terendah: {mata_kuliah_terendah} ({nilai_mata_kuliah_terendah:.2f})")


def tambah_mahasiswa():
    nama_baru = input("Masukkan nama mahasiswa baru: ").strip()
    if not nama_baru:
        print("Nama tidak boleh kosong.")
        return

    nilai_baru = []
    print("Masukkan nilai untuk setiap mata kuliah:")
    for mata in mata_kuliah:
        while True:
            try:
                nilai = float(input(f"- {mata}: "))
                if nilai < 0 or nilai > 100:
                    print("Nilai harus antara 0 sampai 100.")
                    continue
                nilai_baru.append(nilai)
                break
            except ValueError:
                print("Masukkan angka yang valid.")

    mahasiswa.append(nama_baru)
    grades.append(nilai_baru)
    print(f"Mahasiswa {nama_baru} berhasil ditambahkan.")


def main():
    while True:
        print("\n=== MENU NILAI MAHASISWA ===")
        print("1. Tampilkan data mahasiswa")
        print("2. Tambah mahasiswa dan nilai")
        print("3. Cari mahasiswa paling pintar")
        print("4. Cari mata kuliah dengan rata-rata terendah")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa_terbaik()
        elif pilihan == "4":
            cari_mata_kuliah_terendah()
        elif pilihan == "5":
            print("Keluar dari program. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")


if __name__ == "__main__":
    main()
