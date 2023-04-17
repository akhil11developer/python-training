"""
while loop:

syntax:
initialization

while condition:
    statement
    updation
"""

status =True
while status:
    num = int(input("Enter number:"))
    choice = int(input("DO YOU WANT TO CONTINUE PRESS 1 FOR YES AND PRESS 2 FOR NO:"))
    if choice ==1:
        status = True
    else:
        status = False