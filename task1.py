
# define the function to sum the array
def SumArray(n): 
    if len(n)==0: #if the array is empty return 0
        return 0
    else:
        return n[0] + SumArray(n[1:]) #This is the recursion step calling the funtion
print(SumArray([1, 3, 4, 2, 5])) # print the sum of our array
