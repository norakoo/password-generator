# TP4 - Générateur de mots de passe - Fichiers

---

## Etapes

---

### 1 - Ouvrir un fichier pour la liste des mots

Code de la fonction ```get_word_list_from_file()``` :

```python
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
```

> *Question 1 :* Si nous n'avions pas utilisé de gestionnaire de contexte (with ... as ...: ), qu'aurait-on dû absolument faire après avoir travaillé avec notre fichier ? Quelle méthode aurions-nous dû utiliser pour ça ?
- On aurait dû fermer absolument le fichier grâce à la méthode ```fichier.close()```.

---

### 2 - Ecrire dans un fichier

Code de la fonction ```write_password_in_file``` :

```python
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
```

> *Question 1 :* Que constatez-vous dans le fichier si vous appelez plusieurs fois votre programme à la suite ?
- Cela génère et écrit le nombre de mot de passe qui équivaut au nombre de fois ou le programme a été exécuté.
> *Question 2 :* Quelle est la différence entre le mode "write" et le mode "append" ?
- Le mode "write" supprime le contenu du fichier pour écrire à l'intérieur, tandis que le mode "append" écrit sans supprimer, il rajoute des lignes.
> *Question 3 :* Quel mode puis-je utiliser si je veux à la fois lire et écrire dans mon fichier ?
- On doit rajouter "+" après la lettre, comme "r+" qui nous permet de lire et d'écrire dans le fichier.

---

### 3 - Faire un vrai jet de dés

Code de la fonction ```tirer_les_des``` :

```python
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
```

---

### 4 - Générer une passphrase tirée aux dés

Code de la fonction ```generer_dice_passphrase``` :

```python
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
```

> *Question 1 :* Quelle est la différence entre la syntaxe ```mon_dict[key]``` et ```mon_dict.get(key)```, sachant que ```mon_dict``` est un dictionnaire python ?
- La différence est que ```mon_dict[key]``` permet d'accéder à la clé en question, tandis que ```mon_dict.get(key)``` permet d'obtenir la valeur correspondant à la clé.

---

### Bonus - Lire les dictionnaires à partir d'un fichier