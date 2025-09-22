# Compte Rendu - Itération 1 - Menu interactif en Python

## Réponses

### 1 - Affichage du titre et du menu

Code Python :

```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
```

Ce code affiche bien le résultat demandé.

### 2 - Demander le choix à l'utilisateurice

Code Python :

```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
input("Saisissez votre choix : ") # On demande le choix.
```

Ici on demande à l'utilisateurice de saisir son choix.

> *Question 1 :* Quel est le type de la donnée récupérée via ```input``` ?
- Le type de donnée récupérée via ```input``` est un ```string```.
> *Question 2 :* Comment allez-vous stocker cette donnée ? Quel type aura la variable ?
- Pour stocker cette donnée, on utilisera une variable nommée ```choix_utilisateurice```. La variable aura comme type un ```string```. 

**Code pour la question 2 :**
```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
choix_utilisateurice=input("Saisissez votre choix : ") # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice'.
```

### 3 - Gérer les choix valides

Code Python :

```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
choix_utilisateurice=input("Saisissez votre choix : ") # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice'.
if int(choix_utilisateurice)==1: # Ici on regarde si (if) la valeur entière (int) de la variable 'choix_utilisateurice' est égale à 1.
    print("Mot de passe par défaut") # Si oui alors on affiche le texte ici présent.
elif int(choix_utilisateurice)==2: # Sinon si (elif) la valeur entière (int) de la variable 'choix_utilisateurice' est égale à 2.
    print("Mot de passe personnalisé") # On affiche ce texte. Ainsi de suite.
elif int(choix_utilisateurice)==3:
    print("Phrase de passe par défaut")
elif int(choix_utilisateurice)==4:
    print("Phrase de passe personnalisée")
elif int(choix_utilisateurice)==0:
    print("Vous quittez le programme")
```

### 4 - Gérer les choix invalides

Code Python

```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
choix_utilisateurice=input("Saisissez votre choix : ") # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice'.
if int(choix_utilisateurice)==1: # Ici on regarde si (if) la valeur entière (int) de la variable 'choix_utilisateurice' est égale à 1.
    print("Mot de passe par défaut") # Si oui alors on affiche le texte ici présent.
elif int(choix_utilisateurice)==2: # Sinon si (elif) la valeur entière (int) de la variable 'choix_utilisateurice' est égale à 2.
    print("Mot de passe personnalisé") # On affiche ce texte. Ainsi de suite.
elif int(choix_utilisateurice)==3:
    print("Phrase de passe par défaut")
elif int(choix_utilisateurice)==4:
    print("Phrase de passe personnalisée")
elif int(choix_utilisateurice)==0:
    print("Vous quittez le programme")
else: # Si le choix ne correspond à aucune possibilité cité ci-dessus.
    print(f"Erreur : l'option {choix_utilisateurice} n'existe pas.") # Alors on affiche une chaîne formatée (f{variable}) expliquant que ce choix n'existe pas.
```

> *Question 1 :* Que se passe-t-il lorsque l'utilisateurice saisit une lettre au lieu d'un chiffre lors du choix de l'option ? Pourquoi à votre avis ?
- Lorsque l'utilisateur saisit une lettre ```a par exemple``` à la place d'un chiffre lors du choix de l'option, une erreur survient.
- Cette erreur se produit car la variable ```choix_utilisateurice``` au niveau du ```if int(choix_utilisateurice)``` transforme la variable, qui était au préalable un ```string```, en ```int```. 1 peut être convertis en un nombre, mais a par exemple ne peut pas être convertis > en un nombre.

```python
if int(choix_utilisateurice)==1: # Ici on regarde si (if) la valeur entière (int) de la variable 'choix_utilisateurice' est égale à 1.
ValueError: invalid literal for int() with base 10: 'a'
```

**Simplification du code :**

Ici à chaque condition si, on convertis la variable en int. 

```python
if int(choix_utilisateurice)==1:
```

Pour simplifier le code, il suffit juste d'effectuer cette conversion une fois lors de l'input :

```python
choix_utilisateurice=int(input("Saisissez votre choix : "))
```

Code Python avec la simplification :

