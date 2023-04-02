import re
import json

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')

q_list = []

with open('ch_2_questions') as f:
    f_data = f.read()
    f_data = f_data.replace('\n', ' ')
    ct = 1
    q_num_matches = q_num_pattern.finditer(f_data)
    for match in q_num_matches:
        q_num = int(match.group()[0:len(match.group())-2])
        if ct == q_num:
            ct += 1

    num_of_qs = ct-1
    # print(f_data)

    ct = 1
    while ct <= num_of_qs:
        q_begins = re.compile(rf'{str(ct)}\. ')
        q_ends = re.compile(rf'{str(ct+1)}\. ')
        begins_match = q_begins.search(f_data)
        ends_match = q_ends.search(f_data)
        if begins_match and ends_match:
            q_list.append(f_data[begins_match.start():ends_match.start()-1])
        elif begins_match and not ends_match:
            q_list.append(f_data[begins_match.start():len(f_data)])
        ct += 1

choice_pattern = re.compile(r'[ABCD]\. ')


for enum, q in enumerate(q_list):
    choice_matches = choice_pattern.finditer(q)
    for c in choice_matches:
        if q[c.start()-1] != ' ':
            # print(f'format error in {enum_1+1}. for choice {c.group()}')
            q = q[:c.start()]+' '+q[c.start():]
            q_list[enum] = q
            break

# for q in q_list:
#     print(q)



# c_a_pattern = re.compile(r' A\. ')
# c_b_pattern = re.compile(r' B\. ')
# c_c_pattern = re.compile(r' C\. ')
# c_d_pattern = re.compile(r' D\. ')

# updated pattern after reformat of f_data

f_c_pattern = re.compile(r' [ABCD]\. ')

q_dict = {
    'full_str': 'full string',
    'q_num': 0,
    'q_txt': None,
    'choices': [
        {
            'opt': 'A',
            'opt_text': 'answer A',
            'is_correct': False,
        },
        {
            'opt': 'B',
            'opt_text': 'answer D',
            'is_correct': False,
        },
        {
            'opt': 'C',
            'opt_text': 'answer C',
            'is_correct': False,
        },
        {
            'opt': 'D',
            'opt_text': 'answer D',
            'is_correct': False,
        },
    ],
    'explanation': None,
    'tot_attempts': None,
    'correct_attempts': None
}

for enum, q in enumerate(q_list):
    c_match = f_c_pattern.finditer(q)
    q_match = q_num_pattern.search(q)
    # start = q_match.start()
    # end = q_match.end()-2
    # print(start, end=' ')
    # print(end, end=' ')
    # print(q_match.group()[start:end])
    q_dict = {'full_str': q}
    q_dict['q_num'] = int(q_match.group()[q_match.start():q_match.end()-2])
    a_start = None
    a_end = None
    b_start = None
    b_end = None
    c_start = None
    c_end = None
    d_start = None
    d_end = None
    for c in c_match:
        if c.group() == ' A. ':
            a_start = c.start()
            a_end = c.end()
        if c.group() == ' B. ':
            b_start = c.start()
            b_end = c.end()
        if c.group() == ' C. ':
            c_start = c.start()
            c_end = c.end()
        if c.group() == ' D. ':
            d_start = c.start()
            d_end = c.end()
            pass
    # for ch in q_dict['choices']:
    #     if ch['opt'] == 'A':
    #         print(ch['opt_text'])
    q_dict['q_txt'] = q[q_match.end():a_start]
    q_dict['choices'] = []
    q_dict['choices'].append({'opt': 'A', 'opt_text': q[a_end:b_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'B', 'opt_text': q[b_end:c_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'C', 'opt_text': q[c_end:d_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'D', 'opt_text': q[d_end:len(q)], 'is_correct': False})
    q_list[enum] = q_dict.copy()

for q in q_list:
    print(q['q_num'])
    print(q['q_txt'])
    for ch in q['choices']:
        print(ch['opt']+' '+ch['opt_text'], end=' ')
        print(ch['is_correct'])

print(f'There are {num_of_qs} questions in the data file')
