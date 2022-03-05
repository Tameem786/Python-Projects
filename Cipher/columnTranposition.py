def split_seq(str, length):
    return [list(str[i:i+length]) for i in range(0, len(str), length)]

def encode(key, plainText):
    order = {
        int(val):num for num, val in enumerate(key)
    }

    cipherText = ''

    for index in sorted(order.keys()):
        for part in split_seq(plainText, len(key)):
            try: cipherText += part[order[index]]
            except IndexError:
                continue
    
    return cipherText

print(encode('3214', 'I Love Programming'))

