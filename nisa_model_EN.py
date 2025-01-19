print()
total = 0
count = 0
original = 0
want = int(input("How much money you want? (USD): "))
monthly_invest = int(input("How much you invest per month? (USD): "))
interest_rate = int(input("Interest Rate (Expected Return) (%): ")) / 100
print()

while total < want:
    total += monthly_invest
    total += total * (interest_rate / 12)
    count += 1
    original += monthly_invest

years = count / 12

print(f"You will reach ${want:,} in '{years:.2f}' years if you invest.")

total = 0
count = 0

while total < want:
    total += monthly_invest
    count += 1

years = count / 12

print(f"You will reach ${want:,} in '{years:.2f}' years if you just saving.\n")

print(f"Your original money is {original:,}\n")





