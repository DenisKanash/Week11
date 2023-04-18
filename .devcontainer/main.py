def modulo_calculator():
    #standart usage of %
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    remainder = dividend % divisor
    print(f"The remainder of {dividend} divided by {divisor} is {remainder}.")

def integer_division_calculator():
    #standart usage of division ( but in python we have to use //)
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    quotient = dividend // divisor
    print(f"The integer quotient of {dividend} divided by {divisor} is {quotient}.")

def for_loop_counter():
    #inputing everything 
    counter = float(input("What should be the initial value of the counter? "))
    loop_count = int(input("How many times should the loop run? "))
    increment = float(input("How much should the counter increment by? "))
    #bool
    is_positive = input("Should the counter decrement instead of incrementing? (y/n) ").lower() == 'n'

    # If not positive, make the increment negative
    if not is_positive:
        increment *= -1

    # Run the loop the specified number of times
    for i in range(loop_count):
        counter += increment

    print(f"The final value of the counter is {counter}")

def float_addition():
    #python not very good in decimals< thats why better to use les than 2 decimals
    # i also added option to add more than 1 value, just for fun
    num_values = int(input("How many values do you want to add together?\n"))
    #thats the way how to add more values in code
    values = [float(input(f"Enter value {i+1}: ")) for i in range(num_values)]
    #thats the way how to make summary without typing every digit
    result = sum(values)
    #thats like print and loop in one line
    print(f"The result of adding {', '.join(str(v) for v in values)} is {result}")
    return result

def print_ascii_values():
    #just converts< the same principle as C but different in writing
    string = input("Enter a string: ")
    #covertation is here
    ascii_values = [ord(char) for char in string]
    print(f"The ASCII values for {string} are {', '.join(str(v) for v in ascii_values)}")

def change_machine():
    #python has problems with decimals and therefore its necessary to use pennies
    #i used modulo because it fits great
    amount = float(input("Enter the amount of money in pennies you have: "))
    #layers of divider values ( pennies)
    quarters = int(amount / 25)
    dimes = int((amount % 25) / 10)
    nickels = int(((amount % 25) % 10) / 5)
    pennies = int((((amount % 25) % 10) % 5) / 1)
    print(f"You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")

def rock_paper_scissors():
    #input
    valid_choices = ['rock', 'paper', 'scissors']
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    #cases for all scenarios
    if player_choice not in valid_choices:
        print("Invalid choice.")
        return
    import random
    #i found sample of usage random. in internet ( for flip coin programm) 
    computer_choice = random.choice(valid_choices)
    print(f"Computer chooses {computer_choice}")
    #common if/else usage
    if player_choice == computer_choice:
        print("Tie!")
        #ways how to win
    elif (player_choice == 'rock' and computer_choice == 'scissors' or 
          player_choice == 'paper' and computer_choice == 'rock' or 
          player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        #every other case is the way how u loose
    else:
        print("Computer wins.")
def mario_wins():
    #it was difficult to find out the righ number of spaces , i had to try different amount many times, but for function is not so hard
    stairs = int(input("How many stairs should Mario climb to finish the level? "))
    #our flag
    print(" " * (stairs) + "  |>")
    #pyramid constractor
    for i in range(stairs):
        print(" " * (stairs - i - 1) + "#" * (i + 1) + "  |" )
    

#here is options
print("Choose one of the following options:")
print("1. Modulo Calculator")
print("2. Integer Division Calculator")
print("3. For Loop Counter")
print("4. Integer and Float Addition")
print("5. Print ASCII values of letters in a string")
print("6. Change Machine")
print("7. Rock Paper Scissors")
print("8. Mario wins a level")
#your choice
choice = int(input("Enter your choice (1-8): "))
#function start colomn
if choice == 1:
    modulo_calculator()
elif choice == 2:
    integer_division_calculator()
elif choice == 3:
    for_loop_counter()
elif choice == 4:
    float_addition()
elif choice == 5:
    print_ascii_values()
elif choice == 6:
    change_machine()
elif choice == 7:
    rock_paper_scissors()
elif choice == 8:
    mario_wins()
    #just in case
else:
    print("Invalid choice. Please enter a number between 1 and 8.")