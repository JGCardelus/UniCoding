import matplotlib.pyplot as plt
import pandas as pd

# Lab 8.4 Word with API REST
import os
import requests
import json
import random
import time

# os.popen('pip3 install requests')
class Game_Stats:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.total_time = 0
        self.answered_questions = 0

    def update(self, is_correct, time):
        self.answered_questions += 1
        self.total_time += time
        if is_correct:
            self.correct += 1
        else:
            self.incorrect += 1

def get_amount():
    amount = 0
    while True:
        try:
            amount = int(input("Enter the number of questions (1-50): "))

            if amount > 0 and amount < 51:
                break
            else:
                print("The number is out of range")
        except ValueError:
            print("You have to enter a number.")

    return amount

def get_difficulty():
    difficulty = ''
    
    print()
    print("Please select the difficulty: ")
    print("     1 -- Easy")
    print("     2 -- Medium")
    print("     3 -- Hard")
    print("The default answer is 1.")
    print()
    choice = input("      >>> ")

    if choice == '1':
        difficulty = 'easy'
    elif choice == '2':
        difficulty = 'medium'
    elif choice == '3':
        difficulty = 'hard'
    else:
        print("The value entered is not value. Selected default option.")
        difficulty = 'easy'

    return difficulty

def get_category():
    category = None
    print()
    print("Please select the difficulty: ")
    print("     1 -- Any category")
    print("     2 -- General knowledge")
    print("     3 -- Politics")
    print("     4 -- Science: Computers")
    print("     5 -- Science: Mathematics")
    print("     6 -- History")
    print("The default answer is 1.")
    print()
    choice = input("      >>> ")

    if choice == '2':
        category = 9
    elif choice == '3':
        category = 24
    elif choice == '4':
        category = 18
    elif choice == '5':
        category = 19
    elif choice == '6':
        category = 23

    return category

def get_api_url():
    api_url = "https://opentdb.com/api.php"

    amount = get_amount()
    difficulty = get_difficulty()
    category = get_category()

    # Params = ?amount=10&difficulty=medium&type=multiple&category
    params = '?amount=' + str(amount)
    params += '&type=multiple'
    params += '&difficulty=' + difficulty
    if category != None:
        params += '&category=' + str(category)

    if category != None:
        params["category"] = category

    api_url += params

    return api_url

def get_questions():
    api_url = get_api_url()
    response = requests.get(api_url)
    data = response.json()
    
    return data

def ask_solution(correct, answers):
    time = 0
    is_correct = False
    while True:
        start_time = time.time()
        for i, answer in answers:
            print("     %s) %s" % ((i + 1), answer))
        print()
        try:
            choice = int(input("       >>> "))

            if choice > len(answers) or choice < 1:
                print("Please enter a number between 1 and %s" % (len(answers)))
            else:
                time = time.time() - start_time
                index = choice - 1
                if correct == answers[index]:
                    is_correct = True

                break
        except ValueError:
            print("Please enter a number between 1 and %s" % (len(answers)))

        return is_correct, time
    

def ask_question(question_data, game_stats):
    category = question_data["category"]
    question = question_data["question"]
    correct_answer = question_data["correct_answer"]
    answers = question_data["incorrect_answers"]

    answers.extend(correct_answer)
    answers = random.shuffle(answers)

    print()
    print(question)
    print('     -- %s' % (category))
    print()
    is_correct, time = ask_solution(correct_answer, answers)

    game_stats.update(is_correct, time)

def start_game(data):
    questions = data["results"]
    game_stats = Game_Stats()

    for question_data in questions:
        ask_question(question_data, game_stats)

def new_game():
    data = get_questions()
    start_game(data)




