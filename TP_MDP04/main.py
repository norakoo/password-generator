import mdp # On importe le module mdp

choix_utilisateurice=-1 # On affecte une valeur non utilisé à la variable pour pouvoir lancer la boucle.

"""
Docstring de la fonction write_password_in_file()

On lui affecte 2 paramètres, password et filename avec comme valeur par défaut passwords.txt

On ouvre et on écrit dans le fichier passwords.txt

On écrit dedans la valeur de la variable password et on saute une ligne

On renvoie password
"""

def write_password_in_file(password,filename="passwords.txt"):
    with open("passwords.txt", "a", encoding="UTF-8") as file:
        file.write(password + "\n")
    return password

"""
Docstring de la fonction afficher_menu().
    
Ici on définit la fonction afficher_menu() sans paramètre.
    
Elle permet, quand elle est appellée, d'afficher le menu du générateur de mots de passe.
"""

def afficher_menu(): # On définit une fonction 'afficher_menu' sans paramètre.
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
    print("5 - Phrase de passe avec configuration EFF")
    print("6 - Générer un fichier avec des passphrases")
    print("")
    print("0 - Quitter le menu du générateur.")
    print("")
    
"""
Docstring de la fonction choix_generateur(choix_utilisateur).
    
On définit une fonction choix_générateur() avec comme paramètre choix_utilisateur.
    
On détecte le choix de celui-ci, et on renvoie plusieurs cas avec plusieurs messages personnalisées, ou, pour les cas 1 et 2
on génère un mot de passe complètement aléatoire.
"""
    
def choix_generateur(choix_utilisateurice): # On définit une fonction 'choix_generateur' avec comme paramètre 'choix_utilisateurice'.
    match choix_utilisateurice:
        case 1:
            print(mdp.generer_mdp()) # On appelle la fonction 'generer_mdp' et on l'affiche.
        case 2:
            password_length = int(input("Veuillez entrer une longueur de mot de passe : ")) # On demande à l'utilisateur de choisir une longueur de mot de passe.
            print(mdp.generer_mdp(password_length)) # On renvoie son mot de passe en fonction de la longueur choisie.
        case 3:
            print(mdp.generer_passphrase())
        case 4:
            nb_words = int(input("Veuillez entrer un nombre de mots à générer : "))
            print(mdp.generer_passphrase(nb_words))
        case 5:
            print(mdp.generer_dice_passphrase())
        case 6:
            password = mdp.generer_passphrase()
            print(write_password_in_file(password))
        case 0:
            print("Vous quittez le programme. Au revoir :)")
        case _:
            print(f"Erreur : l'option {choix_utilisateurice} n'existe pas ! Veuillez entrer une option valide.")
            
    if choix_utilisateurice!=0:
        input("Appuyez sur 'Entrée' pour reboucler") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.

while choix_utilisateurice!=0: # Tant que 'choix_utilisateurice' est différent de 0.
    
    afficher_menu() # On appelle la fonction.
    
    choix_utilisateurice=int(input("Saisissez votre choix : ")) # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice' en 'int' à chaque boucle.
    
    choix_generateur(choix_utilisateurice)