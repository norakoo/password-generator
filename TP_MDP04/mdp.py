import secrets # On importe les modules secrets et string.
import string
from eff_words import get_word_list, get_word_dict

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
    words = get_word_list_from_file()
    passphrase_words = []
    for _ in range(nb_words):
        passphrase_words.append(secrets.choice(words))
    passphrase_words = "-".join(passphrase_words)
    return passphrase_words

"""
Docstring de la fonction generer_dice_passphrase

On initialise la variable 'words' à laquelle on affecte le dictionnaire 'get_word_dict()'

On initialise une liste passphrase_words vide

On boucle nb_words de fois :

    On appelle la fonction tirer_les_des() qu'on affecte à la variable des
    
    On ajoute dans la lite passphrase_words les mots correspondant à la valeur 'XXXXX' du mot
    
On renvoie la passephrase en une chaîne de caractère entière
"""

def generer_dice_passphrase(nb_words=6):
    words = get_word_dict()
    passphrase_words = []
    for _ in range(nb_words):
        des = tirer_les_des()
        passphrase_words.append(words[des])
    return "".join(passphrase_words)

"""
Docstring de la fonction tirer_les_des()

On initialise une liste dice vide

On boucle 5 fois la liste à laquelle on ajoute un chiffre entre 1 et 5

On renvoie la liste de chiffre sous forme 'XXXXX'
"""

def tirer_les_des():
    dice = []
    for _ in range(5):
        dice.append(str(secrets.randbelow(6) + 1))
    return "".join(dice)

"""
Docstring de la fonction get_world_list_from_file()

On lui attribue un paramètre filename qui par défaut est "worldlist_fr.txt"

On initialise une liste lines vide

On ouvre et on lit le fichier worldlist_fr.txt

Pour chaque ligne dans le fichier

    On ajoute chacune des lignes dans la liste lines

On renvoie la liste lines

"""

def get_word_list_from_file(filename="worldlist_fr.txt"):
    lines = []
    with open("D:\Python\TP Python\TP_MDP04\wordlist_fr.txt", "r", encoding="utf-8") as file:
        for ligne in file:
            lines.append(ligne.strip())
    return lines