# Workshop2 Algorand
Bienvenue pour ce deuxième workshop ;) 

🧵 Aujourd'hui nous allons nous concentrer sur une blockchain en particulier : Algorand.

Nous verrons comment : 

✔️ Configurer l'environnement de programmation Algorand

✔️ Créer un compte Algorand 

✔️ Effectuer notre première transaction



## Quelques termes techniques à éclairer avant de commencer le workshop 
📌 Smart contract :  Un smart contract est un contrat automatisé qui utilise la technologie de la blockchain pour s'exécuter de manière autonome. Il permet de gérer des transactions électroniques sans avoir besoin d'intermédiaires.

📌 SDK : Softaware Development Kit - c'est une collection d'outils. Les SDK sont comme des boîtes à outils pour construire des logiciels. 

📌 TestNet vs Mainnet : La principale différence entre le testnet et le mainnet est que le testnet est un réseau de test et de développement, tandis que le mainnet est le réseau en production. Le testnet est un réseau public qui permet aux développeurs de tester leurs applications, contrats intelligents et autres fonctionnalités sans risquer des actifs réels. Les transactions réelles sont traitées sur le mainnet et c'est là que les tokens Algorand sont utilisés. 


<details>
  <summary>
  <h1>🔧 Installation des logiciels principaux</h1>
  </summary>
  
  - Installation de Git
  
  Pour windows : https://git-scm.com/download/win
  Vous pouvez retrouver la version de votre système, en tapant dans votre barre de recherche de votre barre de tâche " A propos de votre PC", et vous retrouverez la version de votre système dans "type du système". Cela vous permettra de savoir si vous avez un processeur de 32-bit ou 64-bit. 
  
  Pour Mac: `git --version`
  Si git est déjà installé vous trouverez la version, sinon vous trouverez les instructions pour installer le logiciel. 

  - Installation de python 3: https://www.python.org/downloads/
  
  - Installation de Docker : `https://docs.docker.com/compose/install/`
 

  </details>
  
  
  <details><summary><h1>🌍 L'environnement Algorand </h1></summary>
   
  - Installation de sandbox (clône de repo par github Desktop) :
  Nous pouvons désormais commencer à jouer avec les commandes github : 
  ~~~
  git clone https://github.com/algorand/sandbox.git
  ~~~

( Ajout de code dans le fichier sandbox/docker-compose sous les ports ) 
~~~
volumes:
- type: bind
  source: ../
  target: /data 
~~~

  - Initialisation de sandbox ( au sein du terminal git) 
~~~
cd sandbox
./sandbox up testnet
~~~
  
  - Documentation d'Algorand : `https://developer.algorand.org/`
  
  - AlgoExplorer : `https://algoexplorer.io/`
  
  - SDK installation : `pip3 install py-algorand-sdk` ou `pip install py-algorand-sdk`
  
  - Dispenser Algorand (permet de récupérer des jetons/ faucet) : `https://dispenser.testnet.aws.algodev.network/`
 </details> 
 
 
 <details><summary><h1>💸 Première transaction</h1></summary>
 
 
### Création d'un compte Algorand et ajout de faucet dans notre compte

👉🏽 Dans le fichier sandbox, créez un nouveau fichier, nommez le (compte_algorand.py), puis collez le bout de code. Il nous permettra de générer des clés privées et public afin de créer notre compte Algorand.


~~~
from algosdk import account, mnemonic

def generate_algorand_keypair():
    cle_prive, addresse = account.generate_account()
    print("Mon adresse: {}".format(addresse))
    print("Ma clé privée: {}".format(cle_prive))
    print("Ma phrase mnémonique: {}".format(mnemonic.from_private_key(cle_prive)))

generate_algorand_keypair()

~~~

Puis sur le terminal, faites appel au fichier nouvellement créée. Cela permettra de générer le nouveau compte. Sur un nouveau fichier, ou en commentaire (chaque ligne précédé de #), copier-coller les données de votre nouveau compte.  : 
~~~
python3 compte_algorand.py 
~~~

La spécialité de la blockchain est que chaque transaction nécessite provoque des gas fees. Notre wallet sera celui qui valide les transactions, pour cela, nous devons avoir des faucets ( qui est en vérité de la fausse monnaie ), nous permettant d'intéragir avec la blockchain. 

👉 Allons sur le dispenser algorand, et avec l'adresse précédemment générée, nous pouvons nous procurer des faucets Algorand. Vous pouvez vérifier que la transaction c'est bien effectué dans l'explorateur de bloc. 
    
### Création de la première transaction 

Dans le même fichier précédement créé, nous rajouterons une nouvelle fonction permettant de créer la première transaction. Vous pouvez commenter la fonction précédente en séléctionnant la partie et avec 'CTRL + /' ou 'COMMAND + /'. 

~~~
#nouvelle en-tête et librairie 
from algosdk.v2client import algod
from algosdk import transaction
from algosdk import constants
import json
import base64

def exemple_de_premiere_transaction(ma_cle_prive, mon_adresse):
    # permet d'initialiser le client algod 
    algod_addresse = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_addresse)
~~~

Toujours dans la même fonction, nous créerons une variable permettant de récupérer les informations du compte. 
~~~
    # permet de récupérer les informations sur le compte 
    info_compte_initial = algod_client.account_info(mon_adresse)
    print("Voici la balance de mon compte: {} microAlgos".format(info_compte_initial.get('amount')) + "\n")
~~~

L'étape suivante consiste à ajouter du code dans notre fonction. Cette partie permet d'initialiser une transaction. 
~~~
    # construction de la transaction
    parametre = algod_client.suggested_params()
    #pour utiliser les données de la transaction avec les gas fess, tu peux commenter la ligne suivante
    parametre.flat_fee = True
    parametre.fee = constants.MIN_TXN_FEE 
    destination = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    note = "Hello World".encode()
    montant = 1000000
    transaction_non_signe = transaction.PaymentTxn(mon_adresse, parametre, destination, montant, None, note)
~~~

Puis, nous devons signer notre transaction : 
~~~
    # signature de transaction
    transaction_signe = transaction_non_signe.sign(ma_cle_prive)
~~~

La dernière étape consiste à soumettre notre transaction dans la blockchain algorand
~~~
    #soumettre la transaction
    txid = algod_client.send_transaction(transaction_signe)
    print("La transaction est passée avec succée: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
        return

    print("Information sur la transaction: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Les notes décodées: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("La balance initial du compte: {} microAlgos".format(info_compte_initial.get('montant')) )
    print("Montant transféré: {} microAlgos".format(montant) )    
    print("Frais: {} microAlgos".format(parametre.fee) ) 


    infos_compte_final = algod_client.account_info(mon_adresse)
    print("La balance finale du compte : {} microAlgos".format(infos_compte_final.get('montant')) + "\n")
~~~

Enfin, nous devons faire appel à notre fonction avec les paramétres définit. 
Remplacer, 'ICI MA CLE PRIVEE' et 'ICI MON ADRESSE', par vos informations précédemment généré. 

~~~
exemple_de_premiere_transaction('ICI MA CLE PRIVEE', 'ICI MON ADRESSE')
~~~


