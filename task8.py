# define the function to print each element of a string on a new line
def newLine(s):
    if s:
       print(s[0]) # print each element of the string starting at 0
       newLine(s[1:]) # new  line will now have 1 less element for the function to recurse through
 
print(newLine('217382'))


