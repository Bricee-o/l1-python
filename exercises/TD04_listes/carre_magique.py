#Revoir ces exos pour la kholle.

carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[]

#1ere solution
for i in range(len(carre_mag)):
    carre_pas_mag.append([])
    for j in range(len(carre_mag[i])):
        carre_pas_mag[i].append(carre_mag[i][j])
 
#2eme solution for l in carre_mag:
    #carre_pas_mag.append(l.copy())
    
#3eme solution avec liste en compréhension: carre_pas_mag=[l[:] for l in carre_mag]
carre_pas_mag[3][2]=7
    
def afficheCarre(carre):
    for i in carre:
        print(i[0:])
    return 


def testLignesEgales(carre:list)->int:#Autre notation
#1ere Solution:
    somme=sum(carre[0])
    for l in carre:
        if sum(l)!=somme:
            return -1
    return somme

    a=carre#Programme pas généralisé donc faux.
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
    c1=[lignes[0] for lignes in carre]
    somme=sum(c1)
    for j in range(1,len(carre)):
        colonne=[lignes[j] for lignes in carre]
        if sum(colonne)!=somme:
            return -1
    return somme
#Faux car non generalisé.    
    s,sa,sb,sc=0,0,0,0
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
    taille=len(carre)
    diago1=[carre[i][i] for i in range(taille)]
    diago2=[carre[i][taille-i-1] for i in range(taille)]
    somme=sum(diago1)
    if sum(diago2)!=somme:
        return -1
    else:
        return somme
    k=0
    for i in range(len(carre)):
        k+=1
    b=[]
    c=[]
    i,j,=0,0
    n=(len(carre)-1)
    sg,sd=[],[]
    for a in range(k):#gauche
        b.append(carre[i])
        sg.append(b[i][i])
        i+=1    
    #print(sg)
    dg,dd=0,0
    for g in sg:
        dg+=g
    for j in range(k):
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
    return testLignesEgales(carre)==testColonnesEgales(carre)and testLignesEgales(carre)==testDiagonalesEgales(carre)!=-1
    #Ca marche aussi !
    if testLignesEgales(carre) and testColonnesEgales(carre) !=-1:
        if testDiagonalesEgales(carre) !=-1:
            return True
    else:
        return False
 

def estNormal(carre):
    #autre solution:
    liste=[]
    for l in carre:
        liste.extend(l)
    taille=len(carre)
    for entier in range(1,taille*taille+1):
        if entier not in liste:
            return False
    return True
    
    #Cette solution marche aussi.
    n,b=0,1
    for i in range(len(carre)):
        n+=1
    l=[]
    for i in carre:
        for j in i:     
            l.append(j)
    l.sort()
    if n**2>l[-1]:
        return False
    else:
        while b!=len(l):
            if l.count(b)!=1:
                return False
            else:
                b+=1 
        return True

print(afficheCarre(carre_mag))
print(afficheCarre(carre_pas_mag))

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

print(estNormal(carre_pas_mag))
print(estNormal(carre_mag))
        

 
    



