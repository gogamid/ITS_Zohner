import hashlib
import sys
import time
from art import tprint

m = 0
counter = 0
iter_it = 0
same_hash = False
hash_value_array = []

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x- (b // a) * y, y)

def modinv(a,m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular Inverse doesnt exist, CHECK WRONG INPUT!");
    else:
        return x % m
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

tprint("The ZohnerDecrypter", font="graffity")
tprint("  by  fancyStuff90", font="graffity")
z1 = 0
confirm = False
while confirm is False:
    z1 = int(input("\n\nEnter the value from z1 now:(without the point please):"))

    print(f"\nEntered Value is:\n"
          f"-->Value of z1: {z1}")

    confirm = yes_or_no("Please Type \"y\" if that is the correct value:")
    if confirm is True:
        print("Continue...")
        time.sleep(5)
    if confirm is False:
        print("Enter values again....")

print("\n-------------------------------------------------------------------------------------------------\n")

print(f"Entered z1 value: {z1} \n"
      f"Starting to calculate Hash-Values for messages soon....\n\n")

print("\n\n-------------------------------------------------------------------------------------------------\n\n")

while iter_it < 3000000:
    convert_it = iter_it + int(z1)
    calculated_sha_value = int.from_bytes(hashlib.sha256(bytearray(convert_it.to_bytes(32, sys.byteorder))).digest()[: 5], 'little') # 40 - bit int
    hash_value_array.append(calculated_sha_value)
    print(f"Processing and Saving Hash- Value of Message [{iter_it}] of [3.000.000]")
    iter_it += 1

print(f"Processing of Hash- Values finished.")

print("-------------------------------------------------------------------------------------------------")
print("Comparing saved Values on Same Values... Starting ...")

hash_value_set = set(hash_value_array)
contains_duplicates = len(hash_value_set) != len(hash_value_array)
print(f"SetArray- Length: [{len(hash_value_set)}] vs. ArrayLength: [{len(hash_value_array)}]")

safe_index1 = 0
safe_index2 = 0

if contains_duplicates is True:
    print("Contains Duplicates!")
    print("Identifying Duplicates...")
    counter_outer = 110

    idx = {}
    for i, sig in enumerate(hash_value_array):
        idx.setdefault(sig, []).append(i)

    for sig, v in idx.items():
        if len(v) > 1:
            safe_index1 = v[0]
            safe_index2 = v[1]
            print(f'Duplicated Hash- Value found: {sig} on Messages: {safe_index1} and {safe_index2}')


print("-------------------------------------------------------------------------------------------------")

print(f"\nThe duplicated Messages are: {safe_index1} and {safe_index2}.\n\nNow grab your Terminal, communicate to Zohner- Docker with ncat and type the following:\nTask-ID: 5A\nStudent- ID: [Your ID]\nMessage: \"{safe_index1}\"")

confirm = False
while confirm is not True:
    confirm = yes_or_no("Please Type \"y\" if you have done your Task")
    if confirm is True:
        print("Continue...")
        time.sleep(5)
    if confirm is False:
        print("Dude, just do that Zohner thing! Troll....")

g = 0
p = 0
q = 0

s1 = 0
r1 = 0
s2 = 0
r2 = 0

confirm = False
while confirm is False:
    g = int(input("Enter the Value of \"Generator g\" (without the point please)"))
    p = int(input("Enter the Value of \"Prime p\" (without the point please)"))
    q = int(input("Enter the Value of \"Prime q\" (without the point please)"))
    s1 = int(input("Enter the Value of \"Signature value s\" (without the point please)"))
    r1 = int(input("Enter the Value of \"Signature value r\" (without the point please)"))

    print(f"Entered Values are:\n-->Generator g: {g}\n\n-->Prime p: {p}\n\n-->Prime q: {q}\n\n"
          f"-->Signature value s: {s1}\n\n-->Signature value r: {r1}\n\n")

    confirm = yes_or_no("Please Type \"y\" if you have done your Task\n")
    if confirm is True:
        print("Continue...")
        time.sleep(5)
    if confirm is False:
        print("Enter values again....")
print("\n-------------------------------------------------------------------------------------------------\n")

print(f"Now grab your Terminal again, communicate to Zohner- Docker with ncat and type the following:\nTask-ID: 5A\nStudent- ID: [Your ID]\nMessage: \"{safe_index2}\"")

confirm = False
while confirm is not True:
    confirm = yes_or_no("Please Type \"y\" if you have done your Task")
    if confirm is True:
        print("Continue...")
        time.sleep(5)
    if confirm is False:
        print("Dude, just do that Zohner thing! Troll....")

confirm = False
while confirm is False:
    s2 = int(input("Enter the Value of \"Signature value s\" (without the point please)"))
    r2 = int(input("Enter the Value of \"Signature value r\" (without the point please)"))

    print(f"Entered Values are:\n"
          f"-->Signature value s: {s1}\n-->Signature value r: {r1}")

    confirm = yes_or_no("Please Type \"y\" if you have done your Task")
    if confirm is True:
        print("Continue...")
        time.sleep(5)
    if confirm is False:
        print("Enter values again....")
print("-------------------------------------------------------------------------------------------------")
print("All necessary data is there - start processing....")

print("-------------------------------------------------------------------------------------------------")
print("Starting calculating nonce K...")

sD = (s1 - s2) % q
mD = (safe_index1 - safe_index2) % q
k = (mD * modinv(sD,q)) % q

print(f"K is = {k}")

print("Checking if K is correct...")

#code written  by fancyStuff90
r_k_check = pow(g,k,p) % q

print(f"Comparing r with r = (g^k mod p) mod q..")

print(f"Value of r is: {r1} \n"
      f"------------VS----------\n"
      f"Value of r = (g^k mod p) mod q = {r_k_check}")

if r1 == r_k_check:
    print(f"Result: SAME VALUE, K is correct calculated. K = {k}")
else:
    print("Something went wrong, please start the program again and give the correct input values!")
    exit()

print("\n\nContinue...")

print("-------------------------------------------------------------------------------------------------")
print(f"Starting calculating Secret/Private Key X...")
time.sleep(5)
x = modinv(r1,q) * ((k * s1) - safe_index1) % q

print("X is Calculated.")


print(f"Calculated Private Key X Value: {x}\nChecking if X Value is correct...")
print("Checking if sCalculated = (k^-1 * (M1 + r * x)) % q = s1 ")

sCalculated = (modinv(k,q) * (safe_index1 + r1 * x)) % q

print(f"sCalculated = {sCalculated}\n"
      f"-----------VS-------------\n"
      f"s1 = {s1}")

if s1 == sCalculated:
    print(f"Result: SAME VALUE, x is correct calculated. x = {x}")
else:
    print("Something went wrong, please start the program again and give the correct input values!")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")

print(f"JOB DONE - \n-->Go to terminal, \n-->ncat Zohner Docker, \n-->type Task-ID: 5AV, \n-->Your Student- ID and \n-->Solution: {x}")

print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
