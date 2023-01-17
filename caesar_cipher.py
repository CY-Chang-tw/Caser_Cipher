#Owen @ pyCharm_2022/10/18.
#HW02-Q6_7111056228

# ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
# len(ASCII) = 95



def encrypt(text, key):
    cipherText = ""
    for letter in text:
        if letter.isupper():

            letter_index = ord(letter) - ord('A')

            offset_index = (letter_index + key) % 26
            shifted_ascii = offset_index + ord('A')

            converted_text = chr(shifted_ascii)
            cipherText = cipherText + converted_text
        else:
            letter_index = ord(letter) - ord('a')

            offset_index = (letter_index + key) % 26
            shifted_ascii = offset_index + ord('a')

            converted_text = chr(shifted_ascii)
            cipherText = cipherText + converted_text
    print('Encrypted text: ' + cipherText)
    print()



def decrypt(text, key):
    plainText = ""
    key = 26
    for letter in text:
        if letter.isupper():

            letter_index = ord(letter) - ord('A')

            offset_index = (letter_index + key) % 26
            shifted_ascii = offset_index + ord('A')

            converted_text = chr(shifted_ascii)
            plainText = plainText + converted_text
        else:
            letter_index = ord(letter) - ord('a')

            offset_index = (letter_index + key) % 26
            shifted_ascii = offset_index + ord('a')

            converted_text = chr(shifted_ascii)
            plainText = plainText + converted_text
    print('Encrypted text: ' + plainText)
    print()


if __name__ == '__main__':
    text = input('Enter the text: ')
    key = input('Enter the key: ')
    key = int(key)
    print()
    if key >= 26:
        while 1:
            print('Please input the key under 26.')
            key = input('Enter the key: ')
            key = int(key)
            print()
            if key < 26:
                break
    encrypt(text, key)
    decrypt(text, key)


