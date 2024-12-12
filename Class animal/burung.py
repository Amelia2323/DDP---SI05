from Animals import * 

class Burung(Animals):
    def __init__(self, nama, makanan, hidup, berkembangbiak, jenisbulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembangbiak) 
        self.jenisbulu = jenisbulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f"Burung ini berbulu {self.jenisbulu}, dan hewan ini berbunyi {self.bunyi}")

print("\n=======Cetak Burung=======")
print("\nBurung Beo")
beo = Burung("Burung Beo", "Biji-bijian", "Udara", "Bertelur", "blue and orange", "meniru suara")
beo.cetak_burung()

print("\nBurung Kakak tua")
kakaktua = Burung("Burung Kakak Tua", "biji-bijian", "udara", "bertelur", "putih", "suara seperti peluit atau suara whistle")
kakaktua.cetak_burung()

print("\nBurung Hantu")
hantu = Burung("Burung Hantu", "hewan-hewan kecil", "udara dan darat", "bertelur", "coklat dan abu-abu", "Hoo-hoo atau Who-who")
hantu.cetak_burung()