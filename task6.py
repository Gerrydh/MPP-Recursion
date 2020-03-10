# define the function to reurn the index in an array of a character
def find_ind(L, v):
    if not L: 
            return [-1] # if the character is not present, return -1

    result = [] # add the result into a new array
    if L[-1] == v:
            result = [len(L)-1] # check the lenght of the array to see if L(the string to check) matches v (the character to be checked)
        
    return find_ind(L[:-1], v) + result # return the result after checking the full lenght of the array

print(find_ind("Galway Mayo Institute of Technology", "y"))
print(find_ind("Galway Mayo Institute of Technology", "x"))
