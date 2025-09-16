# Author: Joseph Kracht
# Last Modified: 9/16/2025
# Title: Hot Dog Price

def get_hot_dog_price():
    # Get hot dog type
    hot_dog_type = input('Enter Hot Dog Type("Hot Dog" or "Chili Dog"): ')

    # Set hot dog initial price
    if hot_dog_type == "Hot Dog":
        hot_dog_subtotal = 3.5
    else:
        hot_dog_subtotal = 4.5

    # Check if cheese is ordered
    cheese = input('Do you want cheese("yes" or "no"): ')
    if cheese == "yes":
        hot_dog_subtotal += .5

    # Check if peppers are ordered
    peppers = input('Do you want peppers("yes" or "no"): ')
    if peppers == "yes":
        hot_dog_subtotal += .75

    # Check if grilled onions are ordered
    grilled_onions = input('Do you want grilled onions("yes" or "no"): ')
    if grilled_onions == "yes":
        hot_dog_subtotal += 1

    # Calculate the sales tax
    sales_tax = hot_dog_subtotal * .07 # .07 represents the tax precent

    # Calculate the total
    total = hot_dog_subtotal + sales_tax

    # Display subtotal, sales tax and total
    print(f'Subtotal:  ${hot_dog_subtotal:,.2f}')
    print(f'Sales Tax: ${sales_tax:,.2f}')
    print(f'Total:     ${total:,.2f}')


# Call the above function.
get_hot_dog_price()
