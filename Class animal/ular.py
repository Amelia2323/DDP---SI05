from Animals import * 

class ular(Animals):
    def __init__(self, nama, makanan, hidup, berkembangbiak, warnaular, jenisular):
        super().__init__(nama, makanan, hidup, berkembangbiak) 
        self.warnaular = warnaular
        self.jenisular = jenisular
    
    def cetak_ular(self):
        super().cetak()
        print(f"Warna ular ini warna {self.warnaular}, dan jenis ular ini {self.jenisular}")

print("\n=======Cetak Ular=======")
print("\nUlar Kobra")

kobra = ular("Ular kobra", "daging", "darat", "bertelur", "abu-abu kehitaman atau coklat kehitaman", "berbisa")
kobra.cetak_ular()

print("\nUlar Anaconda")
anaconda = ular("Ular Anaconda", "hewan reptil", "air", "bertelur", "hijau kecoklatan", "tidak berbisa")
anaconda.cetak_ular()

print("\nUlar Sawah")
sawah = ular("Ular Sawah", "hewan kecil-kecil", "sawah atau tempat lembab", "bertelur", "hijau", "berbisa")
sawah.cetak_ular()

