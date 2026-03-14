import random
computer_number=random.randint(1,10)
attempts=0
score=100
print("guess the number between 1 and 9")
while True:
    guess=input("enter your guess (or type 'exit' to 'quit')")
    if guess.lower()=="exit":
        print("game exited.")
        print("computer number was:",computer_number)
        print("final score:",score)
        break
    if not guess.isdigit():
        print("please ente a valid number:")
        continue
    guess=int(guess)
    attempts+=1
    if guess==computer_number:
        print(f"correct! you guessed it in {attempts} attempts")
        score+=10
        print("your score",score)
        break
    else:
        score-=10
        if guess<computer_number:
            print("too low! Try again.")
        else:
            print("too high! Try again.")
        print("your score is:",score)
