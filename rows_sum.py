from pip._internal.commands import index
arr_a = [[1,4,6], [6,9,3],[2,7,9]]

sum_r=0
for row in arr_a: #sum of each row
    print(f" Sum of each row: {sum(row)}")

for row in arr_a: #sum of all rows
    for row1 in row:
        sum_r = sum_r+row1
print(f" Sum of all rows: {sum_r}")


def sum_rows(arr):
    sum_r=0
    for row in arr:
        print(f" Sum of each row: {sum(row)}")

    for row in arr:
        for row1 in row:
            sum_r = sum_r+row1
    print(f" Sum of all rows: {sum_r}")


sum_rows(arr_a)

