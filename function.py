# normal funciton
# def my_name():
#     print("My name is jana")

# my_name()

# parameterized function
# def my_name(name):
#     print("My name " + name)

# my_name("Jana")


# return function
# def get_fullname(fname, lname):
#     fullname = fname + " " + lname
#     return fullname

# full = get_fullname("Panchalingam", "Janarthan")
# print(full)

# def get_fullname(fname="Panchalingam", lname="Janarhtan"):
#     fullname = fname + " " + lname
#     return "My name is " + fullname

# full1 = get_fullname()
# full2 = get_fullname("Jana")
# full3 = get_fullname("Kumar", "Kamal")

# print(full1)
# print(full2)
# print(full3)


name = "Jana"

def my_name():
    global name
    
    print(f"My Name is {name}")

    name = "Janarthan"

my_name()

print("Global: " + name)