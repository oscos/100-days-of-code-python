print("Welcome to the tip calculator.")
bill_amount = float(input("What was the bill amount? "))
tip_percentage = float(input("What percentage tip do you want to give? "))
number_of_people = int(input("How many people are splitting the bill? "))
total_bill = bill_amount + (bill_amount * (tip_percentage / 100))
cost_per_person = total_bill / number_of_people
print(f"Each person should pay {cost_per_person:.2f}")
