from random import uniform

lowLimit = 1
highLimit = 100
amount = 1000000
listeL = [uniform(lowLimit, highLimit) for _ in range(amount)]

sorted = listeL.copy()
sorted.sort()
print(f"Liste: {listeL}")
print(f"Sortiert{sorted}")

sum = 0
for i in range(amount):
    sum += (listeL[i] - sorted[i])**2

if (amount <= 0):
    print(f"Ändere 'amount' für ein valides Resultat")
else:
    mse = sum / amount
    print(f"Der MSE beträgt: {mse}")