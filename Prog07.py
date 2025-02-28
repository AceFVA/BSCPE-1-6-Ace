# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

u_10nums = input("Enter 10 numbers separated in spaces: ")

u_num = u_10nums.split()
num_total = 0

for i in range(0,10):
    num_total = num_total + int(u_num[i])

print(num_total)
