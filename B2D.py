#Converting Binary into Decimal
number=0
base=1
last=0
sums=0
number = int(input("Enter number: "))
while number:
    last = int(number%10)
    number = int(number/10)
    last *= base
    sums += last
    base *= 2
print(sums)
