import os
import sqlite3
import random
import subprocess
import sys

try:
    import pyautogui
except ImportError:
    print('Please, wait. Installing the required library')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    import pyautogui
    print('Installation completed')

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'Dictionary.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS words (english TEXT, russian TEXT, test INTEGER)')

def words_check():
    print(word1, '– ', end='')
    global word2
    word2 = input().lower().strip()
    if word1_in_english and word2 == words[1].lower() or word1_in_russian and word2 == words[0].lower():
        print('Correct!')
    elif word2 == 'stop':
        return
    else:
        print('Incorrect! ', end='')
        global mistake_made
        mistake_made = True

answer1 = ''
while answer1 != 'exit':
    print('                         MAIN MENU                        ')
    print('If you want to edit your dictionary, write "edit"')
    print('If you want to practice word translating, write "practice"')
    print('If you want to exit the program, write "exit"')
    answer1 = input('I want to ').lower().strip()

    if answer1 == 'edit':
        answer2 = ''
        while answer2 != 'stop':
            print('                          EDITING MENU                          ')
            print('If you want to add words to your dicitionary, write "add"')
            print('If you want to correct words in your dictionary, write "correct"')
            print('If you want to delete words from your dictionary, write "delete"')
            print('If you want to stop editing your dictionary, write "stop"')
            answer2 = input('I want to ').lower().strip()

            if answer2 == 'add':
                answer3 = ''
                while answer3 != 'stop':
                    eng_word = input('Write the english word: ')
                    cursor.execute('SELECT english FROM words WHERE english = ?', (eng_word,))
                    word_being_added = cursor.fetchone()
                    if word_being_added:
                        print('This word is already in your dictionary')
                    else:
                        pyautogui.hotkey('alt', 'shift')
                        rus_word = input('Write its russian translation: ')
                        pyautogui.hotkey('alt', 'shift')
                        answer4 = input('Press Enter to save the pair, or write "no" elsewise: ').lower().strip()
                        answer3 = input('If you want to stop adding, write "stop", or press Enter to continue: ').lower().strip()
                        if answer4 != 'no':
                            cursor.execute('INSERT INTO words (english, russian, test) VALUES (?, ?, ?)', (eng_word, rus_word, 0))
                            connection.commit()

            elif answer2 == 'correct':
                answer5 = ''
                while answer5 != 'stop':
                    word_to_correct = input('Write the word you need to correct: ')
                    cursor.execute('SELECT english, russian FROM words WHERE english = ? OR russian = ?', (word_to_correct, word_to_correct))
                    pair_being_corrected = cursor.fetchone()
                    if pair_being_corrected:
                        corrected_word = input('Write the corrected word: ')
                        answer6 = input('Press Enter to save the correction, or write "no" elsewise: ').lower().strip()
                        answer5 = input('If you want to stop correcting, write "stop", or press Enter to continue: ').lower().strip()
                        if answer6 != 'no':
                            if word_to_correct == pair_being_corrected[0]:
                                cursor.execute('UPDATE words SET english = ? WHERE english = ?', (corrected_word, word_to_correct))
                            else:
                                cursor.execute('UPDATE words SET russian = ? WHERE russian = ?', (corrected_word, word_to_correct))
                            connection.commit()
                    else:
                        print('There is no such word in your dictionary')

            elif answer2 == 'delete':
                answer7 = ''
                while answer7 != 'stop':
                    word_to_delete = input('Write any word from the pair you want to delete: ')
                    cursor.execute('SELECT english, russian FROM words WHERE english = ? OR russian = ?', (word_to_delete, word_to_delete))
                    pair_being_deleted = cursor.fetchone()
                    if pair_being_deleted:
                        answer8 = input(f'Press Enter to delete the pair "{pair_being_deleted[0]} - {pair_being_deleted[1]}", or write "no" elsewise: ').lower().strip()
                        answer7 = input('If you want to stop deleting, write "stop", or press Enter to continue: ').lower().strip()
                        if answer8 != 'no':
                            if word_to_delete == pair_being_deleted[0]:
                                cursor.execute('DELETE FROM words WHERE english = ?', (word_to_delete,))
                            else:
                                cursor.execute('DELETE FROM words WHERE russian = ?', (word_to_delete,))
                            connection.commit()
                    else:
                        print('There is no such word in your dictionary')
       
            elif answer2 != 'stop':
                print('Invalid answer. Try again')

    elif answer1 == 'practice':
        word2 = ''
        prev_word1 = ''
        prev_word1_in_english = False
        prev_word1_in_russian = False
        print('                   PRACTICING MENU                   ')
        print('If you want to stop practicing, write "stop" any time')
        while word2 != 'stop':
            cursor.execute('SELECT english, russian FROM words WHERE test = 0 ORDER BY RANDOM() LIMIT 1')
            words = cursor.fetchone()
            if words:
                word1 = random.choice(words)
                word1_in_english = False
                word1_in_russian = False
                if word1 == words[0]:
                    word1_in_english = True
                else:
                    word1_in_russian = True
                if word1_in_english and prev_word1_in_russian or word1_in_russian and prev_word1_in_english:
                    pyautogui.hotkey('alt', 'shift')
                prev_word1_in_english = False
                prev_word1_in_russian = False
                mistake_made = False
                
                words_check()
                if mistake_made:
                    print('Try again')
                    mistake_made = False
                    words_check()
                    if mistake_made:
                        print('Try again')
                        mistake_made = False
                        words_check()
                        if mistake_made:
                            if word1_in_english:
                                print(f'The correct meaning for "{word1}" is "{words[1]}"')
                            else:
                                print(f'The correct meaning for "{word1}" is "{words[0]}"')
                prev_word1 = word1
                if word1_in_english:
                    prev_word1_in_english = True
                else:
                    prev_word1_in_russian = True
                cursor.execute('UPDATE words SET test = ? WHERE english = ? OR russian = ?', (1, word1, word1))
            else:
                print('You completed practicing all words in your dictionary')
                answer9 = input('Press Enter to return to MAIN MENU, or write "start over", if you want to start practicing again: ').lower().strip()
                if answer9 == 'start over':
                    connection.close()
                    connection = sqlite3.connect(db_path)
                    cursor = connection.cursor()
                else:
                    break

    elif answer1 != 'exit':
        print('Invalid answer. Try again')

cursor.execute('UPDATE words SET test = ? WHERE test = ?', (0, 1))
connection.commit()
connection.close()