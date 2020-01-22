  
def fizz_buzz(max_num):
  for organizer in range(1, max_num + 1):
    if organizer % 3 == 0 and organizer % 5 == 0:
      print("fizzbuzz")
      continue
    elif organizer % 3 == 0:
      print("fizz")
      continue
    elif organizer % 5 == 0:
      print("buzz")
      continue
    print(organizer)
    

fizz_buzz(100)

