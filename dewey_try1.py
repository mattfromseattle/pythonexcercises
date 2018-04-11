'''
1. Prompt your user to decide if your program should print 'beer' or something else to the screen. - DONE.
2. Prompt user for that something else. - DONE.
3. Create a loop to print your song repeatedly. You should only have to write print statements for one verse. - DONE.
4. Use variables appropriately to populate the beverage. - DONE.
'''

def try_one():
    singAboutBeer = input ('Would you like to sing about beer? ') # Asks the user if they want to sing about beer
    singAboutBeer = singAboutBeer.lower()
    if singAboutBeer == 'no':
        drinkChoice = input('What drink would you like to sing about? ') # Sets the drink choice the user wants to sing about.
    else: drinkChoice = 'beer'
    bottles = 99
    while int(bottles) > 0:
        print('\n', bottles, 'bottles of ' + drinkChoice + ' on the wall.' + '\n', bottles, 'bottles of ' + drinkChoice + '.' + '\n', 'Take one down, pass it around,')
        bottles = bottles - 1
        print('\n', bottles, 'bottles of ' + drinkChoice + ' on the wall' + '\n')
    if int(bottles) == 1:
        print(bottles, 'bottle of ' + drinkChoice + ' on the wall.' + '\n', bottles, 'bottle of ' + drinkChoice + '.' + '\n', 'Take one down, pass it around,')
        bottles = bottles - 1
        print(bottles, 'bottle of ' + drinkChoice + ' on the wall' + '\n')
    elif bottles <= 0:
        print('\n', 'No more bottles of ' + drinkChoice + ' on the wall, no more bottles of beer.' + '\n' + 'Go to the store and buy some more, 99 bottles of ' + drinkChoice + ' on the wall!')
try_one()