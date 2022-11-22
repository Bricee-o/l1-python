#Regarder le site"lint code" pour entrainement

#Questions de cours:

#2)
##var1,var2=4.5,"2.0"
##print(var1+var2) # On ne peut pas additonner un type float et un type str

#3)
##print(5*3==15 or 4*2==9 and 18//6==2)#True car True or ((False and False)=False)
                                       #DONC C EST TRUE

#4)
##print(type(12=3*4))#erreur de redac c'est "==".

#5)
#réponse 1, on ne peut pas mettre de tiret du 6:"-", c'est un opérateur.
#Il n'est pas considéré comme un opérateur.

#Exercice 1 partie "if else elif"

#a=int(input("nb1"))
#b=int(input("nb2"))
#if a>b:
    #a,b=b,a
    #print(a,b)
#elif a==b:
    #print("Recommencer")
#else:
    #print(a,b)

#Exercice 2.

#import random

#a=random.randint(10,20)
#b=int(input("entrer un nb à 1 chiffre"))
#if b>9:
#    print("Ce n'est pas un nombre à 1 chiffre, recommencer.")
#if b>1 and a%b==0:
#    print("Diviseur")
#else:
#    print("Nope")

#Ex2 seconde version

#import random
#a=random.randint(10,20)
#b=int(input("entrer un nb à 1 chiffre"))
#if 9>b>1 and a%b==0:
#    print("Diviseur")
#else:
#   print("non")

#Ex 3

#var1=3
#var2=-3
#if var1>1 and var2>1 or var1<1 and var2 <1:
#    print("meme signe")
#    var1,var2=var2,var1
#    print(var1," ",var2)
#else:
#    var1,var2=var1**2,var1*var2
#    print(var1,var2)

#While for
#Ex2

#n=int(input("anniversaire"))
#cmpt=0
#for i in range(1,n+1):
#    cmpt+=120
#cmpt+=3*n
#print(cmpt)

#Ex3

#nb=int(input("nb"))
#for i in range(11):
#    print(nb-i)

#Question 1 ce sont des opérateurs, on peut les utiliser avec les obj de type float str int bool

#Ex2

a=int(input("nb1"))
b=int(input("nb2"))
s=input("chaine caractere")
if s =="addition":
    print(a+b)
elif s =="soustracton":
    print(a-b)
elif s=="multiplication":
    print(a*b)
elif s=="division":
    print(a/b)


#Ex3
# ON rentre un nb ensuite on défini n =0, on va prendre tous les nb de 0 à 20 par ex,
# on va mettre au carré chaque nb et s'arreter au premier nb élevé au carré qui sera supérieur à a,ce nb sera égal à n.
a=int(input("nb"))
n=0
for i in range(20):
    n+=1
    if n**2>a:
        print(n)
        break #Le mot break permet d'arreter l'execution d'une boucle et de passer à l'instruction suivante.