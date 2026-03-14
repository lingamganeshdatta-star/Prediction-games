def guess_number(length):
    print("think of your phone number. I will guess it digit by digit")
    guessed_number=""
    for position in range(1,length+1):
        possible_digits=list(range(10))
        print("guessing your phone number.......")
        while len(possible_digits)>1:
            mid=len(possible_digits)//2
            first_half=possible_digits[:mid]
            second_half=possible_digits[mid:]
            print(f"is your digit in this group? {first_half}")
            answer=input("enter yes/no:").lower()
            if answer=="yes":
                possible_digits=first_half
            else:
                possible_digits=second_half

        digit=str(possible_digits[0])
        guessed_number+=digit
        
    print("your phone number is:",guessed_number)
guess_number(10)
        
