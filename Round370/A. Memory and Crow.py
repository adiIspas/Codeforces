numbers = int(input())

a = []
b = []

a = list(map(int, input().split()))

for i in range(1, numbers):
    b.append(a[i - 1] + a[i])

b.append(a[numbers - 1])
print(" ".join(list(map(str, b))))
