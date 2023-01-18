# Workshop2 Algorand
Bienvenue pour ce deuxième workshop ;) 

🧵 Aujourd'hui nous allons nous concentrer sur une blockchain en particulier : Algorand. Voyons comment configurer notre environnement pour ce workshop, et nous commencerons à déployer des smart contracts sur cette blockchain 



## Quelques termes techniques à éclairer avant de commencer le workshop 
📌 Smart contract :  Un smart contract est un contrat automatisé qui utilise la technologie de la blockchain pour s'exécuter de manière autonome. Il permet de gérer des transactions électroniques sans avoir besoin d'intermédiaires.

📌 SDK : Softaware Development Kit - c'est une collection d'outils. Les SDK sont comme des boîtes à outils pour construire des logiciels. 


<details>
  <summary>
  <h1>Installation des logiciels principaux</h1>
  </summary>
  
  - Installation de brew (pour mac / linux) 
  
~~~
cd /opt
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
export PATH=/opt/homebrew/bin:$PATH
export PATH=/opt/homebrew/sbin:$PATH
~~~
    - Installation de WSL (pour windows)
  
  Il est possible d'utiliser Homebrew (ou "brew" en anglais) sur Windows en utilisant la fonctionnalité Windows Subsystem for Linux (WSL). Cependant, il est important de noter que cela n'est pas pris en charge officiellement et que certains outils et paquets peuvent ne pas fonctionner comme prévu.

Pour installer WSL sur Windows, vous devez avoir la version 1607 ou ultérieure de Windows 10 et suivre ces étapes:

Ouvrez l'application Paramètres en appuyant sur la touche Windows + I

Cliquez sur "Apps"

Cliquez sur "Programmes et fonctionnalités"

Cliquez sur "Activer ou désactiver les fonctionnalités Windows"

Cochez la case "Windows Subsystem for Linux"

Cliquez sur "OK" et redémarrez votre ordinateur

  - Installation de python 3 
  
Pour Mac et Linux : `brew install python3`

Pour Windows ( WSL )
```sudo apt-get update
sudo apt-get install python3```

ou 
  
```sudo apt-get install python```


  - Installation de Docker : `https://docs.docker.com/compose/install/`
  
  - Installation de sandbox (clône de repo par github Desktop) : `https://github.com/algorand/sandbox.git`

( Ajout de code dans le fichier sandbox/docker-compose sous les ports ) 

```
volumes:
- type: bind
  source: ../
  target: /data 
```

  Initialisation de sandbox
`./sandbox up -v`
`./sandbox enter algod`

  </details>
  
  
  <details><summary><h1>L'environnement Algorand </h1></summary>
    
    - Documentation d'Algorand : https://developer.algorand.org/
    
    - AlgoExplorer : https://algoexplorer.io/
  
    - SDK installation : `pip3 install py-algorand-sdk` ou `pip install py-algorand-sdk`
    
    
    
   
