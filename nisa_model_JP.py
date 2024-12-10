print()
total = 0
count = 0
original = 0
want = int(input("いくらほしいですか？ (円): "))
monthly_invest = int(input("月にいくら投資しますか (万): ")) * 10000
interest_rate = int(input("利回り(金利) (%): ")) / 100
print()

while total < want:
    total += monthly_invest
    total += total * (interest_rate / 12)
    count += 1
    original += monthly_invest

years = count / 12

print(f"投資した場合: '{years:.2f}年' で目標金額に到達します!\n")

total = 0
count = 0

while total < want:
    total += monthly_invest
    count += 1

years = count / 12

print(f"投資しなかった場合: '{years:.2f}年' で目標金額に到達します!\n")

print(f"元本は {original:,} 円です。\n")