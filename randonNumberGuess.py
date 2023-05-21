from random import randint

print("Welcome To Random Number Guess Game")
print("\n")
random_value = randint(1,50)
print(random_value)
game_on = True
while game_on == True:
      try:
        user_guess = int(input("Enter a random interger value between 1 and 50: "))
        if user_guess > random_value:
          print("Number given is higher than the randon value")
        elif user_guess < random_value:
          print("Number given is lower than the randon value")
        elif user_guess == random_value:
          print("Congratulations , Your given number matches the randon value")
          game_on = False
      except ValueError:
        print("Please enter a valid integer 1-10")
        continue