```python
print("==================================")
print("CIEL - Générateur de mots de passe")
print("==================================")
print("Quel type de mot de passe souhaitez-vous créer ?")
print("1 - Mot de passe avec configuration par défaut")
print("2 - Mot de passe avec configuration personnalisée")
print("3 - Phrase de passe avec configuration par défaut")
print("4 - Phrase de passe avec configuration personnalisée")
print("0 - Quitter")
choix_utilisateurice=int(input("Saisissez votre choix : ")) # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice' en 'int'.
if choix_utilisateurice==1: # Ici on regarde si (if) la valeur de la variable 'choix_utilisateurice' est égale à 1.
    print("Mot de passe par défaut") # Si oui alors on affiche le texte ici présent.
elif choix_utilisateurice==2: # Sinon si (elif) la valeur de la variable 'choix_utilisateurice' est égale à 2.
    print("Mot de passe personnalisé") # On affiche ce texte. Ainsi de suite.
elif choix_utilisateurice==3:
    print("Phrase de passe par défaut")
elif choix_utilisateurice==4:
    print("Phrase de passe personnalisée")
elif choix_utilisateurice==0:
    print("Vous quittez le programme")
else: # Si le choix ne correspond à aucune possibilité cité ci-dessus.
    print(f"Erreur : l'option {choix_utilisateurice} n'existe pas.") # Alors on affiche une chaîne formatée (f{variable}) expliquant que ce choix n'existe pas.
```

### 5 - Ajouter une boucle

Code Python:

```python
choix_utilisateurice=-1 # On affecte une valeur non utilisé à la variable pour pouvoir lancer la boucle.

while choix_utilisateurice!=0: # Tant que 'choix_utilisateurice' est différent de 0.
    print("==================================")
    print("CIEL - Générateur de mots de passe")
    print("==================================")
    print("Quel type de mot de passe souhaitez-vous créer ?")
    print("1 - Mot de passe avec configuration par défaut")
    print("2 - Mot de passe avec configuration personnalisée")
    print("3 - Phrase de passe avec configuration par défaut")
    print("4 - Phrase de passe avec configuration personnalisée")
    print("0 - Quitter") # On affiche le menu entier à chaque boucle.
    
    choix_utilisateurice=int(input("Saisissez votre choix : ")) # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice' en 'int' à chaque boucle.
    
    if choix_utilisateurice==1: # Ici on regarde si (if) la valeur de la variable 'choix_utilisateurice' est égale à 1.
        print("Mot de passe par défaut") # Si oui alors on affiche le texte ici présent.
        
    elif choix_utilisateurice==2: # Sinon si (elif) la valeur de la variable 'choix_utilisateurice' est égale à 2.
        print("Mot de passe personnalisé") # On affiche ce texte. Ainsi de suite.
        
    elif choix_utilisateurice==3:
        print("Phrase de passe par défaut")
        
    elif choix_utilisateurice==4:
        print("Phrase de passe personnalisée")
        
    elif choix_utilisateurice==0:
        print("Vous quittez le programme")
        break
        
    else: # Si le choix ne correspond à aucune possibilité cité ci-dessus.
        print(f"Erreur : l'option {choix_utilisateurice} n'existe pas.") # Alors on affiche une chaîne formatée (f{variable}) expliquant que ce choix n'existe pas.
    input("Appuyez sur 'Entrée' pour reboucler") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.
```

Pour pouvoir appliquer une boucle, il faut **modifier le code** afin d'avoir quelque chose de logique. On sait que grâce à notre boucle, si **la valeur est différent de 0** alors le programme **se répète**. Il nous suffit donc d'**initialiser la variable à -1** *(valeur non utilisée dans le programme)* pour pouvoir **initier la boucle** sans problème.

> *Question 1 :* Quelle boucle sera la plus adaptée ? Pourquoi ?
- La boucle qui sera la plus adaptée est la boucle ```while```. Elle nous permettra de faire tourner le programme en boucle si ```choix_utilisateurice``` est différent de 0 car on ne connait pas le nombre d'itérations à l'avance.
> *Question 2 :* Comment éviter de déclencher la pause lorsque l'utilisateurice souhaite quitter le programme ?
- Pour éviter de déclencher la pause lorsque l'utilisateurice souhaite quitte le programme, il faut "casser" la boucle à ce moment là.

