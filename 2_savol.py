import math
a = [21,34,55,12,3,5,234,43]
count = 0
for num in a:
    if num > 1 and math.sqrt(num) ** 2 == num:
        count += 1
print (count)

