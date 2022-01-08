from math import floor
def percentil(numbers,percent):
    orderednumbers =sorted(numbers)
    n = len(numbers)
    p = percent
    
    if not (n*p).is_integer():
        return orderednumbers[floor(n*p)]
    else: 
        return int((orderednumbers[int(n*p)-1] + orderednumbers[int(n*p)])/2)
         
