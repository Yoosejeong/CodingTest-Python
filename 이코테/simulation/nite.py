s=input()
row = int(s[1])
col = int(ord(s[0]))-int(ord('a'))+1
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2,1), (1,2), (-1, 2), (-2, 1)]
result = 0
for i in steps:
    next_row = row+i[0]
    next_col = col+i[1]
    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        result +=1
print(result)