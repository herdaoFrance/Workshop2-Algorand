# Workshop-2---Algorand-Blockchain-
Bienvenue pour ce deuxième workshop ;) 

🧵 Pour cette partie du workshop, nous allons nous concentrer sur une blockchain en particulier : Algorand. Voyons comment configurer notre environnement pour ce workshop, et nous commencerons à déployer des smart contracts sur cette blockchain 



## Quelques termes techniques à éclairer avant de commencer le workshop 
📌 Smart contract :  

📌


<details>
  <summary><h1>Installation des logiciels principaux</h1></summary>
  
  - Visual Studio Code
  
  Comme pour un peintre, il faut sa toile. La developeuse à besoin de son environnement de programmation pour coder.  Il en existe plein sur le marché, Sublim text, Vim ect …  
Mais Visual Studio Code à l’avantage de relier plusieurs application, tel que Github et d’être assez ergonomique. 
  https://visualstudio.microsoft.com/fr/downloads/
  
  - Installation de node js 
  
  NPM (Node Package Manager) est un gestionnaire de paquets permettant l’installation facile des modules (bibliothèques de code) qui peuvent être utilisés dans votre projet  
  [Node.js](https://nodejs.org/en/)
  ```bash
  npm -v 
  npm install <library-name> 
  npm run build 
  ```
  
  - Installation de yarn ( similaire à npm, c'est un gestionnaire de paquet, permettant l'installation des bibliothèques et des librairies).
  ```bash
  npm install yarn
  ```
  
  - Le terminal: déjà installer sur VS Code. Voici les commandes prinipales sur le terminal. 
  
  **`ls`**: affiche la liste des fichiers et des répertoires dans le répertoire courant
  
  **`cd`**: change de répertoire
  
  **`mkdir`**: crée un nouveau répertoire
  
  **`touch`**: crée un nouveau fichier vide
  
  **`rm`  :**  supprime un répertoire
  
  **`rm -r <nom du fichier>` :** supprime un fichier 
  
  **`echo`**: affiche du texte à l'écran
  
</details>
  
  
👉🏽 A partir de votre terminal, placez-vous dans le dossier “Document” . Puis, créée un nouveau dossier appelé “H.E.R DAO”

  
<details>
  <summary><h1>Les outils de la développeuse</h1></summary> 
    
  - Github : l'outil open source

  C'est LA plateforme permettant d'échanger du code entre dév, de stocker et de gérer notre code, ainsi que de travailler en collaboration sur des projets de développement de logiciels. 
  
Pour s'approprier un peu l'outil, nous allons forker le projet, puis nous allons clôner notre répertoire sur notre ordinateur . Mais, qu'est ce fork, et clone ?? 👀

Voyons une liste des termes couramment utilisé sur Github: 

  **`dépôt`**(repository) = espace de stockage centralisé pour les fichiers d'un projet.
  
  **`commit `** = enregistrement des modifications apportées aux fichiers dans le dépôt.
  
  **`branche`**(branch) =  une version séparée du dépôt qui permet de travailler sur des fonctionnalités spécifiques sans affecter la version principale (master).

  **`clône `** = une copie locale d'un dépôt sur votre ordinateur.

  **`forks `** = copie du dépôt d'origine sur votre compte GitHub.

  **`demande de fusion`** (pull request) = demande d'intégration des modifications d'une branche à une autre.

  **`issues `** = section de gestion des bugs et des améliorations proposées pour un projet.


  - Github Desktop : 
  [GitHub Desktop](https://desktop.github.com/)
</details>

👉🏽 Forker le projet Workshop1 dans ton Github 
1. Dans ton Github, fork le projet à partir du boutton en haut à gauche 'fork'
  
2. Retourne dans 'your repository' (tes dépôts)
  
3. Done, il est maintenant disponible dans tes repertoires GitHub ! tu as forker ton premier projet, 🔆

👉🏽 Clône le repository sur ton ordinateur en local 
  1. Dans tes repository, appuie sur le bouton vert 'code' 

  2. Puis copie le lien, et rendez-vous sur Github Desktop
  
  3. Dans 'add', vous pouvez selectionner 'clone a repository' (clôner un répertoire) 
  
  4. Selectionne le 'local path' que nous venons de créer via notre terminal. 
  
  5. Done, il est maintenant disponible dans tes repertoires locales, sur ton ordinateur ! tu as clôner ton premier projet, 🔆
  
  
<details>

  <summary><h1>Coder sur une blockchain</h1></summary>
Nous avons maintenant à peu près tous les outils dans notre trousse nous permettant de coder. Mais, chaque blockchain à un environnement et un langage bien spécifique. Par exemple Ethereum utilise le langage de programmation Solidity pour ces smarts contracts. Et nous allons explorer cela. Mais, Algorand par exemple, utilise un autre environnement de programmation, et nous verrons cela lors du prochain workshop. 
Pour le moment, voyons comment déployer un smart contract sur Ethereum. 

✌🏽 Pas de panique l'objectif n'est pas de tout comprendre, simplement de prendre en main les outils principaux. 
  
  - Installation de solidity sur VS CODE
  
  Dans extension, il est possible de télécharger les langages de programmations que l'on souhaite.
  
  - Installation de Hardhat 
  
  Pour écrire un smart contract, nous avons besoin d’un outil de développement de smart contract, visant à simplifier le processus de construction, de déploiement et de test de ces contrats. Les plus utilisés sont Hardhat, Truffle, Brownie, Ganache et Remix. Nous n’allons pas tous les utiliser, mais ils fonctionnent à peu près tous de la même façon. 
Pour notre fil rouge, nous allons installer hardhat. 
  ```bash
  npm install --save-dev hardhat
  ```
</details>
👉🏽 Créez un nouveau projet 'javaScript project", valider toutes les optionnalités. Supprimez tous les fichiers dans le dossier *contracts* et intégrer le fichier forker précèdement. 



✅ Vous avez maintenant tous les outils nécessaire pour commencer à coder ! 

Have fun xxx
 
