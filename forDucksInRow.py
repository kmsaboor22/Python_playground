#For loops

rice = 1
total = 0

for i in range(1,65):
    total += rice
    print("The amount of the rice on square", i, "is: ", rice)
    print("Out total amount of the rice is:", total)
    rice = rice * 2