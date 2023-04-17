CSK = int(input("CSK score:"))
DC = int(input("DC score:")) 
GT = int(input("GT score:"))


if DC >GT:
    if DC > CSK:
        print("DC WON THE MATCH")
    else:
        print("CSK WON THE MATCH")
else:
    if GT>CSK:
        print("DC WON THE MATCH")
    else:
        print("CSK WON THE MATCH")