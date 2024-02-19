# Restaurant Bill Calculator

# Get bill amount from user
bill_amount = float(input("What is the total on the bill?: "))

# Get tip percentage from user
tip_percentage = int(input("What % tip would you like to give?: "))

# Get number of people from user
number_of_people = int(input("How many people are sharing the bill?: "))

# Set tip amount to tip bill * (percentage / 100)
tip_amount = bill_amount * (tip_percentage / 100)
print(f"Tip amount: ${tip_amount:.2f}")

# Set total amount to bill amount + tip amount
total_bill = bill_amount + tip_amount
print(f"Total bill: ${total_bill:.2f}")

# Print tip per person
tip_per_person = tip_amount / number_of_people
print(f"Tip amount per person: ${tip_per_person:.2f}")

# Print total per person
total_amount_per_person = total_bill / number_of_people
print(f"Total amount per person: ${total_amount_per_person:.2f}")
