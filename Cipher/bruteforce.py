import string

def generate(message=''):
    symbols = string.ascii_letters + string.punctuation + string.digits
    for times in range(len(symbols)):
        cipherText = ''
        for word in message:
            if word in symbols:
                index = symbols.find(word) - times
                if index < 0:
                    index += len(symbols)
                cipherText += symbols[index]
            else:
                cipherText += word
        print(f"Attempt {times}: {cipherText}")


generate(message='U my ,mymz')

