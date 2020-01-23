import random

print('\nWelcome to Camel!')
print('You have stolen a camel to make your way across the great Gobi desert.')
print('The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.')


done             = False
miles_traveled   =   0 # Total miles you traveled
thirst           =   0 # Level of your thirsty
camel_tiredness  =   0 # Level of camel tiredness
natives_traveled = -20 # Start point of natives
num_of_drinks    =   3 # Number of drinks in canteen
nm = miles_traveled - natives_traveled # Distance between you and the natives


while not done:
    print('\nA. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night')
    print('E. Status check.')
    print('Q. Quit.\n')

    user_choice = input('Your choice: ').upper()

# --- Checking user's input and setting levels
    if user_choice == 'Q':
        done = True

    elif user_choice == 'E':
        nm = miles_traveled - natives_traveled
        print('Miles traveled:', miles_traveled)
        print('The natives are', nm, 'miles behind you.')
        print('Camel tiredness:', camel_tiredness)
        print('Drinks in canteen:', num_of_drinks)
        print('Thirsty level:', thirst)

    elif user_choice == 'D':
        camel_tiredness = 0
        natives_traveled = natives_traveled + random.randrange(7, 15)
        print('Thanks for the rest. Your camel is happy')

    elif user_choice == 'C':
        full_speed_miles = random.randrange(10, 21)
        miles_traveled = miles_traveled + full_speed_miles
        natives_traveled = natives_traveled + random.randrange(7, 15)
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1, 4)
        print('You traveled:', full_speed_miles)

    elif user_choice == 'B':
        moderate_miles = random.randrange(5, 13)
        natives_traveled = natives_traveled + random.randrange(7, 15)
        miles_traveled = miles_traveled + moderate_miles
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + 1
        print('You traveled:', moderate_miles)

    elif user_choice == 'A':
        if num_of_drinks > 0:
            thirst = 0
            num_of_drinks = num_of_drinks - 1
        else:
            print('There are no drinks left')

# --- Checking if you are thirsty.
    if thirst in range(3, 7):
        print('You are thirsty')
    elif thirst > 6:
        print('You died of thirst!')
        done = True

# --- Checking if your camel is tired
    if camel_tiredness in range(4, 9):
        print('Your camel is getting tired. Take a rest')
    elif camel_tiredness > 8:
        print('Your camel is dead')
        done = True

# --- Checking if natives getting close
    if nm <= 0:
        print('The natives have caught you up. You lose.')
        done = True
    elif not done and nm <= 15:
        print('The natives are getting close!')

# --- Checking if you approached the end of the desert
    if miles_traveled >= 250:
        print('You made it accross the desert! You won!')
        done = True


print('Game over')
