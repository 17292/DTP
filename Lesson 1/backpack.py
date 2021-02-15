def mainMenu():
    while True:
    #displays the main menu
        
        print("""***BACKPACK LIST***

        Select a number for the action that you would like to do:

        1. View Backpack list
        2. Add item to Backpack list
        3. Remove ite from Backpack list
        4. Check if item is on Backpack list 
        5. How many items on Backpack list
        6. Clear backpack list
        """)

        #ask the user to make selection
        selection = input("Make your selection: ")

        #determine which action to perform based on user's preference
        if selection == "1":
            displaylist()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        else:
            print("You did not make a valid selection.")

#add a few items to the backpack list
backpack_list = ["lunchbox", "pencils", "books", "computer"]

#display the items on the backpack list
def displaylist():
    print("---BACKPACK LIST---")
    for i in backpack_list:
        print("*" + i)

#add an item to the backpack list
def addItem():
    item = input("Enter item you wish to add to the backpack list: ")
    backpack_list.append(item)
    print( item + " has been added to the backpack list. ")

#remove an item from backpack list
def removeItem():
    item = input("Which item would you like to remove from the backpack list: ")
    backpack_list.remove(item)
    print( item + " has been removed from the backpack list. ")

#check items on the backpack list
def checkItem():
    item = input("What item would you like to check on the backapck list: ")
    if item in backpack_list: 
        print("Yes," + item + " is on the shopping list. ")
    else:
        print("No," + item + " is not on the shopping list. ")

#counts the list
def listLength():
    print("There are", len(backpack_list), "items on the backpack list." )

#clears list
def clearList():
    backpack_list.clear()
    print("The backpack list is now empty. ")


mainMenu()






