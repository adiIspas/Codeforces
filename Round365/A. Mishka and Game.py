number = int(input())

winMishka = 0
winChris = 0

for _ in range(0, number):
    numbers = list(map(int, input().split()))

    if numbers[0] > numbers[1]:
        winMishka += 1
    elif numbers[0] < numbers[1]:
        winChris += 1

if winMishka > winChris:
    print("Mishka")
elif winMishka < winChris:
    print("Chris")
else:
    print("Friendship is magic!^^")