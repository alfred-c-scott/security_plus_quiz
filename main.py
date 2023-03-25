import re


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

q_num_pattern = re.compile(r'[0-9]{1,3}\.\s')
answr_pattern = re.compile(r'([ABCD])\. ')

question_list = []
choice_dict = {}

with open('test_data_0') as f:
    line_list = f.readlines()
    active_question = 0
    for line in line_list:
        q_num_bool = q_num_pattern.search(line)
        q_num_matches = q_num_pattern.finditer(line)
        answr_bool = answr_pattern.search(line)
        answr_matches = answr_pattern.finditer(line)
        num_of_answrs = len(answr_pattern.findall(line))
        if q_num_bool and answr_bool:
            # if q_num in text body
            # --concatenate_question_text
            # elif q_num in answer body
            # --add_answer
            # --new question
            # else
            # --new question
            pass
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
        elif answr_bool:
            if num_of_answrs > 1:
                c_0_start = 0
                c_0_end = 0
                c_1_start = 0
                c_1_end = 0
                choice_0_dict = {}
                choice_1_dict = {}
                for ct, a in enumerate(answr_matches):
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
                print(choice_0+' '+choice_0_txt)
                print(choice_1+' '+choice_1_txt)
            else:
                choice_dict = {}
                for a in answr_matches:
                    choice = line[a.start():a.end()-2]
                    choice_txt = line[a.end():len(line)-1]
                    print(choice+' '+choice_txt)
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

for q in question_list:
    print(q.question_num, end='. ')
    print(q.question_txt)
    for c in q.choice_list:
        print(c)
