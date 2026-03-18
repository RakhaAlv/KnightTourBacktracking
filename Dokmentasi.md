# KnightTourBacktracking
Tugas Algoritma dan Pemrograman Backtracking - Knight's Tour Problem

Proyek ini adalah tugas implementasi algoritma Backtracking untuk menyelesaikan masalah Knight's Tour, di mana bidak kuda catur harus mengunjungi seluruh kotak pada papan tepat satu kali.

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal.
2. Jalankan `KnightTourBacktracking.py` untuk melihat metode Naive Backtracking.
3. Jalankan `KnightWarnsdorff.py` untuk melihat optimasi menggunakan Warnsdorff's Rule.

## Flowchart
1. BackTracking Knight's Tour.drawio.png
2. Knight's Tour Warnsdorff's.drawio.png

## Pseudocode

```text
FUNGSI utama():
    Inisialisasi papan_catur ukuran N x N dengan nilai KOSONG (-1)
    Tentukan posisi_awal kuda (x=0, y=0)
    Tandai papan_catur[0][0] = 0 (Langkah ke-0)
    
    JIKA fungsi_rekursi(0, 0, 1) bernilai BENAR:
        CETAK "Solusi Ditemukan"
    JIKA TIDAK:
        CETAK "Solusi Tidak Ditemukan"

FUNGSI fungsi_rekursi(x, y, langkah_saat_ini):
    JIKA langkah_saat_ini == Total Kotak (N * N):
        KEMBALIKAN Benar (Semua kotak sudah dikunjungi)

    UNTUK setiap arah dari 8 arah_gerakan_kuda:
        x_baru = x + arah_x
        y_baru = y + arah_y

        JIKA koordinat (x_baru, y_baru) VALID dan KOSONG:
            Tandai papan_catur[x_baru][y_baru] = langkah_saat_ini
            
            JIKA fungsi_rekursi(x_baru, y_baru, langkah_saat_ini + 1) bernilai BENAR:
                KEMBALIKAN Benar
            
            # PROSES BACKTRACKING
            Tandai papan_catur[x_baru][y_baru] = KOSONG (Hapus tanda)

    KEMBALIKAN Salah (Semua arah buntu)
