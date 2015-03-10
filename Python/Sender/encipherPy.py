import os, sys, zipfile
from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Signature import PKCS1_v1_5


# Define Public and Private key names!

# Sender's private key:
priKey = "A_PrivateKey.pem"
# Receiver's public key:
pubKey = "B_PublicKey.pem"

# File name to encrypt
f_name = ""

def usage():
    print "python encipherPy.py <File_Name>"


def sigGenerator(priKey_fname, f_name):
    # Opening and reading file to encrypt

    f = open(f_name, "r")
    buffer = f.read()
    f.close()

    # Creating Hash of the file. Using SHA-256 (there was a problem using SHA-512)

    h = SHA256.new(buffer)

    # Reading PrivateKey to sign file with

    keyPair = RSA.importKey(open(priKey_fname, "r").read())
    keySigner = PKCS1_v1_5.new(keyPair)

    # Saving Signature to *.sig File

    f = open(f_name.split('.')[0] + ".sig", "w")
    f.write(keySigner.sign(h))
    f.close()


def keyGenerator(pubKey_fname, f_name, iv):
    # Generating 1024 random bits, and creating SHA-256 (for 32 bits compatibility with AES)

    h = SHA256.new(str(random.getrandbits(1024)))

    # Reading PublicKey to encrypt AES key with

    keyPair = RSA.importKey(open(pubKey_fname, "r").read())
    keyCipher = PKCS1_OAEP.new(keyPair.publickey())

    # Saving encrypted key to *.key File

    f = open(f_name.split('.')[0] + ".key", "w")
    f.write(iv + keyCipher.encrypt(h.digest()))
    f.close()

    # Returning generated key to encrypt file with

    return h.digest()


def encipher(keyA_fname, keyB_fname, f_name):
    # Opening file to encrypt in binary mode

    f = open(f_name, "rb")
    buffer = f.read()
    f.close()

    # Generating file's Signature (and saving it)

    sigGenerator(keyA_fname, f_name)

    # Generating initializing vector for AES Encryption (there were problems when using different AES modes)
    # Needs to be saved in, for example, .key File!!!

    iv = Random.new().read(AES.block_size)

    # Generating symmetric key for use (and saving it)

    k = keyGenerator(keyB_fname, f_name, iv)

    # Encrypting and saving result to *.bin File. Using CFB mode

    keyCipher = AES.new(str(k), AES.MODE_CFB, iv)
    f = open(f_name.split('.')[0] + ".bin", "wb")
    f.write(keyCipher.encrypt(buffer))
    f.close()


def auxFilesZip(sig, key, bin):
    # Opening file to contain all bin, sig and key files

    f = zipfile.ZipFile(bin.split('.')[0] + ".all", "w")

    # Writing each of the arguments to the created file

    f.write(sig)
    f.write(key)
    f.write(bin)

    # Closing the file

    f.close()

    # Running clean up to the bin, sig and key files

    cleanUp(sig, key, bin)


def cleanUp(sig, key, bin):
    # Deleting each of the files generated during ciphering

    os.remove(sig)
    os.remove(key)
    os.remove(bin)


def checkFiles(f_name, pubKey, priKey):
    # Checking for encrypting file's existence and access

    if not os.path.isfile(f_name) or not os.access(f_name, os.R_OK):
        print "Invalid file to encrypt. Aborting..."
        sys.exit(1)

    # Checking for each of the files to create existence and, in case they exist, if they are writable

    else:
        s = f_name.split('.')[0]
        if os.path.isfile(s + ".sig") and not os.access(s + ".sig", os.W_OK):
            print "Can't create temporary file: *.bin. Aborting..."
            sys.exit(2)
        if os.path.isfile(s + ".key") and not os.access(s + ".key", os.W_OK):
            print "Can't create temporary file: *.key. Aborting..."
            sys.exit(3)
        if os.path.isfile(s + ".bin") and not os.access(s + ".bin", os.W_OK):
            print "Can't create temporary file: *.bin. Aborting..."
            sys.exit(4)
        if os.path.isfile(s + ".all") and not os.access(s + ".all", os.W_OK):
            print "Can't create output file. Aborting..."
            sys.exit(5)

    # Checking for public key's existence and access

    if not os.path.isfile(pubKey) or not os.access(pubKey, os.R_OK):
        print "Invalid public key file. Aborting..."
        sys.exit(6)

    # Checking for private key's existence and access

    if not os.path.isfile(priKey) or not os.access(priKey, os.R_OK):
        print "Invalid private key file. Aborting..."
        sys.exit(7)


# Gathering encrypting file name

if len(sys.argv) > 2:
    usage()
elif len(sys.argv) == 1:
    print "File name:"
    f_name = raw_input(">>> ")
else:
    f_name = sys.argv[1]

# Gathering keys names

if priKey == "":
    print "Sender's private key file name:"
    priKey = raw_input(">>> ")
if pubKey == "":
    print "Receiver's public key file name:"
    pubKey = raw_input(">>> ")

# Running checks to files

checkFiles(f_name, pubKey, priKey)

# Ciphering file (and generating all auxiliary files)

encipher(priKey, pubKey, f_name)

# Generating output file and clean up

auxFilesZip(f_name.split('.')[0] + ".sig", f_name.split('.')[0] + ".key", f_name.split('.')[0] + ".bin")
