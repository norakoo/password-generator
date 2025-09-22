choix_utilisateurice=-1 # On affecte une valeur non utilisé à la variable pour pouvoir lancer la boucle.

while choix_utilisateurice!=0: # Tant que 'choix_utilisateurice' est différent de 0.
    print("=================================================")
    print("HAUTOT Nolan | CIEL - Générateur de mots de passe")
    print("=================================================")
    print("") # Cette ligne permet de créer un espace entre deux lignes, ce qui rend le menu plus lisible.
    print("Quel type de mot de passe souhaitez-vous créer ?")
    print("")
    print("1 - Mot de passe avec configuration par défaut.")
    print("2 - Mot de passe avec configuration personnalisée.")
    print("3 - Phrase de passe avec configuration par défaut.")
    print("4 - Phrase de passe avec configuration personnalisée.")
    print("")
    print("0 - Quitter le menu du générateur.") # On affiche le menu entier à chaque boucle.
    print("")
    
    choix_utilisateurice=int(input("Saisissez votre choix : ")) # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice' en 'int' à chaque boucle.
    
    match choix_utilisateurice:
        case 1:
            print("Mot de passe par défaut : mot2passe!")
        case 2:
            print("Mot de passe personnalisé : M0td3p4ss3#@")
        case 3:
            print("Phrase de passe par défaut : Voici1phrasemdppardefaut!")
        case 4:
            print("Phrase de passe personnalisée : V0ic1unephr4s3mdpPERSO#!$")
        case 0:
            print("Vous quittez le programme. Au revoir :)")
        case _:
            print(f"Erreur : l'option {choix_utilisateurice} n'existe pas ! Veuillez entrer une option valide.")
            
    if choix_utilisateurice!=0:
        input("Appuyez sur 'Entrée' pour reboucler") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.