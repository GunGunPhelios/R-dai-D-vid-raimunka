ásványvíz= 150
gyümölcslé=450

itóka= input("Milyen italt kér?: ").lower()

űrmérték= int(input("Mennyit kér?: "))

vegosszeg=0
if itóka == "ásványvíz":
    vegosszeg = ásványvíz*űrmérték 
    print(f"A választott italod: ásványvíz, űrmérték: {űrmérték} liter.")
elif itóka == "gyümölcslé":
    vegosszeg= gyümölcslé*űrmérték
    print(f"A választott italod: gyümölcslé, űrmérték:{űrmérték} liter.")
else: 
    print("Ismeretlen italtípus!")
    exit()

print(f"A fizetendő összeg: {vegosszeg} Ft.")
