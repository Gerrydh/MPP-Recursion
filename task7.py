  
# define function to sum of digits of a number 
def sum_number(number): 
    if number == 0: #if the number equals 0, then return 0
        return 0
    return (number %10 + sum_number(int(number /10))) #split the string by the left and the right digits
  

print(sum_number(42)) 
