#make a list of all numbers inputed 
#find the smallest number in the list

list = []

while True:
    num = int(input('Enter Num: '))
    list.append(num)
    list.sort()
    print(list)
    print("Smallest: ", list[:1])



