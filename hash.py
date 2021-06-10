import hashlib
Birthday attack attempt
while True:
    with open('filename1','rb') as f:
        bytes_fake = f.read() 
        hash_fake = hashlib.sha256(bytes_fake).hexdigest()
    with open('filename2','rb') as f:
        bytes_real = f.read() 
        hash_real = hashlib.sha256(bytes_real).hexdigest()
    if hash_fake[-2:] != hash_real[-2:]:
        with open ('filename2','a') as f:
            f.write(' ')
            continue
    else:
        print('Done!')
        break



