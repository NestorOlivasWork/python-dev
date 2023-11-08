import math
print("Calculates LCM two numbers\n")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
lcm = (a * b / math.gcd(a, b))
print("Least Common Multiple: ", lcm)
print("hello")