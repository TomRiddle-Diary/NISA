total = 0
count = 0
want = int(input("How much money you want?: "))
monthly_invest = int(input("How much you invest per month? (万): ")) * 10000
interest_rate = int(input("Interest Rate (%): ")) / 100

while total < want:
    total += monthly_invest
    total += total * (interest_rate / 12)
    count += 1

years = count / 12

print(f"You will reach {want:,} yen in {years:.2f} years if you invest.")

total = 0
count = 0

while total < want:
    total += monthly_invest
    count += 1

years = count / 12

print(f"You will reach {want:,} yen in {years:.2f} years if you just saving.")





