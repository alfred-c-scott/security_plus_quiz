import re


class Question:
    def __init__(self, q_num=0, q_text='blah'):
        self.question_num = q_num
        self.question_txt = q_text
        self.answers = []
        self.explanation = None

    def concatenate_question_text(self, q_l):
        self.question_txt = self.question_txt + q_l

    def add_answer(self, answer):
        self.answers.append(answer)


q_num_pattern = re.compile(r'\d{1,3}\.\s')
answr_pattern = re.compile(r'([ABCD])\. ')

question_list = []
answer_list = [
    {
        'option': 'W',
        'text': None,
        'bool_correct': False
    },
    {
        'option': 'X',
        'text': None,
        'bool_correct': False
    },
    {
        'option': 'Y',
        'text': None,
        'bool_correct': False
    },
    {
        'option': 'Z',
        'text': None,
        'bool_correct': False
    },

]

with open('test_data_0') as f:
    for line in f:
        q_num_bool = q_num_pattern.search(line)
        q_num_matches = q_num_pattern.finditer(line)
        answr_bool = answr_pattern.search(line)
        answr_matches = answr_pattern.finditer(line)
        if q_num_bool & answr_bool:
            # if q_num in text body
            # --concatenate_question_text
            # elif q_num in answer body
            # --add_answer
            # --new question
            # else
            # --new question
            pass
        elif q_num_bool:
            # --new question
            # --concatenate_answer
            pass
        elif answr_bool:
            # if two answers in one line
            # add both answers
            # else
            # add answer
            pass
        else:
            # concatenate_question_text
            pass

for q in question_list:
    print(q.question_num, end='. ')
    print(q.question_txt)
