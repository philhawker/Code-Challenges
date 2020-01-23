### Coding Challenge: Palindrome Checker:

# Create a function called 'check' that checks if a word in a string is a palindrome.

# Sample output:
# output: Type out a word or a sentence:
# input: "racecar is a cool word lol"
# output: 'racecar' is a palindrome!
# 'a' is a palindrome!
# 'lol' is a palindrome!



def check(string):
  rev_string = reversed(string)

  if list(string) == list(rev_string):
    return f'The word "{string}," is a palindrome'
  else:
    return f'The word "{string}," is not a palindrome...'
    

print(check('racecar'))


### Create a function and pass in kwargs to print out a first name, middle name, and last name.
# Sample output:

# first == Kent

# mid == James

# last == Potter

def name_list(**kwargs):
  if kwargs: 
    for val, key in kwargs.items():
      print(f'{val} == {key}')



print(name_list(
  first = 'Phil',
  mid = 'Kelsey',
  last = 'Sadie',
))
