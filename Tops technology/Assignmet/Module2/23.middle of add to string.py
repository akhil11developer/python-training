"""Write a Python function to insert a string in the middle of a string.
"""


str = "python is language"
s = str.split() 
strlist = list(s)
strlist.insert(2,"hello")


print(strlist)