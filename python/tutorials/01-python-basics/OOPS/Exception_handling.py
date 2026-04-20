a = int(input("Enter the first Value: "))
b = int(input("Enter the Second Value: "))
d = -1
try:
    d = a/b
    c = "Ansh" + 35
except ZeroDivisionError as ze:
    print("Exception Occurred :",ze)
except TypeError as te:
    print("Exception Occurred :",te)

print("Division is :",d)