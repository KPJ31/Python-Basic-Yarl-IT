"""

print("line 1")
x = int(input("Enter Number: "))

if x != 10:
    print("line 2")
else:
    print("line 3")

"""

marks = int(input("Enter Your Marks: "))

while marks > 100 or marks < 0:
    print("Your marks error!")
    marks = int(input("Enter Marks: "))

if marks >= 75:
    print("A")
elif marks >= 65:
    print("B")
elif marks >= 55:
    print("C")
elif marks >= 45:
    print("D")
else:
    print("F")
