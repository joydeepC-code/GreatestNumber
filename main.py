x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x > y and x > z:
    print(x, "is the greatest")

elif y > x and y > z:
    print(y, "is the greatest")

elif z > x and z > y:
    print(z, "is the greatest")