import binascii
from hashlib import sha256
from ast import literal_eval

SALT = "2c212a4a78595929e1eea5294949b0e7"
PASSHASH = "b9a03d0233a641751ec41527c6c55326a9e23cbb07a2803c9bac9626504d7385"

def getHash(passStr):
    salt = SALT
    #string password to byte hex
    passHex = passStr.encode("utf-8").hex()

    #pass + salt join
    passSaltStr = "0x" + str(passHex) + salt
    passSaltStrInt = literal_eval(passSaltStr)
    passSaltHex = hex(passSaltStrInt)[2:]

    #passSalt to hash 
    hash = sha256(bytes.fromhex(passSaltHex)).hexdigest()
    return hash

vokale = "aeiou"
sonder = "(:$_|"
zahlen = "91585"
lines = []
with open('Wortliste_Deutsch.txt') as f:
    lines = f.readlines()

for wort in lines:
    wort = wort.strip()

    firstUpperCaseWord = wort[0].upper() + wort[1].lower() + wort[2:]
    secondUpperCaseWord = wort[0].lower() + wort[1].upper() + wort[2:]
    secondUpperCaseWord1 = wort[0] + wort[1].upper() + wort[2:]

    words = [secondUpperCaseWord1, firstUpperCaseWord, secondUpperCaseWord]

    for word in words:
        for e in range(1,21):
            wort_e = f'{word}{e}'
            for i in range(5):
                wort_c = wort_e.replace(vokale[i], zahlen[i], 1)
                for j in range(5):
                    wort_d = wort_c.replace(vokale[j], sonder[j], 1)
                    if(getHash(wort_d) == PASSHASH):
                        print(wort_d)
                        break
        