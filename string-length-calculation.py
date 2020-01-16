sentence = 'calculate how long i am'


def get_string_length(str):
  counter = 0
  for i in str:
    counter += 1
  return counter

print(get_string_length(sentence))