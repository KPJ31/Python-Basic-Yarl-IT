waterLiters = int(input("Enter water consumption in liters: "))

while waterLiters<0:
    print("Enter Valid Liters!!!")
    waterLiters = int(input("Enter water consumption in liters: "))


if waterLiters <= 10000:
    payment = 1500
elif waterLiters <= 30000:
    payment = 1500 + ((waterLiters - 10000) * 5)
elif waterLiters <= 60000:
    payment = 1500 + (20000 * 5) + ((waterLiters - 30000) * 7)
else:
    payment = 1500 + (20000 * 5) + (30000 * 7) + ((waterLiters - 60000) * 7)
    tax = payment * 0.03
    payment = payment + tax
    print(f"Water Bill Tax: {tax:.2f}")
print(f"Your Water Bill: {payment:.2f}")
