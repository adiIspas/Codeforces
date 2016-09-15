time_interval = list(map(int, input().split()))

l1 = time_interval[0]
r1 = time_interval[1]

l2 = time_interval[2]
r2 = time_interval[3]

k = time_interval[4]

time = 0

l = max(l1, l2)
r = min(r1, r2)

if l > r:
    time = 0
elif k >= l and k <= r:
    time = r - l
else:
    time = r - l + 1

print(time)
