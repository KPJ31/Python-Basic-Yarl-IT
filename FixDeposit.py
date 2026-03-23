amount = int(input("Enter Your Amount: "))
period = int(input("Enter Your Months: "))

while not (period == 3 or period == 6 or period == 12 or period > 12):
    print("Enter Valid Month 3 or 6 or 12 or morethan 12")
    period = int(input("Enter Your Months: "))

if period == 3:
    interest = ((amount * 0.15) / 12) * 3
    print(f"Your Amount Interest (3 months): {interest}")
    print(f"Your Got Total Amount: {amount + interest}")
elif period == 6:
    interest = ((amount * 0.13) / 12) * 6
    print(f"Your Amount Interest (6 months): {interest}")
    print(f"Your Got Total Amount: {amount + interest}")
elif period == 12:
    interest = amount * 0.10
    print(f"Your Amount Interest: {interest}")
    print(f"Your Got Total Amount: {amount + interest}")
else:
    interest = amount * 0.08
    print(f"Your Amount Interest: {interest}")
    print(f"Your Got Total Amount: {amount + interest}")
