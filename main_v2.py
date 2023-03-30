import re

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')
choice_a_pattern = re.compile(r'A\. ')


with open('ch_1_data') as f:
    f_data = f.read()
    f_data = f_data.replace('\n', ' ')
    ct = 1
    q_num_bool = q_num_pattern.search(f_data)
    q_num_matches = q_num_pattern.finditer(f_data)
    choice_a_bool = choice_a_pattern.search(f_data)
    choice_a_matches = choice_a_pattern.finditer(f_data)
    for match in q_num_matches:
        q_num = int(match.group()[0:len(match.group())-2])
        if ct == q_num:
            ct += 1

    num_of_qs = ct-1
    ct = 1
    print(num_of_qs)

    while ct <= num_of_qs:
        q_num_p = re.compile(rf'{str(ct)}\. ')
        if not re.search(q_num_p, f_data):
            print('No')
        match = re.search(q_num_p, f_data)
        start = match.start()
        if match.group() != '1. ':
            f_data = f_data[:int(match.start())]+'\n'+f_data[int(match.start()):]
        ct += 1
    print(f_data)
