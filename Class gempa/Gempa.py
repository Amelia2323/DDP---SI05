class Gempa :
    # konstruktor inisialisasi atribut 
    def __init__ (self, lokasi, skala) :
        self.lokasi = lokasi
        self.skala = skala

    # Method penentu skala gempa
    def dampak(self):
        # statement 
        if self.skala < 2 :
            print("Tidak Berasa")
        elif 2 <=  self.skala <=4 :
            print("Gempa berdampak bangunan retak-retak")
        elif 4 <= self.skala <=6 :
            print("Gempa berdampak bangunan roboh") 
        elif self.skala > 6 :
            print("Gempa berdampak besar berpotensi tsunami")
        
        # menampilkan lokasi dan skala gempa
        print(f"Lokasi Gempa : {self.lokasi}")
        print(f"Skala Gempa : {self.skala}")
    