import secrets # On importe les modules secrets et string.
import string
from eff_words import get_word_list

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

"""
Docstring de la fonction generer_passphrase

Cette fonction va nous permettre de générer une phrase de passe avec un nombre de mots aléatoires

On l'initialise avec un paramètre 'nb_words' (qui aura pour valeur par défaut 6)

On créer une liste 'words' qui prend la liste entière de 'eff_words.py'

On créer une liste vide 'passphrase_words'

On répète ensuite 6 fois :
    
    On prend notre liste et on lui ajoute un mot aléatoire de la liste 'words'
    
On sépare chaque chaîne de caractère de la liste 'passphrase_words' par un tiret

On renvoie passphrase_words
"""

def generer_passphrase(nb_words=6):
    words = get_word_list()
    passphrase_words = []
    for _ in range(nb_words):
        passphrase_words.append(secrets.choice(words))
    passphrase_words = "-".join(passphrase_words)
    return passphrase_words