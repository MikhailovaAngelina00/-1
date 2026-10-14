red = '\u001b[41m'
blue = '\u001b[44m'
reset = '\u001b[0m'
f = open ("sequence.txt")
num1 = 0
num2 = 0

for s in f:
    s = s.replace("\n","")
    s = float(s)
    if s >= -3 and s <= 3:
        num1 += 1
    else:
        num2 += 1
full = num1 + num2
print(f'{blue}{' ' * (num1//3)}{reset} {num1/full * 100}%')
print(f'{red}{' ' * (num2//3)}{reset} {num2/full * 100}%')

