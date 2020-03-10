#https://stackoverflow.com/questions/44543950/finding-minimum-value-in-a-list-recursively

def findMinimum(l):
    if len(l) == 0:
       raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
       minNumber = findMinimum(l[1:])
       min = l[0]
       if minNumber < min:
            min = minNumber
       return min

print(findMinimum([1,0,-2,10,100,6]))
#print(findMinimum([]))

def find_lowest(lst):
    """Return the lowest positive number in a list."""
    def lowest(first, rest):
        # Base case
        if len(rest) == 0:
            print(first) # This line is only to check the value
            return first
        if first > rest[0] or first < 0:
            lowest(rest[0], rest[1:])
        else:
            lowest(first, rest[1:])
    return lowest(lst[0], lst[1:])


print(find_lowest([1,2,4,6])) # Prints None, but should print the lowest number