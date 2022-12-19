""" 12.Write a function that prints a dictionary where the keys are numbers between 1 and 5
and the values are cubes of the keys"""
cubes = {}
for i in range(3,9):
    cubes[i] = i**4
for k in cubes.keys():
    print("{} : {}".format(k,cubes[k]))
