# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

num = input("Enter 10 numbers separated in spaces: ")

num_list = num.split()
total_odd = 0

for i in range(0,10):
    if int(num_list[i]) % 2 == 1:
        total_odd = total_odd + 1
        
print(total_odd)
