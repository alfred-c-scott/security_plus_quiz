import re

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')
choice_a_pattern = re.compile(r'A\. ')
index_list = []
index_dict = {}


with open('ch_1_data') as f:
    data = f.read()
    new = data.replace('\n', ' ')
    new = new.replace('A. ', ' A. ').replace('  ', ' ')
    new = new.replace('B. ', ' B. ').replace('  ', ' ')
    new = new.replace('C. ', ' C. ').replace('  ', ' ')
    new = new.replace('D. ', ' D. ').replace('  ', ' ')
    new = new.replace(' A. ', '\nA. ')
    new = new.replace(' B. ', '\nB. ')
    new = new.replace(' C. ', '\nC. ')
    new = new.replace(' D. ', '\nD. ')
    # print(new)
    # for char in new:
    #     print(char, end='')
    ct = 1
    q_num_bool = q_num_pattern.search(new)
    q_num_matches = q_num_pattern.finditer(new)
    choice_a_bool = choice_a_pattern.search(new)
    choice_a_matches = choice_a_pattern.finditer(new)
    for match in q_num_matches:
        q_num = int(match.group()[0:len(match.group())-2])
        if ct == q_num:
            print(q_num, end=' ')
            print(ct)
            ct += 1

    num_of_qs = ct-1
    ct = 1
    print(num_of_qs)
    while ct <= num_of_qs:
        q_num_str = str(ct) + '. '
        new = new.replace(q_num_str, '\n'+q_num_str)
        # print(q_num_str)
        ct += 1
    print(new)
