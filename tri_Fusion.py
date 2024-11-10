
T=[]

tab = int( input("entrer la taille de tableau : "))

for i in range(tab):
    T.append(int(input("entrer la valeur : ")))

def Fusion(T1, T2):
    if len(T1) == 0:
        return T2
    if len(T2) == 0:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]] + Fusion(T1[1:], T2)
    else:
        return [T2[0]] + Fusion(T1, T2[1:])

def trifusion(T):
    if len(T) <= 1:
        return T
    T1 = [T[i] for i in range(len(T)//2)]
    T2 = [T[i] for i in range(len(T)//2, len(T))]
    return Fusion(trifusion(T1), trifusion(T2))


print(trifusion(T))