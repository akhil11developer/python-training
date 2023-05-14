"""
Write a Python program to get unique values from a list 
"""

list1 = [1,5,8,20,35,67,2,5,1,20]

print("original list : ",list1)

my_unique = set(list1) #set method remove the same element in list

my_newlist = list(my_unique)  #convert a dict to list

print("print unique number in list : ",my_newlist)