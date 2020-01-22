  
def fizz_buzz(max_num):
  for fizzbuzz in range(1, max_num + 1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
      print("fizzbuzz")
      continue
    elif fizzbuzz % 3 == 0:
      print("fizz")
      continue
    elif fizzbuzz % 5 == 0:
      print("buzz")
      continue
    print(fizzbuzz)
    

fizz_buzz(100)

