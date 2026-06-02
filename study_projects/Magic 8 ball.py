def is_valid_answer(answer):
    return (answer == 'да' or answer == 'нет')

def get_answer():
    global answer1
    answer1 = input('Напиши "да" или "нет": ').lower().strip()

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос, на который можно ответить "да" или "нет".')
print('Начнём?')
answer1 = ''
while is_valid_answer(answer1) != True:
    get_answer()
    if is_valid_answer(answer1) == False:
        print('', 'Не понимаю тебя.', sep='\n')
if answer1 == 'да':
    import random
    ball_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    while True:
        print()
        input('Введи свой вопрос: ')
        print(random.choice(ball_answers))
        print('', 'Хочешь задать ещё вопрос?', sep='\n')
        answer1 = ''
        while is_valid_answer(answer1) != True:
            get_answer()
            if is_valid_answer(answer1) == False:
                print('', 'Не понимаю тебя.', sep='\n')
        if answer1 == 'нет':
            break
        
print()
input('Возвращайся, если возникнут вопросы!')