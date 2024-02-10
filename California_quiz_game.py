print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play.")
score = 0

answer = input('What is the capital of California? ')
if answer.lower() == 'sacramento':
    print('Correct!')
    score += 1
else: 
    print('Try again!')

answer = input("What is the name of California's most famous National Park? ")
if answer.lower() == 'yosemite':
    print('Correct!')
    score += 1
else: 
    print('Almost!') 

answer = input('Which famous basketball team is in Los Angeles? ')
if answer.lower() == 'the lakers':
    print('Correct!')
    score += 1
else: 
    print('Oops! Not quite.')       

answer = input('Which body of water borders California to the west? ')
if answer.lower() == 'the pacific':
    print('Correct!')
    score += 1
else: 
    print('Try again!')    

answer = input('What is the name of the Famous Bridge? ')
if answer.lower() == 'golden gate bridge':
    print('Correct!')
    score += 1
else: 
    print('Oh no! Try again!')    

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score * 20)) + '%')
