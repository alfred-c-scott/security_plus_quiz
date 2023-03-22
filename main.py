# PSUEDO CODE

# 1. read data from file into a list of lines
# 2. iterate through the list and use a regex pattern that checks for an integer followed by a period and space
# 3. if a new question begins in the line, split the line into two parts composed of the detected integer, and the
#    question text string that follows
# 4. before iterating to the next line use the integer, and question text to create a new Question() object
# 5. append the new question to the list of questions
# 6. if no integer matching the pattern is detected this indicates that the line contains question text - use the
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


def q_num_in_q_text(index):
    if index > 0:
        return True
    else:
        return False


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
    answr_started = False
    for line in f:
        q_num_bool = q_num_pattern.search(line)
        q_num_matches = q_num_pattern.finditer(line)
        answr_bool = answr_pattern.search(line)
        answr_matches = answr_pattern.finditer(line)
        if q_num_bool:
            for q in q_num_matches:
                if q_num_in_q_text(q.start()):
                    print(line, end='')
                else:
                    answr_started = False
                    print(q.group()+line[q.end():len(line)-1])
                    new_question = Question(int(q.group()[q.start():q.end()-2]), line[q.end():len(line)-1])
                    question_list.append(new_question)

for q in question_list:
    print(q.question_num, end='. ')
    print(q.question_txt)
