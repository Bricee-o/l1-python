#Un temps a le format suivant: (jour: int, heure: int, minute: int, seconde: int).
#C'est un tuple de 4 éléments. Par exemple (4, 3, 13, 20) correspond à 4 jours, 3 heures, 13 minutes et 20 secondes.
#Si on a une variable temps = (4, 3, 13, 20), pour accéder au premier élément on fait temps\[0\] ce qui donne 4,
#le nombre de jours.

#Temps en seconde = tes
#a,b,c,d="jours","heures","minutes","secondes"
#"Il y a",temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes" 
#1jour=86400sec, 1h=3600sec,1min = 60sec
def tes(temps):
    a,b,c,d=2,1,0,0
    temps=(a,b,c,d)
    js=(temps[0]*24)*3600 #ou temps[0]*86400
    hs=(temps[1])*3600
    ms=(temps[2])*60
    
    print("Il y a",js+hs+ms+temps[3],"secondes dans",temps[0],"jours",temps[1],"heures",temps[2],"minutes et",temps[3],"secondes")
tes(2)

#secondes en temps = scet
def scet(temps): #REFAIRE EN MIEUX
    a=temps
    print("Il y a",a//86400,"jours",a//3600,"heures",a//60,"minutes dans",a,"secondes")
scet(7295762)



