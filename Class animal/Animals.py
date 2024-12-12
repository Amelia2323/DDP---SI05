class Animals :
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def cetak(self):
        print(f"Hewan {self.nama} ini makan {self.makanan}, hewan ini juga hidup di {self.hidup}, dan berkembang biak dengan cara {self.berkembangbiak}.")

# c1 = Animals('Buaya', 'Daging', 'Bertelur')
# c1.cetak()

