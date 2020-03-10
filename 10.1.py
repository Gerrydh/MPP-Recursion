def parens(no, s="", curb=0):
    # case 1: all open parens used
    if no == 0: 
        if curb == 0: 
            return [s]
        return parens(no, s+")", curb-1) 

    # case 2: none are currently open
    if curb == 0:
        return parens(no-1, s+"(", curb+1)

    # case 3: one or more are currently open
    return parens(no-1, s+"(", curb+1) + parens(no, s+")", curb-1)
print(parens(['()']))