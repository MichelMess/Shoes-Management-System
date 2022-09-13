# This software creates a shoes management system.
import sys

# This bit of code creates a class name shoes
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# A function to get cost and quantity is created here.
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'{self.country} {self.code} {self.product} {self.cost} {self.quantity}'

shoes = []

'''
▪ read_shoes_data - this function will open the file
inventory.txt and read the data from this file, creates a shoes 
object and append this object into the shoes list. One line in
this file represents data to create one object of shoes. You 
must use the try except in this function for error handling.'''

def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as f:
            for line in f:
                # don't read the header line
                if not line.startswith('Country'):
                    line = line.strip().split(',')
                    shoes.append(Shoes(line[0], line[1], line[2], line[3], line[4]))
    except FileNotFoundError:
        print('File not found')
        sys.exit()

'''capture_shoes - this function will allow a user to capture
data about a shoe and use this data to create a shoe object
and append this object inside the shoe list.'''

def capture_shoes():
    country = input('Enter country: ')
    code = input('Enter code: ')
    product = input('Enter product: ')
    cost = input('Enter cost: ')
    quantity = input('Enter quantity: ')
    shoes.append(Shoes(country, code, product, cost, quantity))
    with open('inventory.txt', 'a') as f:
        f.write(f'\n{country},{code},{product},{cost},{quantity}')

'''view_all - this function will iterate over all the shoes list and
print the details of the shoes that you return from the __str__
function.'''

def view_all():
    for shoe in shoes:
        print(shoe)

'''re_stock - this function will find the shoe object with the
lowest quantity, which is the shoes that need to be
restocked. Ask the user if he wants to add the quantity of
these shoes and then update it. This quantity should be
updated on the file for this shoe.'''

def re_stock():
    lowest_quantity = min(shoes, key=lambda shoe: int(shoe.get_quantity()))
    print(lowest_quantity)
    quantity = input('Enter quantity: ')
    lowest_quantity.quantity = quantity
    with open('inventory.txt', 'w') as f:
        for shoe in shoes:
            f.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n')


'''search_shoe - This function will search for a shoe from the list
using the shoe code and return this object so that it will be
printed'''

def search_shoe(code):
    for shoe in shoes:
        if shoe.code == code:
            print(shoe)
            return

'''value_per_item - this function will calculate the total value
for each item. (formula for value: value = cost * quantity). Print this information on the
console for all the shoes.'''

def value_per_item():
    for shoe in shoes:
        value = float(shoe.cost) * float(shoe.quantity)
        print(f'{shoe.product} {value}')

'''highest_qty - determine the product with the
highest quantity and print this shoe as being for sale'''

def highest_qty():
    highest_quantity = max(shoes, key=lambda shoe: int(shoe.get_quantity()))
    print(highest_quantity)

def main():
    '''In main create a menu that executes each function
above. This menu should be inside the while loop.'''
    while True:
        print('1. Read shoes data')
        print('2. Capture shoes')
        print('3. View all shoes')
        print('4. Re-stock shoes')
        print('5. Search shoe')
        print('6. Value per item')
        print('7. Highest quantity')
        print('8. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            code = input('Enter code: ')
            search_shoe(code)
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            sys.exit()
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
