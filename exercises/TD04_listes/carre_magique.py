carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

def afficheCarre(carre):
    a=print("",carre[0],"\n",carre[1],"\n",carre[2],"\n",carre[3])
    return a

afficheCarre(carre_mag)  
afficheCarre(carre_pas_mag)

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

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    b=[a[0][0],a[1][0]]
    a=carre
    s,sa,sb,sc=0,0,0,0
    for i in a:
        for j in i:
            print(j)
    
        return j
    
print(testColonnesEgales(carre_mag))













