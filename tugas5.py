#tugas nomor 1 membuat data kendaraan dengan program python

#buat variabel list berisi value
Data_Kendaraan = ['Nama Kendaraan', 'Jenis Kendaraan', 'CC Kendaraan', 'Warna Kendaraan', 'Roda Kendaraan']
print(Data_Kendaraan)

#menambah list (append)
#karna metode append hanya bisa menambah 1 value, jadi menambah valuenya 2 kali
Data_Kendaraan .append ('Harga Kendaraan')
print(Data_Kendaraan)

Data_Kendaraan .append('Tipe Kendaraan')
print(Data_Kendaraan)

#menyisipkan list (insert)
#indeks ke-2 atau urutan ke-3 setelah jenis kendaraan
Data_Kendaraan .insert (2, 'Merk Kendaraan')
print(Data_Kendaraan)

print('=======================================================soal no 1============================================================')


#tugas nomor 2 buat program match case untuk menghitung luas bangun datar 

pilih = int(input('''Selamat Datang di Aplikasi Menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga 
Masukkan Pilihan Anda : \n''')) 

match pilih : 
    case 1 : 
        print('Kamu Memilih 1 Untuk Menghitung Luas Persegi')
        sisi = int(input('Masukkan Sisi Persegi : '))
        luasPersegi = sisi*sisi
        print('Luas persegi yang sisinya', sisi, 'hasilnya adalah', luasPersegi)
    case 2 : 
        print('Kamu Memilih 2 Untuk Menghitung Luas Lingkaran')
        JariJari = int(input('Masukkan Sisi Lingkaran : '))
        luasLingkaran = 3.14 * JariJari * JariJari
        print('Luas lingkaran yang Jari-Jarinya', JariJari, 'hasilnya adalah', luasLingkaran)
    case 3 : 
        print('Kamu Memilih 3 Untuk Menghitung Luas Segitiga')
        alas = int(input('Masukkan Alas Segitiga : '))
        tinggi = int(input('Masukkan Tinggi Segitiga : '))
        luasSegitiga = 0.5 * alas * tinggi
        print('Luas Segitiga dengan alas', alas, 'dan tingginya', tinggi, 'hasilnya adalah', luasSegitiga )
    case _ :
        print('Anda Salah Pilih')

print('=============================================soal no 2====================================================')