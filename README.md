<!-- # LabI-Crypto -->
# Hybrid-Cryptography

Hosting two programs that use an hybrid cryptosystem to encrypt and decrypt. Assymetric encryption (and decryption) uses the RSA algorithm and symmetric encryption (and again, decryption) uses AES on CFB mode. For more on the subject you can check the PDF on the LaTeX folder (though it's in portuguese).

The programs were writen in *Python 2.7* and require PyCrypto in order to properly work. Inside *Sender* and *Receiver* folders there are already RSA keys (used in tests) but for safety reasons be sure to generate your own pair.

### KeysGenerator

Use the program **generateKeys.py** in order to generate a pair of RSA keys (or you can use your own generated pair if you wish). Syntax:

```
python generateKeys.py
```

### Sender

Here you can find the ciphering program. Either edit the code and add for example your private key file name (and path to it), or you will be promped for it at runtime. You can also add the password for your private key but I myself would not advise that. Syntax:

```
python encipher.py <file_name>
```

You can ommit the file name, in which case you will be promped for it at runtime. As the output you will get a *.all file which you can safely send to you recipient.

### Receiver

Here you can find the deciphering program. Again, either edit the code and add your private password file name (and path) or you will be promped for it. This program works as the reverse of the ciphering one, so what you can do with the last you should be able to also do with this one. Syntax:

```
python decipher.py <file_name>
```

As the ouput you will get the deciphered file that was sent to you. A message will also be printed to the terminal that ensures you of the file's authenticity.


By Ricardo Jesus
