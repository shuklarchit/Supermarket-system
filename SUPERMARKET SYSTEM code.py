import sys
import time
import matplotlib.pyplot as plt 

print( "                                   !! WELCOME TO OUR SUPERMARKET !!")
print("ALL PRICES OF RESPECTIVE ITEMS ARE IN INR")
print() 
d1 = {'MILK' : 80,
      'BREAD' : 40 ,
      'CHIPS' : 20,
      'EGGS': 12,
      'SOFT DRINK' : 40,
      'ICE CREAM' : 50,
      'CUP NOODLES': 50,
      'WATER BOTTLE': 20,
      'COFFEE POWDER': 120,
      'TEA LEAVES': 90}
   
print("ACTIONS")
print (" 1 - SHOW ITEM LIST")
print (" 2 - ADD ITEMS") 
print(" 3 - CANCEL SHOPPING  ") 


        
while True:
      user = int(input("Enter the action's no. to be carried on : "))
      if user == 1:
         print("OPENING ITEMS LIST........")
         time.sleep(2)
         print() 
         for i in d1.items():
                print(i)
      elif user == 2:
            print("PLEASE CONTINUE")
            print() 
            break
      elif user == 3:
            print("AS YOU WISH, SEE YOU LATER !")
            sys.exit()

cart_list = []
price_list = []

while True:
     cart = input("Enter the product name (ENTER 'CHECKOUT' WHEN DONE WITH ADDING ITEMS) : ").upper()
     
     if cart in d1:
           quantity = int(input("Enter the quantity : "))
           sum_all = quantity * d1[cart]
           print() 
           print(quantity,"x",{cart},"ADDED TO CART") 
           OK = cart,quantity  
           cart_list.append(OK)
           price_list.append(sum_all)
           print()  
     elif cart == "CHECKOUT":
          print("CHECKING OUT.........")
          print()
          time.sleep(3) 
          break 
          
     else:
        print("INVALID INPUT, TRY AGAIN")
        print() 
        

print("YOUR FINAL CART IS", cart_list, end="x")
print() 
grand_total = sum(price_list)
print("YOUR GRAND TOTAL IS : ", grand_total) 

while True:
       payment_mode = input("Choose your payment method(Card,cash,upi) : ").upper()
       if payment_mode == "CASH":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       elif payment_mode == "UPI":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       elif payment_mode == "CARD":
            print("YOU'VE CHOSEN",{payment_mode}, "AS YOUR PAYMENT METHOD")
            break
       else:
            print("CHOOSE FROM THE AVAILABLE PAYMENT MODE !") 
 
print() 

while True:
    payment = int(input("ENTER THE GRAND TOTAL AMOUNT : "))
    if payment == grand_total:
         print("PROCESSING.......")
         time.sleep(2)
         print("VERIFYING",{payment_mode},"DETAILS.........")
         time.sleep(3) 
         print("PAYMENT SUCCESSFUL, THANK YOU")
         break
   
    else:
         print("PROCESSING........")
         time.sleep(2)
         print("TRY AGAIN COZ YOU'VE ENTERED EITHER MORE OR LESS AMOUNT THAN THE GRAND TOTAL")  

print() 
print("VISIT AGAIN !") 

n = len(cart_list)

m = range(1,n+1) 

print()
print("PRINTING YOUR PURCHASED ITEMS GRAPH FOR CONVINIENCE....")
time.sleep(5)  

x = (m)
y = (price_list)
plt.plot(x,y, color = 'yellow', marker = 'o', linewidth = 12, markerfacecolor = 'blue')
plt.title("YOUR BILL'S GRAPH")
plt.xlabel("ITEM NO.s")
plt.ylabel("PRICES")
plt.show() 
