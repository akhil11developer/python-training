"""
looping example:
there are 2 tyoe of loops

1) for loop -sequence control loop
2) while loop - entry control loop

        ->condition check at entry level
        if condtion goes true loop will execute

"""
for i in range(1,6):   #by default loop start from 1 to 5
    print(i)
    
for i in range(5):   #by default loop start from 0 to 4
    print(i)

for i in range(1,6):   #ACCEPT 5 number from user
    num = int(input("ENTER NUMBER:"))
    
