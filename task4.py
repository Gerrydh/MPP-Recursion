#define the function to remove even numbers from list
def rem_even(list):
    if not list: # if there are none in the list return an empty array list
        return []
    return ([list[0]] 
    if list[0] % 2  # if there are odd numbers
    else []) + rem_even(list[1:]) # add them to a new list


print(rem_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))