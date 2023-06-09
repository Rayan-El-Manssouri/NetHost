# Python Wi-Fi Box App

<div align="center">
  <img src="./assets/logo.png" alt="Logo" height="200">
</div>

## Table des matières
- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Remarque](#remarque)

## Introduction
Ce code est une application Python qui transforme votre ordinateur en une box Wi-Fi. Il crée un serveur web local sur le port 8080, vous permettant d'accéder à des fichiers statiques et de gérer des boîtes Wi-Fi à partir d'un navigateur web.

## Prérequis
- Python 3.x
- Les packages suivants doivent être installés :
  - `socket`
  - `os`
  - `threading`
  - `webbrowser`
  - `json`
  - `wmi`
  - `win10toast`
  - `PIL`
  - `pystray`

## Configuration
Avant d'exécuter l'application, assurez-vous de configurer les éléments suivants :

### Répertoire des fichiers statiques
Le répertoire `www` contient les fichiers statiques (HTML, CSS, JavaScript) que vous souhaitez rendre accessibles via le serveur web local. Placez vos fichiers dans ce répertoire.

### Chemin de l'image du logo
Spécifiez le chemin vers votre propre image de logo en remplaçant le chemin `./assets/logo.png` par le chemin de votre image.

## Utilisation
1. Exécutez le script Python à l'aide de la commande `python index.py`.
2. L'application démarrera et affichera le logo dans la barre d'état système.
3. Cliquez avec le bouton droit de la souris sur l'icône pour afficher le menu.
4. Sélectionnez "Ouvrir le serveur web" pour démarrer le serveur.
5. Le serveur est maintenant en cours d'exécution et accessible à l'adresse `http://localhost:8080`.
6. Les fichiers statiques présents dans le répertoire `www` peuvent être consultés à partir du navigateur.
7. Le fichier `index.html` est spécialement pris en charge et chaque fois qu'il est chargé, la liste des boîtes Wi-Fi disponibles est mise à jour et enregistrée dans le fichier `wifi_boxes.json`.
8. Pour arrêter le serveur, sélectionnez "Quitter" dans le menu.

## Remarque
- Assurez-vous que les autorisations et les pare-feux appropriés sont configurés pour permettre l'accès au serveur sur le port 8080.
- L'application utilise la bibliothèque `wmi` pour récupérer les informations sur les boîtes Wi-Fi. Assurez-vous que vous avez les privilèges suffisants pour accéder à ces informations.
