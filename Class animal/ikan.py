from Animals import *

class Ikan(Animals):
    def __init__(self, nama, makanan, hidup, berkembangbiak, warnaikan, jenisikan):
        super().__init__(nama, makanan, hidup, berkembangbiak) 
        self.warnaikan = warnaikan
        self.jenisikan = jenisikan
    
    def cetak_ikan(self):
        super().cetak()
        print(f"Warna ikan ini adalah {self.warnaikan}, dan ikan ini jenisnya ikan {self.jenisikan}.")

print("\n=======Cetak Ikan=======")
print("\nIkan Nemo")
nemo = Ikan("Ikan Nemo", "plankton", "air", "bertelur", "orange", "air laut")
nemo.cetak_ikan()

print("\nIkan Koi")
koi = Ikan("Ikan Koi", "pelet atau cacing sutra", "air", "bertelur", "orange dan putih", "air tawar")
koi.cetak_ikan()

print("\nIkan Hiu")
hiu = Ikan("Ikan Hiu", "daging", "air", "bertelur", "coklat atau keabu-abuan", "air laut")
hiu.cetak_ikan()
