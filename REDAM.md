# Gestionnaire de Tâches et de Notes

Ce petit programme Python permet de créer et de gérer facilement une liste de tâches ou de notes directement dans la console (le terminal). 

## Ce que le programme permet de faire

Une fois le programme lancé, vous pouvez :
* **Ajouter vos tâches :** Choisir combien de tâches vous voulez noter et les écrire une par une.
* **Afficher la liste :** Voir toutes vos notes enregistrées d'un seul coup.
* **Rechercher une note :** Vérifier si une note existe grâce à son numéro.
* **Modifier une note :** Changer le texte d'une note déjà écrite.
* **Supprimer une note :** Effacer une note dont vous n'avez plus besoin.
* **Épingler une note :** Mettre en avant une tâche importante en ajoutant `*****épingler*****` à côté.

## Comment le projet a été construit

Le code dans `main.py` a été organisé étape par étape :
1. **Demander le nombre de tâches :** Création de `saisir_N()` pour s'assurer que l'utilisateur entre bien un nombre positif (supérieur à $0$).
2. **Enregistrer les notes :** Avec `saisir_les_taches()`, le programme récupère chaque tâche et les range les unes à la suite des autres.
3. **Gérer les notes :** Création d'une fonction pour chaque action (afficher, rechercher, modifier, supprimer, marquer). Pour modifier une ligne précise, le programme découpe le texte ligne par ligne, fait le changement, puis recolle le tout.
4. **Créer le menu :** La fonction `service()` affiche les choix possibles (de `0` à `5`) et lance l'action demandée.
# 1. Initialiser le dépôt Git dans le dossier
git init

# 2. Ajouter uniquement le fichier Python principal
git add main.py

# 3. Enregistrer le premier commit
git commit -m "feat: ajouter le code de base du gestionnaire de tâches (main.py)"

# 1. Ajouter le fichier README.md
git add README.md

# 2. Enregistrer le deuxième commit
git commit -m "docs: ajouter le fichier README.md explicatif"

## Comment lancer le programme sur VS Code
1. Ouvrez **Visual Studio Code**.
2. Ouvrez le dossier de votre projet, puis cliquez sur le fichier **`main.py`** pour l'afficher à l'écran.
3. Regardez tout en haut à droite de la fenêtre et cliquez sur le bouton **« Run Python File »** (la petite flèche de lecture **▷**).
4. Une fenêtre de terminal va s'ouvrir en bas : cliquez dedans pour répondre aux questions du programme et gérer vos tâches.

## ce travail a été développer par MESTAYSSER AMAN ALLAH
