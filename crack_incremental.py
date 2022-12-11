import string
import sys
import time
import hashlib
import argparse
import atexit


def crack_dict(md5, file):
    try:
        trouve = False
        ofile = open(file, "r")
        for mot in ofile.readlines():
            mot = mot.strip("\n")
            hashmd5 = hashlib.md5(mot.encode("utf8")).hexdigest()
            if hashmd5 == md5:
                print("Mot de passe trouvé : " + str(mot) + " (" + hashmd5 + ")")
                trouve = True
        if not trouve:
            print("Mot de passe non trouvé :(")
        ofile.close()
    except FileNotFoundError:
        print("Erreur ; nom de dossier ou fichier introuvable !")
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)


def crack_incr(md5, length, currpass=[]):
    lettres = string.ascii_letters  # .printable
    if length >= 1:
        if len(currpass) == 0:
            currpass = ['a' for _ in range(length)]
            crack_incr(md5, length, currpass)
        else:
            for c in lettres:
                currpass[length - 1] = c
                print("Trying : " + "".join(currpass))
                if hashlib.md5("".join(currpass).encode("utf8")).hexdigest() == md5:
                    print("PASSWORD FOUND! " + "".join(currpass))
                else:
                    crack_incr(md5, length - 1, currpass)


def display_time():
    print("Durée : " + str(time.time() - debut) + " secondes")


parser = argparse.ArgumentParser(description="Password Cracker")
parser.add_argument("-f", "--file", dest="file", help="Path of the dictionary file", required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Generate MD5 hash of password", required=False)
parser.add_argument("-md5", dest="md5", help="Hashed password (MD5)", required=False)
parser.add_argument("-l", dest="plength", help="Password length", required=False, type=int)

args = parser.parse_args()

debut = time.time()
atexit.register(display_time)

if args.md5:
    print("[CRACKING HASH " + args.md5 + "]")
    if args.file:
        print("[USING DICTIONARY FILE " + args.file + "]")
        crack_dict(args.md5, args.file)
    elif args.plength:
        print("[USING INCREMENTAL MOD FOR " + str(args.plength) + " letter(s)")
        crack_incr(args.md5, args.plength)
    else:
        print("Please choose either -f or -l argument")
else:
    print("MD5 HASH NOT PROVIDED")

if args.gen:
    print("[MD5 HASH OF " + args.gen + " : " + hashlib.md5(args.gen.encode("utf8")).hexdigest())
