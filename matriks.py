def print_matrix(matrix):
    for row in matrix:
        print("[", end=" ")
        for val in row:
            print(f"{val:.2f}", end=" ")
        print("]")

def input_matrix(rows, cols, name):
    matrix = []
    print(f"\n--- Masukkan elemen untuk Matriks {name} ---")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"Elemen baris {i+1}, kolom {j+1}: "))
            row.append(val)
        matrix.append(row)
    return matrix

def main():
    while True:
        print("\n" + "="*30)
        print(" PROGRAM OPERASI MATRIKS")
        print("="*30)
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Pembagian Matriks")
        print("5. Keluar")
        print("="*30)
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
            
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        if pilihan in ['1', '2', '4']:
            print("\nCatatan: Untuk operasi ini, ukuran kedua matriks harus sama.")
            rows = int(input("Masukkan jumlah baris matriks: "))
            cols = int(input("Masukkan jumlah kolom matriks: "))
            
            matriks_A = input_matrix(rows, cols, "A")
            matriks_B = input_matrix(rows, cols, "B")
            hasil = []
            
            if pilihan == '1':
                print("\nHasil Penjumlahan (A + B):")
                for i in range(rows):
                    row_hasil = []
                    for j in range(cols):
                        row_hasil.append(matriks_A[i][j] + matriks_B[i][j])
                    hasil.append(row_hasil)
                    
            elif pilihan == '2':
                print("\nHasil Pengurangan (A - B):")
                for i in range(rows):
                    row_hasil = []
                    for j in range(cols):
                        row_hasil.append(matriks_A[i][j] - matriks_B[i][j])
                    hasil.append(row_hasil)
                    
            elif pilihan == '4':
                print("\nHasil Pembagian (A / B) per elemen:")
                for i in range(rows):
                    row_hasil = []
                    for j in range(cols):
                        if matriks_B[i][j] == 0:
                            print("Error: Terdapat pembagian dengan angka 0. Operasi dibatalkan.")
                            hasil = None
                            break
                        row_hasil.append(matriks_A[i][j] / matriks_B[i][j])
                    if hasil is None:
                        break
                    hasil.append(row_hasil)
            if hasil is not None:
                print_matrix(hasil)

        
        elif pilihan == '3':
            print("\nCatatan: Untuk perkalian, kolom Matriks A harus sama dengan baris Matriks B.")
            rows_A = int(input("Masukkan jumlah baris Matriks A: "))
            cols_A = int(input("Masukkan jumlah kolom Matriks A (juga baris Matriks B): "))
            cols_B = int(input("Masukkan jumlah kolom Matriks B: "))
            
            matriks_A = input_matrix(rows_A, cols_A, "A")
            matriks_B = input_matrix(cols_A, cols_B, "B") 
    
            hasil = []
            for i in range(rows_A):
                row_hasil = []
                for j in range(cols_B):
                    
                    row_hasil.append(0) 
                hasil.append(row_hasil)
                
            print("\nHasil Perkalian (A x B):")
            for i in range(rows_A):
                for j in range(cols_B):
                    for k in range(cols_A):
                        hasil[i][j] += matriks_A[i][k] * matriks_B[k][j]
            print_matrix(hasil)
if __name__ == "__main__":
    main()
    