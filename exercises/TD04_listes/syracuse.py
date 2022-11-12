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
print(syracuse(3))

def testeConjecture(n_max):
    a=syracuse(n_max)
    if a.count(1)!=1:
        return False
    else:
        return True  
print(testeConjecture(10000))

def tempsVol(n):
    b=syracuse(n)
    return "Le temps de vol de",n,"est",len(b[1:])

print(tempsVol(3)) 

def tempsVolListe(n_max):#FINIR
    a=syracuse(n_max)

    return "Le temps de vol est",(i for i in range(len(a[1:n_max])))
print(tempsVolListe(1000))

