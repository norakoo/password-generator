choix_utilisateurice=-1 # On affecte une valeur non utilisé à la variable pour pouvoir lancer la boucle.
continuer=True # On affecte True à la variable continuer qui nous servira pour la pause pour 0.

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
    
    if choix_utilisateurice==1: # Ici on regarde si (if) la valeur de la variable 'choix_utilisateurice' est égale à 1.
        print("Mot de passe par défaut : mot2passe!") # Si oui alors on affiche le texte ici présent.
        
    elif choix_utilisateurice==2: # Sinon si (elif) la valeur de la variable 'choix_utilisateurice' est égale à 2.
        print("Mot de passe personnalisé : M0td3p4ss3#@") # On affiche ce texte. Ainsi de suite.
        
    elif choix_utilisateurice==3:
        print("Phrase de passe par défaut : Voici1phrasemdppardefaut!")
        
    elif choix_utilisateurice==4:
        print("Phrase de passe personnalisée : V0ic1unephr4s3mdpPERSO#!$")
        
    elif choix_utilisateurice==0:
        print("Vous quittez le programme. Au revoir :)")
        continuer=False # Affecter False à continuer pour sortir de la boucle sans Break.
        
    else: # Si le choix ne correspond à aucune possibilité cité ci-dessus.
        print(f"Erreur : l'option {choix_utilisateurice} n'existe pas ! Veuillez entrer une option valide.") # Alors on affiche une chaîne formatée (f{variable}) expliquant que ce choix n'existe pas.
        
    if continuer==True: # Si continuer est Vrai.
        input("Appuyez sur 'Entrée' pour rouvrir le menu et faire un autre choix.") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.