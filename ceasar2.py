import random

def trans_print(message,enc):
    print(f'Before:\n{message}')
    print()
    print('After:')
    for i in enc:
        print(i, end='')

    print(' \n')

def pri_nt(enc):
    print('Before:\n\nA B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    print()
    print('After: \n')
    for i in enc:
        print(i.upper(), end=' ')
    print()

class Ceasar_2:

    # alpha = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,
    #             "g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
    #             "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,
    #             "s":19,"t":20,"u":21,"v":22,"w":23,"x":24,
    #             "y":25,"z":26}

    def __init__(self,ciph) -> None:
        self.ciph = ciph
    
    def encrypt(self,message):
        alph_encry = []

        for i in message.lower():

            if not i.isalpha():
                pass
            else:
                i = chr(ord(i) - self.ciph)

                if ord(i) < 97: 
                    i = chr(ord(i) + 26)

            alph_encry.append(i)
        return alph_encry

    def decrypt(self, message):
        alph_decry = []

        for i in message.lower():

            if not i.isalpha():
                pass
            else:
                i = chr(ord(i) + self.ciph)

                if ord(i) > 122:
                    i = chr(ord(i) - 26)

            alph_decry.append(i)
        return alph_decry




while True:
    bif = (input("Do you want to decrypt or encrypt a message?: ")).strip()
    if bif == 'encrypt' or bif == 'decrypt':
        break
    else:
        print("\n\nPlease type one of the options above\n\n")

if bif == 'encrypt':
    message = input('choose a sentence to encrypt: ')
elif bif == 'decrypt':
    message = input('choose a sentence to decrypt: ')



while True:
    try:
        cipher = int(input('select the cipher: '))
    except ValueError:
        print("type an int value pls.")

    if cipher >= 26 or cipher < 1:
        print('choose a number between 1 and 25 pls.')
    else:
        break



my_cipher = Ceasar_2(cipher)
if bif =='encrypt':
    my_encry = my_cipher.encrypt(message)
    trans_print(message,my_encry)
elif bif == 'decrypt':
    my_decry = my_cipher.decrypt(message)
    trans_print(message,my_decry)


