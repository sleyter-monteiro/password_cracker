import random
import time
import string
import hashlib
import sys
import argparse


parser = argparse.ArgumentParser(description="Password Cracker")
parser.add_argument("-f", "--file", dest="file", help="Path of the dictionnary file", required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Generation de Mot de Passe Hashé", required=False)
parser.add_argument("-md5", dest="md5", help="Mot de Passe Hashé (MD5)", required=False)

args = parser.parse_args


"""
mot_de_passe_md5 = hashlib.md5(mot_de_passe.encode("utf8")).hexdigest()
"""

def crack_dict(md5, file):
    try:    
        trouve = False
        for mot in file.readlines():
            mot = mot.strip("\n").encode("utf8")
            hashmd5 = hashlib.md5(mot).hexdigest()
            if hashmd5 == md5:
                print("Mot de passe trouvé : " + str(mot) + " (" + hashmd5 + ") ")
                trouve = True 
        if not trouve:
            print("Mot de passe non trouvé :(")    
    except FileNotFoundError: 
        print("Erreur : fichier ou dossier introuvable !") 
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)


debut = time.time()
crack_dict()
print("Durée : " + str(time.time() - debut) + " secondes")

     