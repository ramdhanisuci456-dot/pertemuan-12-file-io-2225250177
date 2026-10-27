# Pertemuan 12 — File Input-Output dan Error Handling

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** Pendidikan Matematika FKIP Untirta  
**Kelas:** 3B  
**NIM:** 2225250177

## Deskripsi
Proyek ini berisi latihan dan tugas Python tentang membaca file, menulis file, menambahkan data, memproses baris, serta menangani kesalahan saat pemrosesan file.

## Struktur Folder
- `data/`: Menyimpan file teks sumber data dan hasil rekap.
- `latihan/`: Berisi enam program latihan.
- `tugas/`: Berisi program rekap nilai mahasiswa.

## Format Data
File `data/nilai.txt` menggunakan format `NIM,nilai`, dengan satu data pada setiap baris.

Contoh:
```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

## Cara Menjalankan
Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek:

```bash
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py
```

## Penanganan Error
Program mempelajari penanganan `FileNotFoundError` ketika file tidak ditemukan dan `ValueError` ketika data tidak dapat dikonversi menjadi angka.

Pada tugas rekap nilai, data yang tidak valid dilewati agar pemrosesan dapat dilanjutkan.

## Pengujian
Pengujian dilakukan menggunakan data nilai yang valid, data dengan nilai bukan angka, dan file yang tidak ditemukan.

## Refleksi
Melalui tugas ini, saya mempelajari cara membaca dan menulis file menggunakan Python, mengolah data dari file teks, serta menangani kesalahan agar program dapat berjalan dengan lebih baik.