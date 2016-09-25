n = int(input())
colors = list(input())

red_first = 0
red_second = 0
black_first = 0
black_second = 0

for i in range(0, n):
    if colors[i] is 'r':
        if i % 2 is 0:
            red_second += 1
        else:
            red_first += 1
    elif colors[i] is 'b':
        if i % 2 is 0:
            black_second += 1
        else:
            black_first += 1

red = red_first + red_second
black = black_first + black_second

result = 0
if red > black:
    if not red_first > red_second:
        result = max(red_first, black_second)
    else:
        result = max(red_second, black_first)
else:
    if not black_first > black_second:
        result = max(black_first, red_second)
    else:
        result = max(black_second, red_first)

print(result)
