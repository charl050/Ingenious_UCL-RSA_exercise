import math
import random


# Vérifie si un nombre est premier
def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

# Génere un couple de nombre premiers
def Prime_generation():
    p = random.randint(1,1000)
    while not isPrime(p):
        p = random.randint(1,1000)
    q = random.randint(1,1000)
    while not isPrime(q):
        q = random.randint(1,1000)
    return p,q



def keys_generation(p, q):

    """Génére deux clés, privée et publique, avec un couple de nombres premiers p, q donné
    Args:
        p (int) : nombre premier
        q (int) : nombre premier
    Returns:
        list : la clé privée (le couple d,e,n), la clé publique (le couple n,e)"""
    
    try:
        # Calcul du n
        n = p*q 

        if q < p:
            r = q
        else:
            r = p
        
        # Calcul du e
        e = random.randint(r, (p-1)*(q-1))
        while math.gcd(e,(p-1)*(q-1)) != 1:
            e = random.randint(r, (p-1)*(q-1))
        
        # Calcul du d
        while True:
            i = random.randrange(r,(p-1)*(q-1))
            if 1 == (e*i)%((p-1)*(q-1)):
                    d = i
                    break
        
        # Création des clés
        public_key = [n,e]
        private_key = [d,e,n]

        return [private_key, public_key]
    # Si une entrée est incorrecte, retourne None
    except:
        return None




def encryption(message, public_key):
    """Chiffre un message donné avec une clé publique,
    Args:
        message (str) : message à chiffrer
        public_key (list) : la clé publiqe
    Returns:
        list : le message chiffré"""
    try:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        encrypted = []
        # Transforme les lettres en minuscules pour les comparer à la liste de l'alphabet
        message = message.lower()
        for i in range(len(message)):
            for y in alphabet:
                if y == message[i]:
                    # Chiffre avec la méthode, et ajoute le bloc à la liste encrypted
                    encrypted.append( (alphabet.index(y) ** public_key[1]) % public_key[0])
        return encrypted
    except:
        return None




def decrypt(encrypted_message, private_key):
    """Déchiffre un message donné avec une clé privé,
    Args:
        message (list) : message à déchiffrer
        private_key (list) : la clé privée
    Returns:
        str : le message déchiffré"""
    try:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        decrypt = ""
        for i in range(len(encrypted_message)):
            for y in range(len(alphabet)):
                # Déchiffre chaque bloc selon la méthode, et ajoute la lettre dans le string decrypt
                if y == (encrypted_message[i] ** private_key[0]) % (private_key[2]):
                    decrypt += alphabet[y]

        return decrypt

    except:
        return None