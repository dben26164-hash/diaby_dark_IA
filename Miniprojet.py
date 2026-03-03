# Mini projet 
#fiche d'inscription à un jeu video 

print("SMART GAME")
print("Bienvenue dans  veiller SMART GAME vous inscrire ")
nom_utilisateur = input("Nom d'utlilisateur:" )
email = input("Adress email:" )
age = input ("Age : ")
age = int(age)
num = input("Numéro mobile :")
num= int(num)
num_utilisateur =(num/age/1000)
num_utilisateur =int(num_utilisateur)

print("Salut ",nom_utilisateur, "vous êtes inscrit avec sucsès votre code de validation est ",num_utilisateur)
confirmation = input("Veiller confirmer votre num d'utilisateur : ")
confirmation =int(confirmation)
if num_utilisateur == confirmation :
    print ("Vous pouvez commencer l'aventure ")
else:    
    print("Verification echouer veiller rééseiler")
#___________________________________________________________________________________________________________________________________
#2) Explication du jeu 
print("SMART GAME")
print("SMART GAME est un jeu qui permet de dévelopé vos facultées  naturel grâce à nos devinettes de chiffre incroyable ")
print("Commençons")
print ("J'ai chisit un nombre  aléatoire entre 1 et 100 que tu vas essayer de deviné en 5 essaies ")
print("A chaque fois que tu donne une fausse réponse je te guide en te donnent la position du chiffre magique par rapport au chiffre que tu as donné")
print("Prêt ?")
#___________________________________________________________________________________________________________________________________

#3) LE CHOIX DU NOMBRE MAGIQUE 
import random
x=  random.randint(1,100)
essais = 10
print("j'ai choisi un nombre entre 1 et 100")
print("Tu as 10 essais")
while essais >0:
    try:
       n=int(input("Saisis le nombre magique : "))
    except ValueError:
        print("Entre un nombre valide ")
        continue



    if n==x :
        print("Bravo, tu as gagné !")
        gagne = True
        break

       
    elif n<x :
        print("Trop petit")
    else:
        print("Trop grand ")
    
    essais -= 1
    print("Essais restants : ", essais)
if essais == 0:
    print("Perdu ! le nombre étai : ",x)
    gagne = False

if not gagne:
    print("Perdu ! le nombre était :", x)








 

    
    

