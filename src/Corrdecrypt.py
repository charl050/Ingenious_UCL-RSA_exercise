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
                if y == (encrypted_message[i] ** private_key[0]) % (private_key[2]):
                    decrypt += alphabet[y]

        return decrypt

    except:
        return None