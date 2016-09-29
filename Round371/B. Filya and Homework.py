n = int(input())
numbers = list(map(int, input().split()))

def all_equals(numbers):
    start = numbers[0]

    for number in numbers:
        if number != start:
            return 0
        start = number

    return 1

def check_numbers(numbers):
    number_one = -1
    number_two = -1
    number_three = -1
    number_four = -1

    for number in numbers:
        if number_one is -1:
            number_one = number
        elif number_two is -1 and number is not number_one:
            number_two = number
        elif number_three is -1 and (number is not number_one and number is not number_two):
            number_three = number
        elif number_four is -1 and (number is not number_one and number is not number_two and number is not number_three):
            number_four = number

    if number_three is -1:
        return 0
    if number_one is not -1 and number_two is not -1 and number_three is not -1 and number_four is not -1:
        return 1
    else:
        sort_numbers = []
        sort_numbers.append(number_one)
        sort_numbers.append(number_two)
        sort_numbers.append(number_three)

        if (2 * sort_numbers[1]) is (sort_numbers[0] + sort_numbers[2]):
            return 0
        else:
            return 1

if check_numbers(numbers) is 1 and n >= 3 and all_equals(numbers) is 0:
    print('NO')
else:
    print('YES')