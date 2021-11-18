##Project16: FizzBuzz Game
## Children sit around a circle
#each child will spell in a spell.If the number is divisible by 3 ,instead of saying the number they will say "Fizz".
#similarly if the number is divisible by 5 they say "Buzz" and the number is divisible by both 3 and 5 they say "FizzBuzz".

##Write a program for this game and the number start from 1 and end at 100 including 100.

for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)