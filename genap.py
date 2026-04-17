def fibonacci_sequence(n):
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def main():
    while True:
        print("\nMenu Pilihan")
        print("1. Barisan Fibonacci")
        print("2. M x N")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0/1/2): ")

        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah suku Fibonacci: "))
                if jumlah <= 0:
                    print("Masukkan angka positif lebih besar dari 0.")
                    continue
            except ValueError:
                print("Harap masukkan angka bulat valid.")
                continue

            hasil = fibonacci_sequence(jumlah)
            print("Barisan Fibonacci:", " ".join(str(x) for x in hasil))

        elif pilihan == "2":
            try:
                m = int(input("Masukkan nilai M: "))
                n = int(input("Masukkan nilai N: "))
            except ValueError:
                print("Harap masukkan angka bulat valid untuk M dan N.")
                continue

            hasil = m * n
            print(f"Hasil {m} x {n} = {hasil}")

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
