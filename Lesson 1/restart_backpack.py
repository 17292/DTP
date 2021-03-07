'''BACKPACK LIST'''

'''FUNCTIONS'''
def show_backpack():
    '''nicely print the backpack information'''
    print(f"{'Index':<8}{'Name':<20}{'Description':<20}")
    i = 0
    for item in backpack:
        print(f"{i:<8}{item[0]:<20}{item[1]:<60}")
        i += 1

def get_item():
    '''get an item and description from the user and add to backpack'''
    item = input("Name? ")
    description = input("Description? ")
    backpack.append((item, description))

def add_item(item_name, item_description):
    '''add an item and description to the backpack'''
    backpack.append((item_name, item_description))

def delete_item(item_index):
    '''delete an item from backpack by index'''
    try:
        del backpack[int(item_index)]
    except:
        print("That item does not exist")

#THIS IS THE MAIN BACKPACK LIST
backpack = list()

#MAIN LOOP
while True:
    #get user option
    user_input = input("\nWhat do you want to do?\n1. Print backpack contents\n2. Add item\n3. Delete an item\n4. Exist\n")
    #deal with printing
    if user_input == "1":
        show_backpack()
    #now the adding    
    elif user_input == "2":
        get_item()
    #now the deleting
    elif user_input == "3":
        item = input("\nWhat item index do you want to delete\n")
        delete_item(item)
    #and exist
    elif user_input == "4":
        print("\n\nGoodbye!\n\n")
        break
