def syracuse(n):
    a=[]
    a.append(n)
    while a[-1]!=1:
        if (n**2)%2==0:
            a.append(n//2)
            n=n*(1/2)
        elif(n**2)%2!=0:
            a.append(n*3+1)
            n=n*3+1
    return a

#Autre version
#def syracuse(n):
#    L=[n]
#    while n!=1:
#       if n%2==0:
#           n//2
#       else:
#           n=(n*3+1)
#       L.append(n)

print(syracuse(3))

def testeConjecture(n_max):
    a=syracuse(n_max)
    if a.count(1)!=1:
        return False
    else:
        return True  
print(testeConjecture(10000))
#Autre version
#for i in range(i,n_max+1):
#       syracuse(i)
#    return True

def tempsVol(n):
    b=syracuse(n)
    return "Le temps de vol de",n,"est",len(b[1:])

print(tempsVol(3)) 

def tempsVolListe(n_max):#FINIR
    a=syracuse(n_max)

    return "Le temps de vol est",(i for i in range(len(a[1:n_max])))
print(tempsVolListe(1000))

#Correction temps voliste:
def tempsVolListe(n_max):
    return [tempsVol(i) for i in range(i,n_max+1)]

L=tempsVolListe(1000)
t_max=max(L)
print(("l'entier",(index(t_max))+1),"a le plus grand tps",t_max)#comprend pas ????

L_alt=alt_max_liste(10000)
b=max(L_alt)
print("l'entier etc...")

