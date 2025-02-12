# Step 1: Create variables for the bill, tip, and total
bill = input("Enter the bill amount: ")  # Bill amount will be input as a string
tip = input("Enter the tip amount: ")    # Tip amount will be input as a string

# Step 2: Convert the data types
bill = float(bill)  # Change the bill to a float
tip = int(tip)      # Change the tip to an integer

# Step 3: Calculate the total
total = bill + tip  # Total amount is the sum of bill and tip

# Step 4: Print the formatted string
print(f"The total bill is ${bill:.2f}, the tip is ${tip}, and the total amount paid is ${total:.2f}")