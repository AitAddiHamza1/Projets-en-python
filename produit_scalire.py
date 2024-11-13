T1 = []
T2 = []
T3 = []
N = int( input("entrer la taille de tableau : "))
i=1
if (N>0 and N<=100):
    for i in range(N):
        T1.append(int(input("entrer la valeur tableau 1 : ")))   
    for i in range(N):
        T2.append(int(input("entrer la valeur tableau 2 : "))) 
        
    Ps = 0
    for i in range(N):
       T3.append(T1[i] + T2[i])
       Ps += T1[i] * T2[i];
    print(f'Produit Scalaire= {Ps}') 
    print('Somme des vecteurs')
    for i in range(N):
       print(T3[i])
else:
    print('la taille du tableau doit etre entre 1 et 100')       
       