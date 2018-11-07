
def check(find_me, digit):
    if str(find_me) in str(digit):
        return True


def user_input():
    try:
        start = int(input('Enter start point number: '))
        end = int(input('Enter end point number: '))
        find_me = int(input('Enter what to find: '))
        if end <= start:
            print('Please enter correct sequence.\n')
            return user_input()
        if len(str(find_me)) > 1:
            print('Please enter one digit to find.\n')
            return user_input()

        return start, end, find_me
    except ValueError:
        print('Please enter integer. \n')
        return user_input()


def main(start, end, find_me):
    found = 0
    while start <= end:
        for digit in str(start):
            if check(find_me, digit) is True:
                found += 1
        start += 1
    print('{} appeared {} times in the series'.format(find_me, found))


if __name__ == '__main__':
    start, end, find_me = user_input()
    main(start, end, find_me)
