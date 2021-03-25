import hashlib

while True:
    with open('confession_fake.txt','rb') as f:
        bytes_fake = f.read() 
        hash_fake = hashlib.sha256(bytes_fake).hexdigest()
    with open('confession_real.txt','rb') as f:
        bytes_real = f.read() 
        hash_real = hashlib.sha256(bytes_real).hexdigest()
    if hash_fake[-2:] != hash_real[-2:]:
        with open ('confession_fake.txt','a') as f:
            f.write(' ')
            continue
    else:
        print('Done!')
        break



