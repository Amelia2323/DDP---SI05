import math

def kubus(sisi):
    volume = sisi**3
    lpermukaan = 6*sisi**2
    print(f"Volume kubus {sisi}**3 = {volume}")
    print(f"Luas Permukaan kubus 6x {sisi}**2 = {lpermukaan}")

def balok (p, l, t):
    volume = p*l*t
    lpermukaan = 2*((p*l) + (p*t) + (l*t))
    print(f"Volume balok {p} x {l} x {t} = {volume}")
    print(f"Luas Permukaan balok 2x(({p}x{l}) + ({p}x{t}) + ({l}x{t})) = {lpermukaan}")

def kerucut (s, r, t) :
    volume = 1/3*r**2*t
    lpermukaan = 22/7*r*(s+r)
    print(f"Volume kerucut 1/3 x {r}**2x {t} = {volume}")
    print(f"Luas permukaan kerucut 22/7 x {r} x ({s}+{r}) = {lpermukaan}")

def bola (r) :
    volume = 4/3*22/7*r**3
    lpermukaan = 4*22/7*r**2
    print(f"Volume bola 4/3 x 22/7 x {r}**3 = {volume}")
    print(f"Luas permukaan bola 4 x 22/7 x {r}**2 = {lpermukaan}")

def tabung(r,t) :
    volume = 22/7*r**2*t
    lpermukaan = 2*22/7*r + (r+t) 
    print(f"Volume tabung 22/7 x {r}**2 x {t} = {volume}")
    print(f"Luas permukaan tabung 2 x 22/7 x {r} + ({r} + {t}) = {lpermukaan}")