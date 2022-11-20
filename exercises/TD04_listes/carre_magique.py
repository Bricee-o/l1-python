carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

def afficheCarre(carre):
    for i in carre:
        a=print(i[0:4])
    return a


def testLignesEgales(carre):
    a=carre
    somme,sommeb,sommec,sommed=0,0,0,0
    
    for i in a[0]:
        somme+=i
    for i in a[1]:
        sommeb+=i
    for i in a[2]:
        sommec+=i
    for i in a[3]:
        sommed+=i
    if somme==sommeb==sommec==sommed:
        return somme
    else:
        return -1


def testColonnesEgales(carre):
    s,sa,sb,sc=0,0,0,0
    a=len(carre)
    for i in carre:
        s+=i[0]
        sa+=i[1]
        sb+=i[2]
        sc+=i[3]
    if s==sa==sb==sc:
        return s
    else:
        return -1
    

def testDiagonalesEgales(carre):
    b=[]
    c=[]
    i,j,n=0,0,3
    sg,sd=[],[]
    for a in range(4):#gauche
        b.append(carre[i])
        sg.append(b[i][i])
        i+=1    
    #print(sg)
    dg,dd=0,0
    for g in sg:
        dg+=g
    for j in range(4):
        c.append(carre[j])
        sd.append(c[j][n])
        j+=1
        n-=1
    #print(sd)
    for h in sd:
        dd+=h
    if dg==dd:
        return print("La somme des valeurs de la diagonale gauche est égale à",dg,"et",dd,"pour celle de droite.")
    else:
        return -1


def estCarreMagique(carre):
    if testLignesEgales(carre) and testColonnesEgales(carre) !=-1:
        if testDiagonalesEgales(carre) !=-1:
            return True
    else:
        return False
  
print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    n,b=0,1
    for i in range(len(carre)):
        n+=1
    l=[]
    for i in carre:
        for j in i:
            print(j)
            l.append(j)
    l.sort()
    print("liste triée",l)
    print("valeur de n:",n)
    if n**2>l[-1]:
        return False
    elif l.count(b)==0:
            return False
    else:
        while b!=len(l):
            l.count(b)
            
            b+=1
            print("b",b)
        return True
        
    
    

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
