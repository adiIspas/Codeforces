x1, x2, x3 = list(map(int, input().split()))

average = (x1 + x2 + x3) / 3

final_point = max(x1, average) - min(x1, average) + max(x2, average) - min(x2, average) + max(x3, average) - min(x3, average)

print(int(final_point))