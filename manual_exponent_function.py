from functools import reduce

def manual_exponent(first_num, second_num):
  result = first_num ** second_num
  return result

print(manual_exponent(4, 4))


def manual_exponent_reduce(first_num, second_num):
  result = [first_num] * second_num
  return(reduce(lambda first_num, second_num: first_num * second_num, result))


print(manual_exponent_reduce(4, 2))


