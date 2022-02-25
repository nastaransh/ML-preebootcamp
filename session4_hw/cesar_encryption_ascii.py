def cesar_encrypt(input_str, key):
    from string import ascii_letters
    result = ''
    input_str.lower()
    for i in input_str:
        if i not in ascii_letters:
            result += i
        else:
            rotation = (ascii_letters.index(i)) + key
            if rotation > 25:
                rotation -= 26
            result += ascii_letters[rotation]
    return result


def cesar_decrypt(enc_str, key):
    from string import ascii_letters
    result = ''
    for i in enc_str:
        if i not in ascii_letters:
            result += i
        else:
            rotation = (ascii_letters.index(i)) - key
            if rotation < 0:
                rotation += 26
            result += ascii_letters[rotation]
    return result


plain_txt = 'abcx d'
key = 3
encrypt_str = cesar_encrypt(plain_txt, key)
print(encrypt_str)
decrypt_str = cesar_decrypt(encrypt_str, key)
print(decrypt_str)