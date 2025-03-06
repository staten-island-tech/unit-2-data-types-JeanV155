price = int(input("Enter price of item one by one: "))
finished = input("IF done, enter Done: ")
def cost(price):
    bill.append(price)
   

bill = []
cost(price)
while finished != "Done": 
        price = int(input("Enter price of item one by one: "))
        cost(price)
        finished = input("IF done, enter Done: ")
          


finalcost = sum(bill) 

if finalcost > 100:
    print(finalcost - 0.1*finalcost)
else:
     print(finalcost)

    



print(bill)


 

 
