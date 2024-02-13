name = input('Please type your name: ')
print("Welcome to your adventure,", name + '!')

answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input ('You come to a river. You can walk around it, or swim across it. Type walk to walk around, or swim to swim across: ')

    if answer == "swim": 
        print("You swim across and were eaten by a river shark")
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and eventually turned into Golem')
    else: 
        print('Not a valid option. You lose.')
    
elif answer == 'right':
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross or head back? (Type cross or head back) ")

    if answer == "head back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes": 
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You LOSE!")
            
else: 
    print('Not a valid option. You lose.')

print("Thanks for playing,", name + '!')