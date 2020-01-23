"""
heading_generator(title, heading_type)
heading_generator('greeting', '1')
<h1> Greeting </h1>

heading_generator('Hi there', '3')
<h3> Hi There </h3>

"""


def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('greeting', 1))
print(heading_generator('Hello there good sir', 3))
