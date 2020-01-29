import operator
from functools import reduce
import itertools

# dynamic_reducer([1, 2, 3], '+') # 6
# dynamic_reducer([1, 2, 3], '-') # -
# dynamic_reducer([1, 2, 3], '*') # 6
# dynamic_reducer([1, 2, 3], '/') # -

num_list = [1, 2, 3]


def flexible_counter(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)


total = flexible_counter([1, 2, 3], '/')  # 0.16666666666666666

print(total)



