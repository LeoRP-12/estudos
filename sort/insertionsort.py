from typing import List

def sortNumbers(toSort: List, mode='n') -> List : 
    try:
        assert mode=='n' or mode=='r' 
        if mode=="n":
            for number in range(1,len(toSort)):
                current_number= toSort[number]
                i=number -1

                while i>= 0 and current_number < toSort[i]:
                    toSort[i+1] = toSort[i]
                    i-= 1
                toSort[i+1] = current_number

        if mode =='r':
            for number in range(1,len(toSort)):
                current_number= toSort[number]
                i=number -1
                while i>= 0 and current_number > toSort[i]:
                    toSort[i+1] = toSort[i]
                    i-= 1
                toSort[i+1] = current_number
    except AssertionError:
        print("allowed values for mode are 'r' (reverse mode) or 'n' (normal mode)")