# challenge one 

string_one = 'mississippi'
string_two = 'f'

def butthole(str):
  if str[:5]:
    print(str[:2] + str[-2:])
  if str[:3]:
    print(str[:2] + str[:2])
  if str[:1]:
    str = 'Empty String'
  print(str)

butthole(string_one)


# ````

# challenge two
word = 'restart'


def specialreplace(r):
  chars = [('$' if c == r[0] else c) for c in r[1:]]
  print (r[0] + ''.join(chars))

print(specialreplace(word))

# ````

# challenge three

greeting = 'Hello'

new_greeting = ''.join(reversed(greeting))

print(new_greeting)



# ````