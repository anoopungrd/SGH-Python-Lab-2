import csv


def cur_calculator(file_name,pln):
    cur_con = {}
    with open(file_name,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  #to skip the header
        csv_dict = dict(csv_reader)
        print(f"The exchange rates of the target currencies:\n{csv_dict}")

    for key, value in csv_dict.items():
        cur_con[key] = round(float(value)*pln,2)


    print(f"The currency equivalent of {pln} pln:\n{cur_con}")



cur_calculator('rates.csv',5)