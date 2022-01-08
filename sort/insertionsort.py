def sortNumbers(toSort):
    for number in range(1,len(toSort)):
        current_number= toSort[number]
        i=number -1

        while i>= 0 and current_number < toSort[i]:
            toSort[i+1] = toSort[i]
            i-= 1
        toSort[i+1] = current_number

def ReversesortNumbers(toSort):
    for number in range(1,len(toSort)):
        current_number= toSort[number]
        i=number -1

        while i>= 0 and current_number > toSort[i]:
            toSort[i+1] = toSort[i]
            i-= 1
        toSort[i+1] = current_number
