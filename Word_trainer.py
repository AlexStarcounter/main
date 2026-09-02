import os
import sqlite3
import random
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'Dictionary.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?", ('words',))
table = cursor.fetchall()
if not table:
    n_language = input('Type your native language: ').lower().strip()
    l_language = input("Type the language you're learning: ").lower().strip()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS words ({n_language} TEXT, {l_language} TEXT, test INTEGER)')
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?", ('tech_stuff',))
table = cursor.fetchall()
if not table:
    switch = ''
    while switch != 'yes' and switch != 'no':
        switch = input('Type "yes" to enable auto keyboard layout switching, or type "no" otherwise: ').lower().strip()
        if switch != 'yes' and switch != 'no':
            print('Invalid answer. Try again')
    cursor.execute('CREATE TABLE IF NOT EXISTS tech_stuff (switch TEXT)')
    cursor.execute('INSERT INTO tech_stuff (switch) VALUES (?)', (switch,))
    connection.commit()

cursor.execute('SELECT switch FROM tech_stuff')
switch = cursor.fetchone()
if switch[0] == 'yes':
    try:
        import pyautogui
    except ImportError:
        print('Please, wait. Installing the required library')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
        import pyautogui
        print('Installation completed')

cursor.execute('SELECT * FROM words LIMIT 0')
columns = [description[0] for description in cursor.description]
n_language = columns[0]
l_language = columns[1]

def words_check():
    print(word1, '– ', end='')
    global word2
    word2 = input().lower().strip()
    if word1_in_l_language and word2 == words[1].lower() or word1_in_n_language and word2 == words[0].lower():
        print('Correct!')
    elif word2 == 'stop':
        return
    else:
        print('Incorrect! ', end='')
        global mistake_made
        mistake_made = True

answer = ''
while answer != 'exit':
    print('                         MAIN MENU                        ')
    print('If you want to edit your dictionary, type "edit"')
    print('If you want to practice translating words, type "practice"')
    print('If you want to exit the program, type "exit"')
    answer = input('I want to ').lower().strip()

    if answer == 'edit':
        while answer != 'stop':
            print('                          EDITING MENU                          ')
            print('If you want to add words to your dicitionary, type "add"')
            print('If you want to correct words in your dictionary, type "correct"')
            print('If you want to delete words from your dictionary, type "delete"')
            print('If you want to stop editing your dictionary, type "stop"')
            answer = input('I want to ').lower().strip()

            if answer == 'add':
                answer1 = ''
                while answer1 != 'stop':
                    l_language_word = input(f'Type the {l_language} word: ')
                    cursor.execute(f'SELECT {l_language} FROM words WHERE {l_language} = ?', (l_language_word,))
                    word_being_added = cursor.fetchone()
                    if word_being_added:
                        print('This word is already in your dictionary')
                    else:
                        if switch[0] == 'yes':
                            pyautogui.hotkey('alt', 'shift')
                        n_language_word = input(f'Type its {n_language} translation: ')
                        if switch[0] == 'yes':
                            pyautogui.hotkey('alt', 'shift')
                        save_check = input('Press Enter to save the pair, or type "no" otherwise: ').lower().strip()
                        answer1 = input('If you want to stop adding, type "stop", or press Enter to continue: ').lower().strip()
                        if save_check != 'no':
                            cursor.execute(f'INSERT INTO words ({l_language}, {n_language}, test) VALUES (?, ?, ?)', (l_language_word, n_language_word, 0))
                            connection.commit()

            elif answer == 'correct':
                answer1 = ''
                while answer1 != 'stop':
                    word_to_correct = input('Type the word you need to correct: ')
                    cursor.execute(f'SELECT {l_language}, {n_language} FROM words WHERE {l_language} = ? OR {n_language} = ?', (word_to_correct, word_to_correct))
                    pair_being_corrected = cursor.fetchone()
                    if pair_being_corrected:
                        corrected_word = input('Type the corrected word: ')
                        save_check = input('Press Enter to save the correction, or type "no" otherwise: ').lower().strip()
                        answer1 = input('If you want to stop correcting, type "stop", or press Enter to continue: ').lower().strip()
                        if save_check != 'no':
                            if word_to_correct == pair_being_corrected[0]:
                                cursor.execute(f'UPDATE words SET {l_language} = ? WHERE {l_language} = ?', (corrected_word, word_to_correct))
                            else:
                                cursor.execute(f'UPDATE words SET {n_language} = ? WHERE {n_language} = ?', (corrected_word, word_to_correct))
                            connection.commit()
                    else:
                        print('There is no such word in your dictionary')

            elif answer == 'delete':
                answer1 = ''
                while answer1 != 'stop':
                    word_to_delete = input('Type any word from the pair you want to delete: ')
                    cursor.execute(f'SELECT {l_language}, {n_language} FROM words WHERE {l_language} = ? OR {n_language} = ?', (word_to_delete, word_to_delete))
                    pair_being_deleted = cursor.fetchone()
                    if pair_being_deleted:
                        save_check = input(f'Press Enter to delete the pair "{pair_being_deleted[0]} - {pair_being_deleted[1]}", or type "no" otherwise: ').lower().strip()
                        answer1 = input('If you want to stop deleting, type "stop", or press Enter to continue: ').lower().strip()
                        if save_check != 'no':
                            if word_to_delete == pair_being_deleted[0]:
                                cursor.execute(f'DELETE FROM words WHERE {l_language} = ?', (word_to_delete,))
                            else:
                                cursor.execute(f'DELETE FROM words WHERE {n_language} = ?', (word_to_delete,))
                            connection.commit()
                    else:
                        print('There is no such word in your dictionary')
       
            elif answer != 'stop':
                print('Invalid answer. Try again')

    elif answer == 'practice':
        word2 = ''
        prev_word1 = ''
        prev_word1_in_l_language = False
        prev_word1_in_n_language = False
        print('                   PRACTICING MENU                   ')
        print('If you want to stop practicing, type "stop" any time')
        while word2 != 'stop':
            cursor.execute(f'SELECT {l_language}, {n_language} FROM words WHERE test = 0 ORDER BY RANDOM() LIMIT 1')
            words = cursor.fetchone()
            if words:
                word1 = random.choice(words)
                word1_in_l_language = False
                word1_in_n_language = False
                if word1 == words[0]:
                    word1_in_l_language = True
                else:
                    word1_in_n_language = True
                if switch[0] == 'yes' and (word1_in_l_language and prev_word1_in_n_language or word1_in_n_language and prev_word1_in_l_language):
                    pyautogui.hotkey('alt', 'shift')
                prev_word1_in_l_language = False
                prev_word1_in_n_language = False
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
                            if word1_in_l_language:
                                print(f'The correct meaning of "{word1}" is "{words[1]}"')
                            else:
                                print(f'The correct meaning of "{word1}" is "{words[0]}"')
                prev_word1 = word1
                if word1_in_l_language:
                    prev_word1_in_l_language = True
                else:
                    prev_word1_in_n_language = True
                cursor.execute(f'UPDATE words SET test = ? WHERE {l_language} = ? OR {n_language} = ?', (1, word1, word1))
            else:
                print('You completed practicing all words in your dictionary')
                answer = input('Press Enter to return to MAIN MENU, or type "start over" if you want to start practicing again: ').lower().strip()
                if answer == 'start over':
                    connection.close()
                    connection = sqlite3.connect(db_path)
                    cursor = connection.cursor()
                else:
                    break

    elif answer != 'exit':
        print('Invalid answer. Try again')

cursor.execute('UPDATE words SET test = ? WHERE test = ?', (0, 1))
connection.commit()
connection.close()