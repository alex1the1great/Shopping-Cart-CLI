cart = []


# add item to cart.
def add_item(item):
    cart.append(item)
    print(f'"{item}" has been added.')


# remove item from cart.
def remove_item(item_id):
    try:
        decrement_id = item_id - 1  # decrement -1. Option start with 1.
        print(f'"{cart[decrement_id]}" has been removed.')
        cart.pop(decrement_id)
    except IndexError:
        print('Sorry, Invalid option selected.')


# clear all items from cart.
def clear_cart():
    cart.clear()
    print('Cart has been clear.')


# show all items of cart.
def show():
    if cart:
        print('Shopping cart:')
        for index, item in enumerate(cart, start=1):  # accessing index & item
            print(f'{index}. {item}')
    else:
        print('The cart is empty.')


# main function to join all tasks.
def main():
    done = False
    while not done:
        print('-' * 50)  # line divider for UI.
        print('Shopping Cart. Choose:')
        try:
            user_option = int(input('1. Add 2. Remove 3. Clear 4. Show \
5. Quit -> '))  # breaking line to make it less than 79 characters.
            print('-' * 50)  # line divider for UI.

            # Quit
            if user_option == 5:
                print('Thanks for playing.')
                done = True
            # Add
            elif user_option == 1:
                new_item = input('Enter item to add to cart: ').title()
                add_item(new_item)
            # Remove
            elif user_option == 2:
                show()
                if cart:  # cart not empty
                    item_id = int(input('Choose an option: '))
                    remove_item(item_id)
            # Clear
            elif user_option == 3:
                clear_cart()
            # Show
            elif user_option == 4:
                show()
            else:
                print('Sorry, Invalid option selected.')
        except ValueError:
            print('Sorry, type number to choose the option.')


main()
