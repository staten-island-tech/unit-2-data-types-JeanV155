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
          


def finalcost(i):
    for price in price:
         bill = bill + i

    
finalcost(i)

print(bill)


 

 
