#make a list of strings
#calculate lenght of strings
#print the shortes strings 
words = []

while True:
    w = input('Word: ')
    words.append(w)
    words.sort(len(w))
    print("Shortest: ", words[0:])
