import re

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')
choice_a_pattern = re.compile(r'A\. ')

q_list = []
q_dict = {}

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
    print(f_data)
    print(f'There are {num_of_qs} questions in the data file')

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

for q in q_list:
    print(q)


