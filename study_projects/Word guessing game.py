import random
words = ['ГРЫЖА', 'ЯСТРЕБ', 'ВОРОБЕЙ', 'ЖАЛЮЗИ', 'СФИНКТЕР', 'РОЗАРИЙ', 'ПЕЛЕНА', 'КАТАСТРОФА', 'ИЗУМРУД', 'ВЫСЕЛКИ', 'ПРОТАГОНИСТ', 'ПЕЛЬМЕНЬ', 'КОСОВОРОТКА', 'КРОВОСОС', 'ПЛЕЯДА', 'ФАНТАСМАГОРИЯ', 'БРОД', 'КРЕСТ', 'СПАЛЬНЯ', 'ПЕКАРЬ', 'РУЖЬЁ', 'БРИТВА', 'НЕАНДЕРТАЛЕЦ', 'ДРИФТ', 'ФЕНОМЕН', 'ВЕРТИХВОСТКА', 'ОСЕНЬ', 'ПАЛИНДРОМ', 'СМОТРИТЕЛЬ', 'ВЕКТОР', 'РОДИНА', 'ПАХОТА', 'РЕКРУТ', 'БРЕЗЕНТ', 'СМЫСЛ', 'ВЕГЕТАРИАНЕЦ', 'СОЛНЦЕ', 'ТРОПА', 'РТУТЬ', 'ПЛАЦЕБО', 'ВОДОКАЧКА', 'ДРЕЗИНА', 'ПРОТОТИП', 'ДРОН', 'ВЕЛОСИПЕД', 'МОТОЦИКЛ', 'ИЗДЕВАТЕЛЬСТВО', 'ФАМИЛЬЯР', 'ГРАФИНЯ', 'ЗЕРКАЛО', 'ВОЙНА', 'БРАТСТВО', 'ДРУИД', 'БЕНЗОПИЛА', 'ПЕРСТЕНЬ', 'КРОМКА', 'АНАКОНДА', 'БОЛИГОЛОВ', 'ВЕРЕНИЦА', 'ГРОЗДЬ', 'ДЕБРИ', 'ЕРМОЛКА', 'ЖУРАВЛЬ', 'ЗЛОСТЬ', 'ИНДИГО', 'ЙОГУРТ', 'КОРИДОРНЫЙ', 'ЛЮСТРА', 'МАНДАТ', 'НАТЮРМОРТ', 'ОВЧИНА', 'ПАГОДА', 'РИСТАЛИЩЕ', 'СМЕРТЬ', 'ТОВАРИЩ', 'УСТРИЦА', 'ФЕНХЕЛЬ', 'ХВОЩ', 'ЦИРЮЛЬНИК', 'ЧЕРЕШНЯ', 'ШТАМП', 'ЩУПАЛЬЦЕ', 'ЭЛЕКТОРАТ', 'ЮВЕЛИР', 'ЯНТАРЬ', 'АЛЮМИНИЙ', 'ВОВЛЕЧЁННОСТЬ', 'ДЕМОНСТРАЦИЯ', 'ЖИМОЛОСТЬ', 'ИНДУСТРИЯ', 'КЛАДБИЩЕ', 'МОНСТР', 'ОБСЕРВАТОРИЯ', 'РЕИНКАРНАЦИЯ', 'ТВЕРДЫНЯ', 'ФОРСУНКА', 'ЦАРЕВНА', 'ШЛЯПА', 'ЭНДОРФИН', 'ЯГЕЛЬ']
answer = ''

def is_valid_answer(answer):
    return (answer == 'д' or answer == 'н')

def is_letter(answer):
    return answer.isalpha()

def get_word():
    return random.choice(words)

def play():
    word = get_word()
    game_word = '_' * len(word)
    answer = ''
    guessed = []
    mistakes = 0

    def display_hangman(mistakes):
        stages = [
                    '''
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    ''',                 
                    '''
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    ''',                 
                    '''
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    ''',                 
                    '''
                    --------
                    |      |
                    |      O
                    |     /|
                    |      |
                    |     
                    -
                    ''',                 
                    '''
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |      
                    -
                    ''',                
                    '''
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     / 
                    -
                    ''',                 
                    '''
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     / \\
                    -
                    '''
        ]
        return stages[mistakes]
    print(display_hangman(mistakes))
    print(game_word)

    def letter_check():
        nonlocal answer
        while not is_letter(answer) or answer in guessed:
            answer = input('Напишите букву или слово целиком: ').upper().strip()
            if not is_letter(answer):
                print('', 'Это не буква и не слово', sep='\n')
            else:
                if answer in guessed:
                    print('', 'Кажется, вы это уже называли...', sep='\n')

        if len(answer) == 1 and answer in word:
            temp_word = ''
            nonlocal game_word
            for i in range(len(word)):
                if word[i] == answer:
                    temp_word += answer
                else:
                    temp_word += game_word[i]
            game_word = temp_word
            print('Такая буква есть в этом слове!')
        elif answer == word:
            game_word = word
        else:
            nonlocal mistakes
            mistakes += 1
            if len(answer) == 1:
                print('Такой буквы нет в этом слове...')
            else:
                print('Нет, это не то слово...')
            print(display_hangman(mistakes))
        guessed.append(answer)

    while True:
        letter_check()
        if game_word == word:
            print('', game_word, sep='\n')
            print('Поздравляю, вы угадали слово!')
            break
        if mistakes == 6:
            print('Вы проиграли...')
            print(f'Это было слово "{word}"')
            break
        print('', game_word, sep='\n')

print('Добро пожаловать в игру "Виселица"!')
print('Правила просты: я загадываю слово, а вы пытаетесь отгадать его по буквам.')
print('Если указанной вами буквы нет в слове, вам засчитывается ошибка. Шестая ошибка станет фатальной!')
print('Также можно попытаться отгадать слово целиком.')

while not is_valid_answer(answer):
    answer = input('Хотите сыграть? [д/н]: ').lower().strip()
    if not is_valid_answer(answer):
        print('', 'Не понимаю вас', sep='\n')

if answer == 'д':
    play()
    print()
    while True:
        answer = ''
        while not is_valid_answer(answer):
            answer = input('Хотите сыграть ещё? [д/н]: ').lower().strip()
            if not is_valid_answer(answer):
                print('', 'Не понимаю вас', sep='\n')
        if answer == 'д':
            play()
        else:
            break

print()
input('Нажмите Enter, чтобы выйти')