```python
elif choix_utilisateurice==0:
        print("Vous quittez le programme")
```

Ici le programme relancera la boucle dès que l'utilisateurice aura tapé 0, et ce n'est pas ce que nous voulons. Il suffit de rajouter un mot pour pouvoir changer tout ça.

```python
elif choix_utilisateurice==0:
        print("Vous quittez le programme")
        break
```

Ici grâce à ```break```, quand l'utilisateurice tapera 0, la boucle se cassera et donc s'arrêtera, ce qui évite donc le système de pause mis en place précédemment pour cette condition précise.

- Il est possible d'utiliser une autre technique à l'aide d'une variable ```continuer``` qui sera mis sur ```True``` par défaut.

```python
choix_utilisateurice=-1 # On affecte une valeur non utilisé à la variable pour pouvoir lancer la boucle.
continuer=True # On affecte True à la variable continuer qui nous servira pour la pause pour 0.

while choix_utilisateurice!=0: # Tant que 'choix_utilisateurice' est différent de 0.
    print("==================================")
    print("CIEL - Générateur de mots de passe")
    print("==================================")
    print("Quel type de mot de passe souhaitez-vous créer ?")
    print("1 - Mot de passe avec configuration par défaut")
    print("2 - Mot de passe avec configuration personnalisée")
    print("3 - Phrase de passe avec configuration par défaut")
    print("4 - Phrase de passe avec configuration personnalisée")
    print("0 - Quitter") # On affiche le menu entier à chaque boucle.
    
    choix_utilisateurice=int(input("Saisissez votre choix : ")) # On demande le choix, qui sera stocké dans la variable 'choix_utilisateurice' en 'int' à chaque boucle.
    
    if choix_utilisateurice==1: # Ici on regarde si (if) la valeur de la variable 'choix_utilisateurice' est égale à 1.
        print("Mot de passe par défaut") # Si oui alors on affiche le texte ici présent.
        
    elif choix_utilisateurice==2: # Sinon si (elif) la valeur de la variable 'choix_utilisateurice' est égale à 2.
        print("Mot de passe personnalisé") # On affiche ce texte. Ainsi de suite.
        
    elif choix_utilisateurice==3:
        print("Phrase de passe par défaut")
        
    elif choix_utilisateurice==4:
        print("Phrase de passe personnalisée")
        
    elif choix_utilisateurice==0:
        print("Vous quittez le programme")
        continuer=False # Affecter False à continuer pour sortir de la boucle sans Break.
        
    else: # Si le choix ne correspond à aucune possibilité cité ci-dessus.
        print(f"Erreur : l'option {choix_utilisateurice} n'existe pas.") # Alors on affiche une chaîne formatée (f{variable}) expliquant que ce choix n'existe pas.
        
    if continuer==True: # Si continuer est Vrai.
        input("Appuyez sur 'Entrée' pour reboucler") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.

```

C'est une méthode alternative pour pouvoir sortir de la boucle à ```choix_utilisateurice=0``` et ne pas effectuer la pause. Ci-dessous le code qui nous permet de tout le temps rester dans la boucle quand nous ne somme pas dans la situation ```choix_utilisateurice=0```.

```python
if continuer==True: # Si continuer est Vrai.
        input("Appuyez sur 'Entrée' pour reboucler") # Ici dès que l'utilisateur appuie sur 'Entrée', la boucle repars à zéro.
```

## Pour aller plus loin

### Bonus - Améliorations

```python
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
```

### Bonus difficile - Utiliser l'instruction ```match```

Code Python :

```python
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
```

> *Question :* Comment gérer les cas non prévus dans le menu (ce que faisait le ```else```) avec ```match``` ?
- Pour gérer les cas non prévus tels que entrer 5, 6 ou + en valeurs, il faut utiliser ```case _:```. Dans ce cas là, si tout autre valeur que celles demandés sont tapés, alors le programme renvois le message d'erreur et raffiche le menu.