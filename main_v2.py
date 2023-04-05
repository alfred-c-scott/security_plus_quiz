import re
import json

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')

q_list = []
in_files = ['ch_1_data', ]


def make_q_dict(question):
    f_c_pattern = re.compile(r' [ABCD]\. ')
    c_match = f_c_pattern.finditer(question)
    q_match = q_num_pattern.search(question)
    q_dict = {}
    q_dict['full_str'] = q
    q_dict['q_num'] = int(q_match.group()[q_match.start():q_match.end() - 2])
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
    q_dict['q_txt'] = q[q_match.end():a_start]
    q_dict['choices'] = []
    q_dict['choices'].append({'opt': 'A', 'opt_text': q[a_end:b_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'B', 'opt_text': q[b_end:c_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'C', 'opt_text': q[c_end:d_start], 'is_correct': False})
    q_dict['choices'].append({'opt': 'D', 'opt_text': q[d_end:len(question)], 'is_correct': False})
    return q_dict


for file in in_files:
    with open(file) as f:
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

    # updated pattern after reformat of f_data
    # f_c_pattern = re.compile(r' [ABCD]\. ')

    for enum, q in enumerate(q_list):
        q_list[enum] = make_q_dict(q)

    # for enum, q in enumerate(q_list):
    #     c_match = f_c_pattern.finditer(q)
    #     q_match = q_num_pattern.search(q)
    #     q_dict = {}
    #     q_dict['full_str'] = q
    #     q_dict['q_num'] = int(q_match.group()[q_match.start():q_match.end()-2])
    #     a_start = None
    #     a_end = None
    #     b_start = None
    #     b_end = None
    #     c_start = None
    #     c_end = None
    #     d_start = None
    #     d_end = None
    #     for c in c_match:
    #         if c.group() == ' A. ':
    #             a_start = c.start()
    #             a_end = c.end()
    #         if c.group() == ' B. ':
    #             b_start = c.start()
    #             b_end = c.end()
    #         if c.group() == ' C. ':
    #             c_start = c.start()
    #             c_end = c.end()
    #         if c.group() == ' D. ':
    #             d_start = c.start()
    #             d_end = c.end()
    #             pass
    #     q_dict['q_txt'] = q[q_match.end():a_start]
    #     q_dict['choices'] = []
    #     q_dict['choices'].append({'opt': 'A', 'opt_text': q[a_end:b_start], 'is_correct': False})
    #     q_dict['choices'].append({'opt': 'B', 'opt_text': q[b_end:c_start], 'is_correct': False})
    #     q_dict['choices'].append({'opt': 'C', 'opt_text': q[c_end:d_start], 'is_correct': False})
    #     q_dict['choices'].append({'opt': 'D', 'opt_text': q[d_end:len(q)], 'is_correct': False})
    #     # must pass copy
    #     q_list[enum] = q_dict.copy()

for q in q_list:
    print(q['q_num'])
    print(q['q_txt'])
    for ch in q['choices']:
        print(ch['opt']+' '+ch['opt_text'], end=' ')
        print(ch['is_correct'])

print(f'There are {num_of_qs} questions in the data file')

json_object = json.dumps(q_list, indent=4)
print(json_object)
with open ('ch_2.json', 'w') as out_f:
    json.dump(json_object, out_f)
