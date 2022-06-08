print("***********Welcome to Mason Vending Machine***********")
print("1. Cereal and granola bars - $1.99")
print("2. Chips and pretzels - $1.00")
print("3. Crackers and cookies - $1.50")
print("4. Fruits - $1.00")
print("5. Seeds and Nuts - $2.99")
print("6. Soda and water - $1.00")
print("7. Checkout")
print("8. Quit")



dict1 = {1:"Cereal and granola bars",
         2:"Chips and pretzels",
         3:"Crackers and cookies",
         4:"Fruits",
         5:"seeds and Nuts",
         6:"Soda and water",         
            }

dict111 ={
         1:1.99,
         2:1.00,
         3:1.50,
         4:1.00,
         5:2.99,
         6:1.00,
          }





lst = list(dict1.keys())
lst11 = list(dict111.keys())
orderlist = []
totalbill = 0


while True:
    print("Select your option (1-8):")
    choice_1 =("1. Cereal and granola bars - $1.99")
    choice_2 =("2. Chips and pretzels - $1.00")
    choice_3 =("3. Crackers and cookies - $1.50")
    choice_4 =("4. Fruits - $1.00")
    choice_5 =("5. Seeds and Nuts - $2.99")
    choice_6 =("6. Soda and water - $1.00")
    choice_7 =("7. Checkout")
    choice_8 =("8. Quit")
    order = input()
    order =int(order)
    if order in lst and lst11 :
        orderlist.append((dict1[order]))
        totalbill = totalbill+(dict111[order])
        print(dict1[order])
    elif order == 7:
        print("checking cart ")
        print("your cart:")
        for i in orderlist:       
            print(i)

        print("Your total before tax:", totalbill)
        total_tax = (totalbill*4.3)/100
        print("Total tax (4.3%):", total_tax)
        print("Your total after tax:",totalbill + total_tax )
        print("*********** Thanks ***********")


            
    elif order == 8:
        print("Exiting the program…")
        break
    else:
        print("Invalid option. Returning to main menu.")

    
        

           



















