#!/usr/bin/python3

import re
import random

class Question:
    def __init__(self, question_num=0, question_txt='blah'):
        self.question_num = question_num
        self.question_txt = question_txt
        self.choice_list = []
        self.explanation = None

    def concatenate_question_text(self, q_l):
        self.question_txt = self.question_txt + q_l

    def append_choice_list(self, c_dict):
        self.choice_list.append(c_dict)

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')
answr_pattern = re.compile(r'([ABCD])\. ')

question_list = []
# choice_dict = {}

with open('ch_1_questions') as f:
    line_list = f.readlines()
    active_question = 0
    active_choice = ''
    for line in line_list:
        q_num_bool = q_num_pattern.search(line)
        q_num_matches = q_num_pattern.finditer(line)
        choice_bool = answr_pattern.search(line)
        choice_matches = answr_pattern.finditer(line)
        num_of_choices = len(answr_pattern.findall(line))
        if q_num_bool and choice_bool:
            for q in q_num_matches:
                if q.start() > 0:
                    for a in choice_matches:
                        if a.start() == 0:
                            for question in question_list:
                                if question.question_num == active_question:
                                    choice = line[a.start():a.end()-2]
                                    choice_text = line[a.end():q.start()]
                                    choice_dict['choice'] = choice
                                    choice_dict['text'] = choice_txt
                                    choice_dict['correct'] = False
                                    question.append_choice_list(choice_dict)
                active_question = int(line[q.start():q.end()-2])
                new_question = Question(active_question, line[q.start():len(line)-1])
                question_list.append(new_question)
        # TODO fix for case where q_num starts in Choice D. where Choice D. is two lines long
        elif q_num_bool:
            for q in q_num_matches:
                if q.start() > 0:
                    for question in question_list:
                        if question.question_num == active_question:
                            question.concatenate_question_text(' '+line[0:len(line)-1])
                else:
                    q_num = int(q.group()[q.start():q.end()-2])
                    active_question = q_num
                    q_text = line[q.end():len(line)-1]
                    new_question = Question(question_num=q_num, question_txt=q_text)
                    question_list.append(new_question)
                    # TODO update for case with multiple lines of text for choice
        elif choice_bool:
            if num_of_choices > 1:
                c_0_start = 0
                c_0_end = 0
                c_1_start = 0
                c_1_end = 0
                choice_0_dict = {}
                choice_1_dict = {}
                for ct, a in enumerate(choice_matches):
                    if ct == 0:
                        c_0_start = a.start()
                        c_0_end = a.end()
                    if ct == 1:
                        c_1_start = a.start()
                        c_1_end = a.end()
                choice_0 = line[c_0_start:c_0_end-2]
                choice_0_txt = line[c_0_end:c_1_start]
                choice_1 = line[c_1_start:c_1_end-2]
                choice_1_txt = line[c_1_end:len(line)-1]
                choice_0_dict['choice'] = choice_0
                choice_0_dict['text'] = choice_0_txt
                choice_0_dict['correct'] = False
                choice_1_dict['choice'] = choice_1
                choice_1_dict['text'] = choice_1_txt
                choice_1_dict['correct'] = False
                for q in question_list:
                    if q.question_num == active_question:
                        q.append_choice_list(choice_0_dict)
                        q.append_choice_list(choice_1_dict)
                choice_0_dict = {}
                choice_1_dict = {}
                # print(choice_0+' '+choice_0_txt)
                # print(choice_1+' '+choice_1_txt)
            else:
                choice_dict = {}
                for a in choice_matches:
                    choice = line[a.start():a.end()-2]
                    choice_txt = line[a.end():len(line)-1]
                    # print(choice+' '+choice_txt)
                    choice_dict['choice'] = choice
                    choice_dict['text'] = choice_txt
                    choice_dict['correct'] = False
                    for q in question_list:
                        if q.question_num == active_question:
                            q.append_choice_list(choice_dict)
                        else:
                            pass
                    choice_dict = {}
        else:
            for q in question_list:
                if q.question_num == active_question:
                    q.concatenate_question_text(' '+line[0:len(line)-1])

for ct, q in enumerate(question_list):
    print(ct+1)
    print(q.question_num, end='. ')
    print(q.question_txt)
    for c in q.choice_list:
        print(c)
    # if len(q.choice_list) < 4:
    #     print(f'Error in Question {q.question_num}. ')

# def quiz_func(q):
#     for i, q in enumerate(q):
#         print(str(i+1) + str(q.question_num))
#
# quiz = []
# while True:
#     response_1 = input('what would you like to do:\n\t1. Take a quiz\n\t2. Exit program\n>', )
#     if response_1 == '1':
#         response_2 = input('How many questions would you like to answer:\n\t1. 10\n\t2. 20\n\t3. 30\n\t4. 40\n>')
#         random.shuffle(question_list)
#         if response_2 == '1':
#             quiz = question_list[0:10]
#             quiz_func(quiz)
#         elif response_2 == '2':
#             quiz = question_list[0:20]
#         elif response_2 == '3':
#             quiz = question_list[0:30]
#         elif response_2 == '4':
#             quiz = question_list[0:40]
#     if response_1 == '2':
#         break
