#Progreammation Bibliothèque mini-projet 
#Catalogue des produits
#____________________________________________________________
produit_1 = [
    {"nom" : "chaussure","prix": 100000},
    {"nom" : "t-short", "prix": 80000},
    {"nom" : "casquette ", "prix": 50000}, 
    {"nom" : "chaussete", "prix": 10000}
]
for produit in produit_1 :
    print("Produit :", produit["nom"])
    print("Prix :", produit["prix"])
    print("-----") 
produit = produit_1
#______________________________________________________________

#Exercice développeur
nom= input("Votre nom : ")
mail= input ("votre e-mail: ")
panier =input("placer un élément dans le panier: ")
user= {
    "nom" :nom ,  
    "e-mail": mail,
    "panier": panier
}
for cle, valeur in user.items():
    print(cle, valeur)

import random
x = random.randint(1, 100)
print("Merci pour la commande votre clé de validation est :", x ,"veillers saisir pour finaliser la commande ")
confirmation = input (" enter le Code : ")
confirmation = int(confirmation)
if x == confirmation :
    print(" Commande validé avec sucsès Merci pour votre coonfiance")