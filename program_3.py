# Author: Joseph Kracht
# Last Modified: 9/15/2025
# Title: Age Categorizer

# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    if weight <= 2:
        price_per_pound = 1.5
    elif weight <= 6:
        price_per_pound = 3
    elif weight <= 10:
        price_per_pound = 4
    else:
        price_per_pound = 4.75

    shippingCost = weight*price_per_pound

    return shippingCost


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))
