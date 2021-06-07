def even(num):
    if num % 2 == 0:
        # print('True')
        return True
    if num % 2 == 1:
        # print('False')
        return False


num = int(input('Give me a number: '))
print(even(num))