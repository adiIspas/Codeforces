numberRows = int(input())

seats = []
find = False
for _ in range(0, numberRows):
    currentSeats = list(input())
    if find is False and currentSeats[0] is 'O' and currentSeats[1] is 'O':
        find = True
        currentSeats[0] = '+'
        currentSeats[1] = '+'
    elif find is False and currentSeats[3] is 'O' and currentSeats[4] is 'O':
        find = True
        currentSeats[3] = '+'
        currentSeats[4] = '+'
    seats.append(currentSeats)

if find is True:
    print('YES')
    for currentSeats in seats:
        print(*currentSeats, sep='')
else:
    print('NO')