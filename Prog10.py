# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

for i in range (0,101):
    if i % 10 != 0:
        print(i)

'''
Alternative:
for i in range (0,101):
    if not str(i).endswith("0"):
        print(i)
'''
