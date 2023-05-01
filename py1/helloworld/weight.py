a = float(input("weight: "))
b = input("(k)g or (L)bs: ")
if b.upper() == "K":
    c = a / 0.45
    print("weight in lbs: " + str(c))
else:
    c = a * 0.45
    print("weight in kg: " + str(c))
