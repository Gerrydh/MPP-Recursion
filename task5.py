
# define function to create new string with replaced character
def replace(string, old, new):
    if string == '': # if string has no charcaters left, return the new string
        return ''
    if string[0] == old: # add new character to new string
        return new + replace(string[1:], old, new)
    return string[0] + replace(string[1:], old, new) # add  new character and replace the old for new characters

print(replace('multi paradigm programming', 'i', '1')) # replace all of the i's with 1