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
    print(f'The word "{string}," is a palindrome:')
  else:
    print(f'The word "{string}," is not a palindrome...')
    


check('racecar')



