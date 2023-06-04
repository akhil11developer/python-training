"""Write a Python program to count the number of lines in a text file. 
"""

f = open("akhil.txt","r")

word = len(f.readlines())

print(word)