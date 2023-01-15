# Workshop-2 Algorand-Blockchain-
Bienvenue pour ce deuxième workshop ;) 

🧵 Aujourd'hui nous allons nous concentrer sur une blockchain en particulier : Algorand. Voyons comment configurer notre environnement pour ce workshop, et nous commencerons à déployer des smart contracts sur cette blockchain 



## Quelques termes techniques à éclairer avant de commencer le workshop 
📌 Smart contract :  

📌


<details>
  <summary><h1>Installation des logiciels principaux</h1></summary>
  
  Installation de python 3
`brew install python3`

  Install sandbox
`git clone https://github.com/algorand/sandbox.git`

## Changes in configuration for running sandbox within a propject folder
```
volumes:
- type: bind
  source: ../
  target: /data
```

  Initialisation de sandbox
`./sandbox up -v`
`./sandbox enter algod`
