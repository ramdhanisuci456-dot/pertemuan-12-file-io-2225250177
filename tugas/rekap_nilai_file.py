# Tugas Pertemuan 12: Rekap Nilai Mahasiswa
# Algoritma dan Pemrograman - Pendidikan Matematika
# Kelas 3B

def baca_data(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data_nilai.append((nim, nilai))
                except ValueError:
                    print(f"Data tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print("File nilai tidak ditemukan.")

    return data_nilai


def tulis_rekap(nama_file, data_nilai):
    with open(nama_file, "w", encoding="utf-8") as file:
        if not data_nilai:
            file.write("Tidak ada data nilai yang valid.\n")
            return

        jumlah = len(data_nilai)
        total = sum(nilai for nim, nilai in data_nilai)
        rata_rata = total / jumlah
        nilai_tertinggi = max(nilai for nim, nilai in data_nilai)
        nilai_terendah = min(nilai for nim, nilai in data_nilai)
        jumlah_lulus = sum(1 for nim, nilai in data_nilai if nilai >= 60)

        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")
        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai tertinggi: {nilai_tertinggi}\n")
        file.write(f"Nilai terendah: {nilai_terendah}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")


def main():
    data_nilai = baca_data("data/nilai.txt")
    tulis_rekap("data/hasil_rekap.txt", data_nilai)

    print("Rekap nilai berhasil dibuat.")
    print("Silakan periksa file data/hasil_rekap.txt.")


if __name__ == "__main__":
    main()