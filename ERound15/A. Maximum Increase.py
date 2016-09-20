number = int(input())

numbers = list(map(int, input().split()))

a = numbers[0]
maxim = 1
current_maxim = 1
for i in range(1, number):
    b = numbers[i]
    if a < b:
        current_maxim += 1
    else:
        current_maxim = 1
    a = b

    if current_maxim > maxim:
        maxim = current_maxim

print(maxim)


