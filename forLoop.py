"""
for i in range(5):
  print(i)

print(10*"-")

for j in range(1, 5):
    print(j)

print("------------------")
   
for k in range(1, 11, 2):
    print(k)


for a in "Jana":
    print(f"{a}")


for a in "Jana":
    print(f"{a}, ",end="")
    


for i in range(1,6):
    for j in range(1,4):
        print(f"j{j}", end=" ")
    print(f"i{i}")


print(list(range(1, 6, 2)))

for i in range(1, 11):
    if 1%2==1:
        print(i)
            


for i in range(1, 11):
    if 1%2==1:
        continue
    print(i)
    
"""

for i in range(1, 11):
    if 1%2==1:
        break
    print(i)