

print("Starting tip calculator program")

food_charge = input("Enter food charge ")
print(f'Food charge is ${food_charge}')

eighteen_percent = (18/100)
seven_percent = (7/100) 

tip = float(food_charge) * eighteen_percent
print(f'Tip = ${tip}')
sales_tax = float(food_charge) * seven_percent
print(f'Sales tax = ${sales_tax}')
total_charge = tip + sales_tax + float(food_charge)
print(f'Grand total = ${total_charge}')

