dimensions = list(map(int, input().split()))

n = dimensions[0]
m = dimensions[1]

colored = False
for _ in range(0, n):
    colors = list(map(str, input().split()))

    if 'C' in colors:
        print("#Color")
        colored = True
        break

    if 'M' in colors:
        print("#Color")
        colored = True
        break

    if 'Y' in colors:
        print("#Color")
        colored = True
        break

if colored is False:
    print("#Black&White")