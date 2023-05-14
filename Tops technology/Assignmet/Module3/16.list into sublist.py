"""
Write a Python program to check whether a list contains a sub list 
"""

list1 = [1,5,6,10,8,11,13]
list2 = [5,7,10]


i =0
for i in list1:  #loop start in list1 0 to n element
    for j in list2: #loop start in list2 o to n element
        if i == j :  #check the element will be same or not 
            print(i) #same value store in i and print same number