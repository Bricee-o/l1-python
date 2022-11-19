#J'ai effacé prcq t'as même pas respecté les consignes.
#Correction exercices:
#1
import time 
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

    return temps[0]*24*3600+temps[1]*3600+temps[2]*60+temps[3]

temps =(24,234,3,1)
print(tempsEnSeconde(temps))
#24*3600 soit 86400
def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    j= seconde//86400
    h=(seconde%86400)//3600
    min=(seconde%(24*3600))%3600//60
    s=(seconde%(24*3600))%3600%60  #Revoir

    return(j,h,min,s) 
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def pluriel(mot,nb):#Revoir
    if nb>0:
        print("",nb,mot,end="")
    if nb>1:
        print("s",end="")
def afficheTemps(temps):
    
    pluriel("jour",temps[0])
    pluriel("heure",temps[1])
    pluriel("minute",temps[2])
    pluriel("seconde",temps[3])


afficheTemps((1,0,14,23)) 

def demandeTemps():
    
    j=-1
    h=-1
    m=-1
    s=-1
    while j<0:
        j=int(input("nb 1 "))#erreur jsp pourquoi
    while h<0 or h>=24:
        h=int(input("nb 2 "))
    while m<0 or m>=60:
        m=int(input("nb 3 "))
    while s<0 or s>=60:
        s=int(input("nb 4 "))
    return (j,h,m,s)

def sommeTemps(temps1,temps2):
    
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))
sommeTemps((2,3,4,25),(5,22,57,1))
afficheTemps(demandeTemps())

def proportionTemps(temps,proportion):
    
    return secondeEnTemps(int(tempsEnSeconde(temps)*proportion))

#afficheTemps(proportionTemps((2,0,36,0),0.2))
afficheTemps(proportionTemps(proportion=0.2,temps=(2,0,36,0)))#Revoir

def tempsendate(temps):
    a=1970+temps[0]//365
    j=1+temps[0]%365
    return(a,j,temps[1],temps[2],temps[3])

def affichedate(date:tuple=()):
    if len(date)==0:
        date=tempsendate(secondeEnTemps(int(time.time())))
    print("jour",date[1],"de l'année",date[0],"à",str(date[2])+":"+str(date[3])+":"+str(date[4]))

print(time.time)
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
affichedate(tempsendate(temps))
affichedate()

#année bisextile:
def estbisextile(annee):
    return annee%4==0 and (annee%100!=0 or annee%400==0)

def bisextile(jour):
    annee=1970
    while jour>=365:
        if estbisextile(annee):
            print("l'année"+str(annee)+"est bisextile")
        else:
            jour-=366
        anne+=1


bisextile(20000)

def nombreBisextile(jour):
    annee=1970
    i=0
    while jour>=365:
        if estbisextile(annee):
            print("l'année"+str(annee)+"est bisextile")
            i+=1
        else:
            jour-=366
        anne+=1
    return i

def temps(temps):
    jour,heures,minutes,secondes=temps
    jour=jour-nombreBisextile(jour)
    temps_modif=(jour,heures,minutes,secondes)
    return tempsendate(temps_modif)