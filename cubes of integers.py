"""WAP to create a list of the cubes of only the even integers appearing in the input list
(may have elements of other types also) using the following:
a. 'for' loop
b. list comprehension"""
# a)
test = []
n = int(input('enter the length of list \n'))
for j in range(0, n):
    vals = input('enter the values: ')
    test.append(vals)
cubes = []
for i in test:
    if str(i).isdigit():
        if int(i) % 2 == 0:
            i = int(int(i) ** 3)
            cubes.append(i)
print('The cubed values of all the even digits in the given string using for loop are: ')
print(cubes)
# b)
list_comp = [int(cube)**3 for cube in test if cube.isdigit() and int(cube) % 2 == 0]
print('The cubed values of all the even digits in the given string using list comprehension are: ')
print(list_comp)
