''' CHALLENGE 4: Build a food ordering system where the user inputs the food name into the food order and
then the order gets  passed to the appropriate restaurant on a listand the restaurant prints the receipt on stdout.
No need to create a  UI, a main function that receives parameters is enough.'''

import sys# mports the sys module to use sys functions
while True:# while loop to continuously ask for inputs
    # dictionary that contains the list of foods, restaurants and prices
    resto_dict = {'burger':['Burger King','Cheese Burger','$10'],
                  'pizza':['Awesome Pizza Place','Pepperoni Pizza','$20'],
                  'pasta':['Italliani\'s Pasta Place', 'Bolognese Spaghetti', '$30'],
                  'chicken': ['Gami Chicken Place', 'Chicken Wings', '$30'],
                  'pho':['Thuan An Pho Restaurant', 'Beef and Vegetable Pho', '$20'],
                  'ramen':['Shunjiko Ramen', 'Shunjiko Tonkatsu Ramen', '$18']}
    sys.stdout.write('-'*60+'\n')
    sys.stdout.write('Selection: ')
    # for loop that prints the selection for the food items
    for items in resto_dict.keys():
        sys.stdout.write('[' + items + ']')
    sys.stdout.write('\nPlease input your preferred food: ')
    food = sys.stdin.readline().strip().lower()# converts the input to lowercase and removes extra spaces
    # conditional loop to check if input is stored in dictionary, if it is the restaurant and prices will be
    # printed, otherwise, it will ask for another input
    if food in resto_dict.keys():
        value = ', '.join(resto_dict[food])
        sys.stdout.write(value)
        sys.stdout.write('\n')
    else:
        sys.stdout.write('Please enter a valid food item from the selection.')
