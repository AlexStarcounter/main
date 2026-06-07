eng_low_letters = 'abcdefghijklmnopqrstuvwxyz'
eng_up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_low_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_up_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
eng_alph_card = 26
rus_alph_card = 33

def r_encr_l_decr_mech(text1, text2, low_letters, up_letters, shift, alph_card):
    for c in text1:
        if c in low_letters:
            text2 += low_letters[(low_letters.index(c) + shift) % alph_card]
        elif c in up_letters:
            text2 += up_letters[(up_letters.index(c) + shift) % alph_card]
        else:
            text2 += c
    return text2

def l_encr_r_decr_mech(text1, text2, low_letters, up_letters, shift, alph_card):
    for c in text1:
        if c in low_letters:
            text2 += low_letters[(low_letters.index(c) - shift) % alph_card]
        elif c in up_letters:
            text2 += up_letters[(up_letters.index(c) - shift) % alph_card]
        else:
            text2 += c
    return text2

def encrypt_text():
    plain_text = input('Write the text you need to encrypt: ')
    print('Encrypted text:')
    if plain_text.isascii():
        if shift_dir == 'R':
            print(r_encr_l_decr_mech(plain_text, cipher_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
        else:
            print(l_encr_r_decr_mech(plain_text, cipher_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
    else:
        if shift_dir == 'R':
            print(r_encr_l_decr_mech(plain_text, cipher_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
        else:
            print(l_encr_r_decr_mech(plain_text, cipher_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
    print()

def decrypt_text():
    cipher_text = input('Write the text you need to decrypt: ')
    print('Decrypted text:')
    if cipher_text.isascii():
        if shift_dir == 'R':
            print(l_encr_r_decr_mech(cipher_text, plain_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
        else:
            print(r_encr_l_decr_mech(cipher_text, plain_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
    else:
        if shift_dir == 'R':
            print(l_encr_r_decr_mech(cipher_text, plain_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
        else:
            print(r_encr_l_decr_mech(cipher_text, plain_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
    print()

def decrypt_text_shift_num_x():
    cipher_text = input('Write the text you need to decrypt: ')
    print('All possible decrypted texts:')
    if cipher_text.isascii():
        for i in range(1, 26):
            print(l_encr_r_decr_mech(cipher_text, plain_text, eng_low_letters, eng_up_letters, i, eng_alph_card))
    else:
        for i in range(1, 33):
            print(l_encr_r_decr_mech(cipher_text, plain_text, rus_low_letters, rus_up_letters, i, rus_alph_card))
    print()

def decrypt_text_shift_dir_x():
    cipher_text = input('Write the text you need to decrypt: ')
    print('All possible decrypted texts:')
    if cipher_text.isascii():
        print(l_encr_r_decr_mech(cipher_text, plain_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
        print(r_encr_l_decr_mech(cipher_text, plain_text, eng_low_letters, eng_up_letters, shift_num, eng_alph_card))
    else:
        print(l_encr_r_decr_mech(cipher_text, plain_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
        print(r_encr_l_decr_mech(cipher_text, plain_text, rus_low_letters, rus_up_letters, shift_num, rus_alph_card))
    print()

print('Hello, I can help you to encrypt or decrypt texts using Caesar chipher')
print('I can work with texts in english or russian languages')
while True:
    answer = ''
    shift_num = ''
    shift_dir = ''
    cipher_text = ''
    plain_text = ''

    while answer != 'E' and answer != 'D':    
        answer = input('Write "E" if you want to encrypt a text or "D" if you want to decrypt a text: ')
        if answer != 'E' and answer != 'D':
            print('', "I don't understand you", sep='\n')
    if answer == 'E':
        while not shift_num.isdigit():    
            shift_num = input('Write the shift number: ')
            if not shift_num.isdigit():
                print('', "It's not a number", sep='\n')
        shift_num = int(shift_num)
        while shift_dir != 'R' and shift_dir != 'L':    
            shift_dir = input('Write the shift direction, "R" for right or "L" for left: ')
            if shift_dir != 'R' and shift_dir != 'L':
                print('', "I don't understand you", sep='\n')
        encrypt_text()
    else:
        while not shift_num.isdigit() and shift_num != 'x':    
            shift_num = input('''Write the shift number or write "x" if you don't know it: ''')
            if not shift_num.isdigit() and shift_num != 'x':
                print('', "I don't understand you", sep='\n')
        if shift_num.isdigit():
            shift_num = int(shift_num)
        while shift_dir != 'R' and shift_dir != 'L' and shift_dir != 'x':    
            shift_dir = input('''Write the shift direction, "R" for right or "L" for left, or write "x" if you don't know it: ''')
            if shift_dir != 'R' and shift_dir != 'L' and shift_dir != 'x':
                print('', "I don't understand you", sep='\n')
        if shift_num != 'x' and shift_dir != 'x':
            decrypt_text()
        elif shift_dir == 'x' and shift_num != 'x':
            decrypt_text_shift_dir_x()
        else:
            decrypt_text_shift_num_x()

    while answer != 'Y' and answer != 'N':    
        answer = input('Write "Y" if you want to continue, or "N" elsewise: ')
        if answer != 'Y' and answer != 'N':
            print('', "I don't understand you", sep='\n')
    if answer == 'N':
        break

print()
input('Press Enter to exit')