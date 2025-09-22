import secrets # On importe les modules secrets et string.
import string

LETTRES = string.ascii_letters # Définit toutes les lettres autorisées
CHIFFRES = string.digits # Définit tous les chiffres autorisés
SPECIAL = string.punctuation # Définit les caractères spéciaux autorisés

ALPHABET = LETTRES + CHIFFRES + SPECIAL # Ensemble complet des caractères autorisés
"""
Docstring de la fonction generer_mdp.

Cette fonction va nous permettre de générer un mot de passe 'password' aléatoire avec une certaines longueur 'password_length=14'.

On l'initialise avec deux paramètres, password et password_length (qui aura pour valeur par défaut 14).

Ensuite on fait une boucle pour générer un mot de passe avec le nombre de caractère que l'on veut (grâce à password_length).

On renvoie un mot de passe avec des caractères aléatoires.
"""

def generer_mdp(password_length=14): # On définit une fonction 'generer_mdp' avec les paramètres 'password' et 'password_length'
    password = ""
    for _ in range(password_length): # Pour chaque valeur jusqu'à un max de password_length.
        password += secrets.choice(ALPHABET) # On fais un choix aléatoire dans l'alphabet pour fabriquer un mot de passe complètement aléatoire.
    return password # On renvoie 'password'

def generer_mdp_avec_contrainte(password_length=14,special=1,digits=1):
    password = ""
    for _ in range(password_length):
        
    return password