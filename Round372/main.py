number, c = list(map(int, input().split()))

seconds = list(map(int, input().split()))

words = 0
for i in range(0, number - 1):
    a = seconds[i]
    b = seconds[i + 1]

    if b - a <= c:
        words += 1
    if b - a > c and words > 0:
        words = 0

words += 1
print(words)

