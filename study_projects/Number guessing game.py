def is_valid_answer(answer):
    return (answer == 'yes' or answer == 'no')

def get_answer1():
    print('Do you want to play with me?')
    global answer1
    answer1 = input('Write "yes" or "no": ').lower().strip()

def get_answer2():
    print('Do you want to play again?')
    global answer2
    answer2 = input('Write "yes" or "no": ').lower().strip()

def is_valid_number(answer):
    return answer.isdigit()

print('Welcome to the game "Number guessing"')
print("The rules are simple. I choose a number from a set range, and you're trying to guess it")
answer1 = ''
while is_valid_answer(answer1) != True:
    get_answer1()
    if is_valid_answer(answer1) == False:
        print('', "I don't understand you", sep='\n')
if answer1 == 'yes':
    import random
    print('', 'Remember that borders are included in the range, and numbers should be natural', sep='\n')
    num1 = ''
    num2 = ''
    while is_valid_number(num1) != True:
        num1 = input('Set the left border of the range: ')
        if is_valid_number(num1) == False:
            print('', "That's not a number", sep='\n')
    while is_valid_number(num2) != True:
        num2 = input('Set the right border of the range: ')
        if is_valid_number(num2) == False:
            print('', "That's not a number", sep='\n')
    answer2 = ''
    while True:
        if answer2 == 'no':
            break
        answer2 = ''
        print('', 'Choosing a number...', "I'm ready for your guesses now", sep='\n')
        chosen_num = random.randint(int(num1), int(num2))
        guess = 10 ** 8
        cnt = 0
        while guess != chosen_num:
            guess = input('Your guess is that the number is: ')
            guess = int(guess)
            if guess == chosen_num:
                cnt += 1
                print('', "Congratulations! You're absolutely right!", sep='\n')
                print(f'Number of guesses: {cnt}', '', sep='\n')
                while is_valid_answer(answer2) != True:
                    get_answer2()
                    if is_valid_answer(answer2) == False:
                        print('', "I don't understand you", sep='\n')
            if guess > chosen_num:
                cnt += 1
                print('', 'No, my number is smaller. Try again', sep='\n')
            if guess < chosen_num:
                cnt += 1
                print('', 'No, my number is bigger. Try again', sep='\n')

print()
input('Okay, maybe another time. Press Enter to exit')