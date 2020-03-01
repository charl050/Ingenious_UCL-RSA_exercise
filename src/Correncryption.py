def encryption(message, public_key):

    """Chiffre un message donné avec une clé publique,
    Args:
        message (str) : message à chiffrer
        public_key (list) : la clé publique
    Returns:
        list : les blocs chiffrés du message"""
    try:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        encrypted = []
        message = message.lower()
        for i in range(len(message)):
            for y in alphabet:
                if y == message[i]:
                    encrypted.append( (alphabet.index(y) ** public_key[1]) % public_key[0])
        return encrypted
    except:
        return None