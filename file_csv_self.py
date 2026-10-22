#import os

def curr_cal(pln):

    my_file = 'rates.csv'
    dict_cur = {}
    cur_lst = []
    with open(my_file,'r') as f:
        lines = f.readlines()
        for line in lines:
            cur_lst.append(line.strip())

        cur_lst = cur_lst[1:]
        print(f"Currency rates from the file:\n{cur_lst}")

    for item in cur_lst:
        key, value = item.split(',')
        dict_cur[key] = round(float(value)*pln,2) #not rounding off is giving more decimal
                                                # values for a couple of values
    print(f"Currency value after applying the conversion rates:\n{dict_cur}")


curr_cal(5)