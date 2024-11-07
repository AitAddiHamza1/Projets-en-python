T=[]

tab = int( input("entrer la taille de tableau : "))

for i in range(tab):
    T.append(int(input("entrer la valeur : ")))

def trirapide(T):
    if len(T) == 0:
        return T
    else:
        n = len(T)
        T1 = []
        T2 = []
        for i in range(1 , n):
            if T[i] <= T[0]:
                T1.append(T[i])
            else:
                T2.append(T[i])
        T = trirapide(T1) + [T[0]] + trirapide(T2)
        return T        
print(trirapide(T))