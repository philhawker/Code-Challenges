from functools import reduce



num_list = [1, 2, 3, 4, 5, 6, 7, 8]


def average(num):
    sum = 0
    for n in num:
        sum = sum + n       

    avg = sum / len(num)
    return avg

print(average(num_list))
