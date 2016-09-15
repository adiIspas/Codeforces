import math

a, b = list(map(int, input().split()))
numberTaxi = int(input())

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

time = 9223372036854775807

for _ in range(0, numberTaxi):
    x, y, speed = list(map(int, input().split()))
    dist = distance(a, b, x, y)
    currentTime = dist/speed

    time = min(time, currentTime)

print(time)
