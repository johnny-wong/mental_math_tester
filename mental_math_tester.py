import random
import math
import time
import os
import pandas as pd

class question():
    def __init__(self, lower=0, upper=200, decimals=0):
        self.operations = ['x', '/', '+', '-', 'sqrt', '^']
        self.operand = None
        self.decimals = decimals
        self.lower = lower
        self.upper = upper
        self.num_1 = None
        self.num_2 = None
        self.q_string = None
        self.answer = None
        self.question_list = []
        self.answer_list = []
        self.time_list = []
        self.given_answer_list = []
        self.percent_error_list = []
        self.score_list = []

    def generate_q(self):
        self.operand = random.choice(self.operations)
        self.num_1 = round(random.uniform(self.lower, self.upper), self.decimals)
        if self.operand == '^':
            self.num_2 = round(random.uniform(2, 3))
        else:
            self.num_2 = round(random.uniform(self.lower, self.upper), self.decimals)
        
        if self.operand == 'x':
            self.q_string = str(self.num_1) + 'x' + str(self.num_2)
            self.answer = self.num_1 * self.num_2
        elif self.operand == '/':
            self.q_string = str(self.num_1) + '/' + str(self.num_2)
            self.answer = self.num_1/self.num_2
        elif self.operand == '+':
            self.q_string = str(self.num_1) + '+' + str(self.num_2)
            self.answer = self.num_1+self.num_2
        elif self.operand == '-':
            self.q_string = str(self.num_1) + '-' + str(self.num_2)
            self.answer = self.num_1-self.num_2
        elif self.operand == 'sqrt':
            self.q_string = 'sqrt(' + str(self.num_1) + ')'
            self.answer = math.sqrt(self.num_1)
        elif self.operand == '^':
            self.q_string = str(self.num_1) + '^' + str(self.num_2)
            self.answer = self.num_1 ** self.num_2

        self.question_list.append(self.q_string)
        self.answer_list.append(self.answer)

    def print_q(self):
        print(self.q_string)

    def calculate_score(self, percent_error, time_taken):
        return abs(percent_error) * time_taken

    def start_test(self, num_q=10):
        for i in range(num_q):
            os.system('cls')
            self.generate_q()
            t0 = time.time() 
            my_input = input(self.q_string + '\n')
            try:
                my_answer = float(my_input)
                parsed = True
                self.given_answer_list.append(my_answer)
                
                percent_error = (my_answer/float(self.answer) - 1) * 100
                self.percent_error_list.append(percent_error)
                
                time_taken = time.time() - t0
                self.time_list.append(time_taken)
                
                score = self.calculate_score(percent_error, time_taken)
                self.score_list.append(score)
            except:
                print('{} can\'t be parsed'.format(my_input))
                parsed = False
                continue

    def print_results(self):
        df_results = pd.DataFrame(data={'question':self.question_list,
            'answer':self.answer_list,
            'given_answer':self.given_answer_list,
            'percent_error':self.percent_error_list,
            'time_taken':self.time_list,
            'score':self.score_list},
            columns=['question', 'answer', 'given_answer', 'percent_error', 
            'time_taken', 'score'])
        print(df_results)
        print('final score: {}'.format(sum(self.score_list)))

if __name__ == '__main__':
    question_class = question()
    question_class.start_test(5)
    question_class.print_results()