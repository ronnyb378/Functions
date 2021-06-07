#figures out wether number is even or odd
def even(num):
    if num % 2 == 0:
        return True
    if num % 2 == 1:
        return False

#empty list for beginning of count 
even_num = []

#infinte loop to keep the count continuing
while True:
    #user input
    num = int(input('Give me a number: '))
    #recalls the def and assigns a variable to return
    nums = even(num)
    #if even, appended to even_num list
    if nums == True:
        even_num.append(num)
        print(even_num)
    #if odd, cycle continues
    if nums == False: 
        continue


