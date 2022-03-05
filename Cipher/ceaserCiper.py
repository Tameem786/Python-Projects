import string

def generate(encrypt=False, decrypt=False, plainText='', key = 1):
    symbols = string.ascii_letters + string.punctuation + string.digits
    cipherText = ''
    for word in plainText:
        if word in symbols:
            if encrypt:
                index = symbols.find(word) + key
            elif decrypt:
                index = symbols.find(word) - key

            if index >= len(symbols):
                index -= len(symbols)
            elif index < 0:
                index += len(symbols)

            cipherText += symbols[index]

        else:
            cipherText += word

    return cipherText



choice = int(input('What do want ot do? (1. Encrypt 2. Decrypt) '))

if choice == 1:
    text = input('Enter you message to encrypt: ')
    k = int(input('Enter a key (1-20): '))
    print(generate(encrypt=True, plainText=text, key=k))
elif choice == 2:
    text = input('Enter you message to decrypt: ')
    k = int(input('Enter the key (1-20): '))
    print(generate(decrypt=True, plainText=text, key=k))
else:
    print('Enter valid input')


