import math


name = "Adrian"
ordNumbers = []
for i in name:
    ordNumbers.append(ord(i))

product = 1
quotient = 0
for i in ordNumbers:
    product *= i
    quotient += i
secretNumber = product / quotient
print(f"Verschlüsselter Name: {math.floor(secretNumber)}")
