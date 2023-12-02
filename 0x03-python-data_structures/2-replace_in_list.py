#!/usr/bin/python3
my_list = [1, 2, 3]
new_list = replace_in_list(my_list, 0, 5)
print(new_list) # [5, 2, 3]  

no_change = replace_in_list(my_list, -1, 5) 
print(no_change) # [1, 2, 3] - no change
