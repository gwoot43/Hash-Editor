import hashlib

#print(hash_fake)
#eightdigitsfake = hash_fake[-8:]   #each SHA256 has 64 characters in its hash value, last 8 characters of the hash 
#print (eightdigitsfake)
hash_real = '6e42cef71afde6d8d2926d9e097152a6bf579f8f50adec6421924f414fe66de1'
#eightdigitsreal = hash_real[-8:]
#print(eightdigitsreal)


while True:
    with open('confession_fake.txt','rb') as f:
        bytes = f.read() 
        hash_fake = hashlib.sha256(bytes).hexdigest()
    if hash_fake[-8:] != hash_real[-8:]:
        with open ('confession_fake.txt','a') as f:
            f.write(' ')
            continue

            
#Attempt 2
import hashlib

while True:
    with open('confession_fake.txt','rb') as f:
        bytes_fake = f.read() 
        hash_fake = hashlib.sha256(bytes_fake).hexdigest()
    with open('confession_real.txt','rb') as f:
        bytes_real = f.read() 
        hash_real = hashlib.sha256(bytes_real).hexdigest()
    if hash_fake[-5:] != hash_real[-5:]:
        with open ('confession_fake.txt','a') as f:
            f.write(' ')
            continue




