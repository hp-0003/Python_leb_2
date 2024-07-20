my_list = []

n = int(input("Enter number for list: "))

for i in range(0,n):
    num = int(input("Enter Value:"))
    my_list.append(num)
    
print("Original List:", my_list)

my_list.reverse()

print("Reversed List:", my_list)

