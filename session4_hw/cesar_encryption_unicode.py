def cesar_encrypt(input_str, key):
    result = ''
    for i in input_str:
        rotation = ord(i) + key
        result += chr(rotation)
    return result


plain_text = 'Cesar The Grea8T@'
key = 4
encrypted_str = cesar_encrypt(plain_text, key)
print(encrypted_str)


def cesar_decrypt(enc_str, key):
    result = ''
    for i in enc_str:
        rotation = ord(i) - key
        result += chr(rotation)
    return result


decrypted_str = cesar_decrypt(encrypted_str, key)
print(decrypted_str)
