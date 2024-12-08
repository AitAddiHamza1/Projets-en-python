import cmath 

while True:
    a = int(input("entrez le nombre a ( a > 0) : "))
    if a > 0:
        break
    print("a doit etre superieur a 0. veuillez reessayer.")
b = int(input("entrez le nombre b : "))
c = int(input("entrez le nombre c : "))

D = (b*b) - (4*a*c)

if D > 0:
    d = cmath.sqrt(D)
    print(f"delta = {D}")
    x1 = (-b + d)/ (2*a)
    x2 = (-b - d)/ (2*a)
    rounded1 = round(x1,2)
    rounded2 = round(x2,2)
    print(f"les solutions de cette equation sont : {rounded1} et {rounded2} ")
elif D == 0:

    print(f"delta = {D}")
    x = -b / (2*a)
    rounded = round(x,2)
    print(f"la solution de lequation est : {rounded} ")
else:
    d = cmath.sqrt(D)
    # i = 1j
    print(f"delta = {D}")
    z1 = (-b + (d))/(2*a)
    z2 = (-b - (d))/(2*a)
    print(f"les solutions de cette equation sont : {z1:.2f} et {z2:.2f} ")
