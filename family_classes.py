"""
Build three classes, two of which must inherit from the first and employ polymorphism. 
Between the three classes there must be at least 5 methods, 3 instance attributes, and 1 class attribute. 
Each class should have a dunder str and dunder representation, 
the parent class should have a dunder init.
"""

class Family:

    ethnicity = 'caucasian'

    def __init__(self, last_name, state, members):
        self.last_name = last_name
        self.state = state
        self.members = members
    
    def __str__(self):
        return f'This class represents the entire {self.last_name} family. We all live in {self.state} and there are {self.members} of us total.'


class HawkerFamily(Family):

    def __str__(self):
        return f'This is the {self.last_name} family. They live in {self.state} and consist of {self.members} members '

    def __repr__(self):
        return f'Last Name: {self.last_name}. Residents: {self.state}. Members: {self.members}'



class BenedictFamily(Family):

    def __str__(self):
        return f'This is the {self.last_name} family. They live in {self.state} and consist of {self.members} members '

    def __repr__(self):
        return f'Last Name: {self.last_name}. Residents: {self.state}. Members: {self.members}'



class ValasquezFamily(Family):

    def __str__(self):
        return f'This is the {self.last_name} family. They live in {self.state} and consist of {self.members} members '

    def __repr__(self):
        return f'Last Name: {self.last_name}. Residents: {self.state}. Members: {self.members}'






entire_family = Family('Mounteer', 'Utah', '17')
hawkers = HawkerFamily('Hawker', 'Utah', '3')
benedict_fam = BenedictFamily('Benedict', 'Utah', '5')
valasquez_fam = ValasquezFamily('Valasquez', 'Texas', '3')




print(str(entire_family))
print(str(hawkers))
print(repr(hawkers))
print(str(benedict_fam))
print(repr(benedict_fam))
print(str(valasquez_fam))
print(repr(valasquez_fam))
