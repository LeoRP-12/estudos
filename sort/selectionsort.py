def sortNumbers(toSort):
    for number in range(1,len(toSort)):
        min = number
        for i in range(number+1,len(toSort)):
            if toSort[min] > toSort[i]:
                min = i
        toSort[number],toSort[min] = toSort[min], toSort[number]
