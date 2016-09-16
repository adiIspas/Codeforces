number = int(input())

one = 'I hate'
two = 'I love'
result = ''

first = True
second = False

for i in range(1, number + 1):
    if first is True and i is 1:
        result += one
        first = False
        second = True
    elif first is True and i is not 1:
        result += ' that '
        result += one
        first = False
        second = True
    elif second is True:
        result += ' that '
        result += two
        second = False
        first = True

result += ' it'
print(result)
