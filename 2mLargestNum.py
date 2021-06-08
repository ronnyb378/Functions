#make a list of all numbers inputed 
#find the largest number in the list
list = []

while True:
    num = int(input('Enter Num: '))
    list.append(num)
    list.sort()
    print("Largest: ", list[-1:])
