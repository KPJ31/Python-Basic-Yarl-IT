marks = int(input("Enter Your Marks: "))

'''
if marks<0 or marks>100:
    print("Your marks is Error")
else:
    if marks>=50:
        print("Pass")
    else:
        print("Fail")
        
'''
        
if marks>=0 and marks<=100:
    if marks>=75:
        print("A")
    elif marks>=65:
        print("B")
    elif marks>=55:
        print("C") 
    elif marks>=45:
            print("S")  
    else:
        print("W")
else:
    print("Your marks is Error")
 