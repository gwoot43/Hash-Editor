import hashlib

while True:
    with open('filename','rb') as f:
        bytes_fake = f.read() 
        hash_fake = hashlib.sha256(bytes_fake).hexdigest()
    with open('filename','rb') as f:
        bytes_real = f.read() 
        hash_real = hashlib.sha256(bytes_real).hexdigest()
    if hash_fake[-2:] != hash_real[-2:]:
        with open ('filename','a') as f:
            f.write(' ')
            continue
    else:
        print('Done!')
        break



