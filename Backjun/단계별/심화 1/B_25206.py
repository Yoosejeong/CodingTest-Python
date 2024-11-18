ratings= ["A+", "A0", "B+", "B0", "C+", "C0", "D+","D0", "F"]
nums = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total = 0
sum = 0
for i in range(20):
    b = float(b)
    a, b, c = input().split()
    if c == "P":
        continue
    index = ratings.index(c)
    sum += nums[index] * b
    total += b

print('%.6f' % (sum/total))