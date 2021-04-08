import random

front = """
front        *  *              
          * #    # *        
         *  ######  *      
         *  #    #  *      
          *        *        
             *  * 
"""
rear = """
rear         *  *              
          *   ##   *        
         *    ##    *      
         *    ##    *      
          *   ##   *        
             *  * 
"""

confirm = 'y'
while confirm == 'y':
    coin = random.randint(1, 2)
    print(front, rear)
    choice = int(input("What's your choice? front : 1, rear : 2\n"))
    if choice < 1 or choice > 2:
        print("you can choice only 1 or 2.")
        continue
    print("Your choice: ")
    if choice == 1: print(front)
    else:   print(rear)
    print("computer: ")
    if coin == 1: print(front)
    else:   print(rear)
    if choice == coin:  print("Great!!\n")
    else:   print("Sorry...\n")
    confirm = input("Do you want to try again? y/n >>>>>> ").lower()
print("Good bye!")









