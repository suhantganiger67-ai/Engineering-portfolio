print("Welcome to the tip calculator!")
bill = float(input("what is your bill?\n$"))
tip = int(input("What is your tip percentage? 10%,15% or 20%\n"))
people = int(input("How many people are spliting?\n"))

tip_percentage = int(tip/100+1)
bill_percentage = int(bill/100+1)

tip_amount = round(((bill/people)*tip_percentage),2)

print(f"each person should pay {tip_amount}" )