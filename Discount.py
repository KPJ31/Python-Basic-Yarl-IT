"""
amount = float(input("Enter Your Bill Ammount: "))

if amount >= 10000 and amount < 15000:
    discount = amount * 0.03
    print("Youre Discount: " + str(discount))
    print("Total Bill: " + str(amount - discount))
elif amount >= 15000 and amount < 25000:
    discount = amount * 0.05
    print("Youre Discount: " + str(discount))
    print("Total Bill: " + str(amount - discount))
elif amount >= 25000 and amount < 50000:
    discount = amount * 0.07
    print("Youre Discount: " + str(discount))
    print("Total Bill: " + str(amount - discount))
elif amount >= 50000:
    discount = amount * 0.1
    print("Youre Discount: " + str(discount))
    print("Total Bill: " + str(amount - discount))
else:
    print("No Discount")
    print("Total Bill: " + str(amount))
"""

amount = float(input("Enter Your Bill Amount: "))

if amount >= 10000 and amount < 15000:
    discount = amount * 0.03
    print(f"Your Discount: {discount}")
    print(f"Total Bill: {amount - discount}")

elif amount >= 15000 and amount < 25000:
    discount = amount * 0.05
    print(f"Your Discount: {discount}")
    print(f"Total Bill: {amount - discount}")

elif amount >= 25000 and amount < 50000:
    discount = amount * 0.07
    print(f"Your Discount: {discount}")
    print(f"Total Bill: {amount - discount}")

elif amount >= 50000:
    discount = amount * 0.10
    print(f"Your Discount: {discount}")
    print(f"Total Bill: {amount - discount}")

else:
    print("No Discount")
    print(f"Total Bill: {amount}")