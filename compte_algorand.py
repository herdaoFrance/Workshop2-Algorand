from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk import transaction
from algosdk import constants
import json
import base64

def generate_algorand_keypair():
    cle_prive, addresse = account.generate_account()
    print("Mon adresse: {}".format(addresse))
    print("Ma clé privée: {}".format(cle_prive))
    print("Ma phrase mnémonique: {}".format(mnemonic.from_private_key(cle_prive)))

#generate_algorand_keypair()

#My address: M2B6ANNLQS3KCWCJQOKDTY3SXK3TLJJJ5BAZ6IK4QSIOP7ATB7OTOSITNU
#My private key: hklcjCl+RrIPJXTFXxKc8kS3Z4L00BG1OpfA6Zq8VRVmg+A1q4S2oVhJg5Q543K6tzWlKehBnyFchJDn/BMP3Q==
#My passphrase: cotton illness shiver tip mind uncle chronic injury weather enact evoke execute hub okay piano special peasant turn entire orchard cupboard hundred primary abandon material


def exemple_de_premiere_transaction(ma_cle_prive, my_adress):
    # permet d'initialiser le client algod 
    algod_addresse = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_addresse)

    print("Mon adresse: {}".format(my_adress))

    # permet de récupérer les informations sur le compte 
    account_info = algod_client.account_info(my_adress)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")


    # construction de la transaction
    parametre = algod_client.suggested_params()
    #pour utiliser les données de la transaction avec les gas fess, tu peux commenter la ligne suivante
    parametre.flat_fee = True
    parametre.fee = constants.MIN_TXN_FEE 
    destination = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    note = "Hello World".encode()
    montant = 1000000
    transaction_non_signe = transaction.PaymentTxn(my_adress, parametre, destination, montant, None, note)


    # signature de transaction
    transaction_signe = transaction_non_signe.sign(ma_cle_prive)


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
    print("La balance initial du compte: {} microAlgos".format(account_info.get('montant')) )
    print("Montant transféré: {} microAlgos".format(montant) )    
    print("Frais: {} microAlgos".format(parametre.fee) ) 


    account_info = algod_client.account_info(my_adress)
    print("La balance finale du compte : {} microAlgos".format(account_info.get('montant')) + "\n")


exemple_de_premiere_transaction("hklcjCl+RrIPJXTFXxKc8kS3Z4L00BG1OpfA6Zq8VRVmg+A1q4S2oVhJg5Q543K6tzWlKehBnyFchJDn/BMP3Q==","M2B6ANNLQS3KCWCJQOKDTY3SXK3TLJJJ5BAZ6IK4QSIOP7ATB7OTOSITNU")

    