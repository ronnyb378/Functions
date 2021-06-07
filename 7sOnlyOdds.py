#figures out wether number is even or odd
def even(num):
    if num % 2 == 0:
        return True
    if num % 2 == 1:
        return False

#empty list for beginning of count 
odd_num = []

#infinte loop to keep the count continuing
while True:
    #user input
    num = int(input('Give me a number: '))
    #recalls the def and assigns a variable to return
    nums = even(num)
    #if even, cycle continues 
    if nums == True:
        continue
    #if odd, appended to odd list
    if nums == False: 
        odd_num.append(num)
        print(odd_num)

