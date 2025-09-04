import random

rolls = 0

#loop
while True:
    #counter
        # Ask: roll dice
    choice = input ('Roll the dice (y/n): ').lower() #makes sure whatever the user types is lowercase
    if choice == 'y':
        rolls += 1
        #generate two random numbers
        dieOne = random.randint(1, 6)
        dieTwo = random.randint(1, 6)
        # and print them
        print (f'({dieOne},{dieTwo})')
    # if user choose n, 
    elif choice == 'n':
        print('Thank you for playing!')
        print(f'You rolled {rolls} time(s)')
    # end process
        break
    # else
    else:
        print('invalid choice.')
    # invalid choice

