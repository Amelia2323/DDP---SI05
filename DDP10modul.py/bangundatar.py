import math

def persegi(sisi): 
    luasp = sisi*sisi
    kelilingp = sisi*sisi*sisi
    print(f"Luas persegi {sisi} * {sisi} = {luasp}")
    print(f"Keliling persegi {sisi} * {sisi} = {kelilingp}")

def persegipanjang (p, l) :
    luas = p*l
    keliling = 2*p + 2*l
    print(f"Luas persegi panjang {p} x {l} = {luas}")
    print(f"Keliling persegi panjang {p} x {l} = {keliling}")

def jajargenjang (t, a, b):
    luas = a*t
    keliling = 2*(a+b)
    print(f"Luas jajar genjang {a} x {t} = {luas}")
    print(f"keliling jajar genjang 2 x ({a} + {b}) = {keliling}")

def lingkaran (r):
    luas = 22/7*r**2
    keliling = 2*22/7*r
    print(f"Luas lingkaran 22/7 x {r}**2 = {luas}")
    print(f"Keliling lingkaran 2 x 22/7 x {r} = {keliling}")

def segitiga (alas, tinggi, sisiA, sisiB, sisiC) :
    luas = 1/2*alas*tinggi
    keliling = sisiA+sisiB+sisiC
    print(f"Luas segitiga 1/2 x {alas} x {tinggi} = {luas}")
    print(f"Keliling segitiga {sisiA} + {sisiB} + {sisiC} = {keliling}")
