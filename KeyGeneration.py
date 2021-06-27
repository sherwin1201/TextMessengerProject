import random

PG = (23,7)  #Public key

def generatePrivateKey():               # Generates private key 
   return random.randrange(1,9999)       # for client

def generatePublicKey(privatekey):          # Generates a public key for the client
    return (PG[1]**privatekey) % PG[0]      # from the global public key (PG)

def generateSharedKey(publickey, privatekey):       # Generates a shared key for the clients by mixing 
    return publickey**privatekey % PG[0]            # public key of each client and private key of that client

def make16BitKey(sharedKey):                # Generates a 16 byte key from the
    key = []                                # shared key using the following
    for i in range(16):                     # algorithm (self-developed)
        key.append(sharedKey ^ (i+1)) 

    return key


# BobsPrivateKey = generatePrivateKey()
# AlicesPrivateKey = generatePrivateKey()

# BobsPublicKey = generatePublicKey(BobsPrivateKey)
# AlicesPublicKey = generatePublicKey(AlicesPrivateKey)

# BobsSharedKey = generateSharedKey(AlicesPublicKey, BobsPrivateKey)
# AlicesSharedKey = generateSharedKey(BobsPublicKey, AlicesPrivateKey)

# BobsKey = make16BitKey(BobsSharedKey)
# AlicesKey = make16BitKey(AlicesSharedKey)

# print(BobsKey, AlicesKey)