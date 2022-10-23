#Regarder les sites"lint code et nint ou nit code je sais plus"

#Questions de cours:

#2)
##var1,var2=4.5,"2.0"
##print(var1+var2) # On ne peut pas additonner un type float et un type str

#3)
##print(5*3==15 or 4*2==9 and 18//6==2)#Revoir!

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

#Exercice 2. Ecrire un programme qui génère de manière aléatoire un nombre à deux chiffres puis
#demande à l'utilisateur de saisir un nombre à un chiffre. Le programme affche Diviseur si le
#nombre donné par l'utilisateur est plus grand que 1 et qu'il divise le nombre aléatoire. Proposer
#une solution en utilisant une seule instruction if.

import random

a=random.randint(0,9)
b=int(input("entrer un nb à 1 chiffre"))
if b>9:
    print("Ce n'est pas un nombre à 1 chiffre, recommencer.")
if b>1 and a%b==0:
    print("Diviseur")
else:
    print("Nope")

