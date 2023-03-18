for zero_to in range(151):
    print("Basic", zero_to)

for five_to in range(5, 1005, 5):
    print("Multiple of five", five_to)

for one_to_hund in range(1, 101):
    if one_to_hund % 10 == 0:
        print("Coding Dojo")
    elif one_to_hund % 5 == 0:
        print("Coding")
    else:
        print(one_to_hund)

sum = 0
for to_five_k in range(1, 500000, 2):
    sum = sum + to_five_k
print(sum)

by_four = 2018
while by_four > 0:
    print("countdown by", by_four)
    by_four -= 4 


lowNum = 2 
highNum = 9
mult = 3

while lowNum <= highNum:
    if lowNum % mult == 0:
        print("multiple of three", lowNum)
    lowNum += 1

"""
low = 2
high = 9
mult = 3

for i in range(low,high + 1):
    if i % mult == 0:
        print(i)"""
