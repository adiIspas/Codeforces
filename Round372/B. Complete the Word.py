def fill():
    temp = []

    for _ in range(0, 26):
        temp.append(0)

    return temp


def sub_string(string, start, length):
    temp = []

    if len(string) - start < length:
        return -1

    for i in range(0, length):
        temp.append(string[i + start])

    return temp


def check_string(base_string, position, string):
    valid = True
    alphabet = fill()

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for c in string:
        value = ord(c) - 65

        if alphabet[value] is 0 and c is not '?':
            alphabet[value] += 1
        elif alphabet[value] is not 0 and c is not '?':
            valid = False
            break

    if valid is True:
        temp = string
        last = 0

        for i in range(0, len(temp)):
            if temp[i] is '?':
                for j in range(last, len(alphabet)):
                    if alphabet[j] is 0 and temp[i] is '?':
                        temp[i] = letters[j]
                        last = j
                        alphabet[j] += 1

        for i in range(0, position):
            if base_string[i] is '?':
                base_string[i] = 'A'

        j = 0
        for i in range(position, len(base_string)):
            if j < len(temp):
                base_string[i] = temp[j]
                j += 1
            else:
                base_string[i] = 'A'

        return base_string
    else:
        return valid


word = list(input())

show = False
for i in range(0,len(word)):
    current_string = sub_string(word, i, 26)

    if current_string is -1:
        break

    result = check_string(word, i, current_string)

    if result is not False:
        result = ''.join(map(str, result))
        print(result)
        show = True
        break

if show is False:
    print('-1')
