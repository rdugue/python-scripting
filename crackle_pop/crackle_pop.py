def crackle_pop():
  number = 1
  crack_pop = None
  for number <= 100:
    if number % 3 == 0:
      crack_pop = "Crackle"
    if number % 5 == 0 and crack_pop is None:
      crack_pop = "Pop"
    elif number % 5 == 0:
      crack_pop = crack_pop + "Pop"
    print crack_pop
    number = number + 1
    crack_pop = None