def hello():
    print("Saya mahasiswa")

hello()


def hai():
    print("Prodi SI")
hai()

# --------mengubah print jadi cetak-----------
# Parameter atau Argumen

def cetak(kata):
    print(kata)

def biodata(nama = "ahmad", alamat = "bogor", umur = 19) :
    cetak("hello nama saya " + nama)
    cetak("alamat saya " + alamat)
    cetak("umur saya " + str(umur))

biodata("lia" , "depok" , 19) 
biodata("Lia", "Depok")
biodata()

# perhitungan
def perkalian(angka1, angka2):
    cetak(angka1+angka2)

perkalian(5,6)

def pangkat(angka1, angka2):
    cetak(angka1**angka2)
pangkat(2,2)

# -----------arbitary-----------
# manggil jika jumlahnya banyak
def function(*nama):
    print("Nama saya adalah " + nama[2])
      
function("Rizki", "Tri", "Amelia" )


#------------ return----------
# mengembalikan nilai
def fungsi2(x):
    return x**x

def fungsi3(y):
    return y**y

print(fungsi3(6))
