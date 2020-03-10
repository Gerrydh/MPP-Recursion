# define function to return the product of an array
 
def product(numbers):
   if len(numbers) == 1: # checking if the list is 1 element in length. Base case
        return numbers[0]
   else:
        return numbers[0] * product(numbers[1:]) #function calls itself and multplys each element in the list

print(product([5,8,38,42,2]))

