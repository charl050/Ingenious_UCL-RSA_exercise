import math
import random

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def keys_generation(length):

    """Génére deux clés, privée et publique,
    Args:
        length (int) : longueur du nombre n
    Returns:
        list : la clé privée (le couple d,e,n), la clé publique (le couple n,e)"""

    try:
        min_number_factor = ""
        max_number_factor = ""

        for i in range(length):
            min_number_factor += str(1)
            max_number_factor += str(9)

        min_number = math.ceil(math.sqrt(int(min_number_factor)))
        max_number = math.ceil(math.sqrt(int(max_number_factor)))

        primes = [i for i in range(min_number,max_number) if isPrime(i)]
        p = random.choice(primes)
        q = random.choice(primes)
        n = p*q

        e = random.randint(min_number, max_number)
        while math.gcd(e,(p-1)*(q-1)) != 1:
            e = random.randint(min_number, max_number)

        while True:
            i = random.randrange(1,(p-1)*(q-1))
            if 1 == (e*i)%((p-1)*(q-1)):
                    d = i
                    break

        public_key = [n,e]
        private_key = [d,e,n]

        return [private_key, public_key]
    except:
        return None

        
        