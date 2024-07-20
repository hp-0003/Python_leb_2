my_list = [12, 35, 9, 56, 24]
print("Original List value: ",my_list)

def demo(lst):
    if (len(lst) > 0): 
        lst[0], lst[-1] = lst[-1], lst[0]  

demo(my_list)

print("After Interchange list value: ",my_list)

