position = str(input())

column = position[0]
row = position[1]

if (column is 'a' or column is 'h') and (row is '1' or row is '8'):
    print(3)
elif (column is 'a' or column is 'h') or (row is '1' or row is '8'):
    print(5)
else:
    print(8)

