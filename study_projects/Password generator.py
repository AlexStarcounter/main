import random
digits = '0123456789'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'
conf_chars = 'l1o0O'

def is_valid_answer(answer):
    return (answer == 'yes' or answer == 'no')

def invalid_answer():
    if not is_valid_answer(answer):
        print('', "I don't understand you", sep='\n')

def is_digit_answer(answer):
    return answer.isdigit()

print('Hello! I can generate passwords with your requirements')
answer = ''
while answer != 'no':
    chars = []
    pass_number = ''
    while is_digit_answer(pass_number) != True:
        pass_number = input('Write the number of passwords you want to generate: ')
        if not is_digit_answer(pass_number):
            print('', "It's not a number", sep='\n')
    pass_number = int(pass_number)

    pass_length = ''
    while is_digit_answer(pass_length) != True:
        pass_length = input('Write the necessary length for your passwords: ')
        if not is_digit_answer(pass_length):
            print('', "It's not a number", sep='\n')
    pass_length = int(pass_length)

    answer = ''
    while is_valid_answer(answer) != True:
        answer = input('Write "yes" if you want to include digits in your passwords, or "no" elsewise: ')
        invalid_answer()
    if answer == 'yes':
        chars.append(digits)

    answer = ''
    while is_valid_answer(answer) != True:
        answer = input('Write "yes" if you want to include letters in your passwords, or "no" elsewise: ')
        invalid_answer()
    if answer == 'yes':
        chars.append(low_letters)
        answer = ''
        while is_valid_answer(answer) != True:
            answer = input('Write "yes" if you want to include capital letters in your passwords, or "no" elsewise: ')
            invalid_answer()
        if answer == 'yes':
            chars.append(up_letters)

    answer = ''
    while is_valid_answer(answer) != True:
        answer = input('Write "yes" if you want to include symbols (!#$%&*+-=?@^_) in your passwords, or "no" elsewise: ')
        invalid_answer()
    if answer == 'yes':
        chars.append(symbols)

    answer = ''
    while is_valid_answer(answer) != True:
        answer = input('Write "yes" if you want to exclude confusing characters (l1o0O) from your passwords, or "no" elsewise: ')
        invalid_answer()
    if answer == 'yes':
        for c in conf_chars:
            for el in chars:
                if c in el:
                    chars.remove(el)
                    el = el.replace(c, '')
                    chars.append(el)

    all_chars = ''.join(chars)
    req_chars = len(chars)
    if pass_length >= req_chars and req_chars != 0:
        print('', 'Generated passwords:', sep='\n')
        for _ in range(pass_number):
            cur_pass_length = 0
            password = []
            for i in range(req_chars):
                password.append(random.choice(chars[i]))
                cur_pass_length += 1
            if cur_pass_length < pass_length:
                for _ in range(pass_length - cur_pass_length):
                    password.append(random.choice(all_chars))
            random.shuffle(password)
            print(*password, sep='')
        print()
    else:
        print('', "Passwords with your requirements can't be generated", sep='\n')
    
    answer = ''
    while is_valid_answer(answer) != True:
        answer = input('Write "yes" if you want to generate passwords with other requirements, or "no" elsewise: ')
        invalid_answer()
    print()

input('Press Enter to exit')