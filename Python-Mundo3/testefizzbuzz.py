c1 = c2 = c3 =  0
for c in range(1, 101):
    if c % 3 == 0:
      c = 'Fizz'
      print(f'{c}')
    elif c % 5 == 0:
     c = 'Buzz'
     print(c)
    else:
        print(c)

