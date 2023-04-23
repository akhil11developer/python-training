##project : KALYAN JEWELLERS

print("kalyan jewellers")

name = input("Enter your name:")
gender = input("Ente your Gender:")
age = int(input("Enter your Age:"))

product = input("Enter produt name:")
product_gram = int(input("Enter Product Gram:"))


"""print("enter name",name)
print("enter name",gender)
print("enter name",age)"""



goldprice = 5752
goldprice1 = goldprice*product_gram
print("Total Gold Rate:",goldprice1)

making_charges = 845 #1
total_making_charges = product_gram *making_charges
print("Total making charges:",total_making_charges)

totalamount = goldprice1 + total_making_charges
print("total amount:",totalamount)




if gender == "male" and age >65:
    if totalamount >200000 and totalamount <300000:
        disc1 = (totalamount*20)/100
        print("discount : 20%")
        print("discount amount 1 : ",disc1)
        totalnet = (totalamount-disc1)
        print("totalnet amount",totalnet)
        
    
    elif totalamount >300000 and totalamount <500000:
        disc2 = (totalamount*30)/100
        print("discount : 30%")
        print("discount amount 2 : ",disc2)
        totalnet = (totalamount-disc2)
        print("totalnet amount",totalnet)
        
        
    elif totalamount >300000 and totalamount <500000:
        disc3 = (totalamount*35)/100
        print("discount : 35%")
        print("discount amount 3 : ",disc3)
        totalnet = (totalamount-disc3)
        print("totalnet amount",totalnet)
        
        
elif  gender == "male" and age <65:
    if totalamount > 200000 and totalamount < 300000:
        discount_amount1 = (totalamount*10)/100
        print("discount : 10%")
        print("discount_amount 1 : ",discount_amount1)
        totalnet = (totalamount-discount_amount1)
        print("totalnet amount",totalnet)
        
            
    elif totalamount > 300000 and totalamount < 500000:
        discount_amount2 = (totalamount*20)/100
        print("discount : 20%")
        print("discount_amount 2 : ",discount_amount2)
        totalnet = (totalamount-discount_amount2)
        print("totalnet amount",totalnet) 
        
           
    elif totalamount > 500000 :
        discount_amount3 = (totalamount*25)/100
        print("discount : 25%")
        print("discount_amount 3 : ",discount_amount3)
        totalnet = (totalamount-discount_amount3)
        print("totalnet amount",totalnet)
        
        
else:
    if gender =="female" and age >65:
        if totalamount >200000 and totalamount <300000:
            disc1 = (totalamount*25)/100
            print("discount : 25%")
            print("discount_amount 1:",disc1)
            totalnet = (totalamount-disc1)
            print("totalnet amount",totalnet)
            
            
        elif totalamount >300000 and totalamount <500000:
            disc2 = (totalamount*35)/100
            print("discount : 35%")
            print("discount amount 2 : ",disc2)
            totalnet = (totalamount-disc2)
            print("totalnet amount",totalnet)
            
        
        elif totalamount <500000:
            disc3 = (totalamount*40)/100
            print("discount : 40%")
            print("discount amount 3 : ",disc3)
            totalnet = (totalamount-disc3)
            print("totalnet amount",totalnet)
            
            
    elif gender =="female" and age <65:
        if totalamount >200000 and totalamount <300000:
            disc1 = (totalamount*15)/100
            print("discount : 15%")
            print("discount_amount 1:",disc1)
            totalnet = (totalamount-disc1)
            print("totalnet amount",totalnet)
            
        elif totalamount >300000 and totalamount <500000:
            disc2 = (totalamount*25)/100
            print("discount : 25%")
            print("discount amount 2 : ",disc2)
            totalnet = (totalamount-disc2)
            print("totalnet amount",totalnet)
        
        elif totalamount <500000:
            disc3 = (totalamount*30)/100
            print("discount : 30%")
            print("discount amount 3 : ",disc3)
            totalnet = (totalamount-disc3)
            print("totalnet amount",totalnet)
    
      
        
    