#define the function to remove odd numbers from list
def rem_odd(list):
    if not list: # if thre are none in the list return an empty array list
        return []
    return ([list[0]] 
    if list[0] % 2 == 0 # if there are even numbers
    else []) + rem_odd(list[1:]) # add them to a new list


print(rem_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

