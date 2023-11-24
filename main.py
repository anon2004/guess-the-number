
from random import randint
number=randint(1,100)
counter=0

while True:
  guess=int(input("Guess a number between 1 and 100: "))
  counter=counter+1
  if guess<0:
    exit()

  if guess>number:
     print("Too high Try again")
     continue
  elif guess<number:
    print("Too low Try again")
    continue
  else:
   break
print(f"You got it {number} after {counter} attempts!")
