import os
import time

def main_menu():
    os.system('cls')
    print("============================================================")
    print("\t\tClothing Management System")
    print("============================================================")
    print("\t\t\t  Main Menu\n------------------------------------------------------------")
    print("1. Register an account\n2. Browse and purchase\n3. Admin mode\n4. Exit")
    print("------------------------------------------------------------")
    #Prompt for input
    main_menu_choice=int(input("Select your choice: "))
    if main_menu_choice==1:
        while True:
            os.system('cls')
            print("\t\t\tRegistration\n------------------------------------------------------------")
            type="customer"
            name=input("Name(no spaces): ")
            username=input("Username: ")
            password=input("Password: ")
            #Call compare function to compare customer registry data
            success=int(compare(type, name, username, password))
            #Detect duplicate account
            if success==1:
                print("\033[0;33;40m\nThis account already exists. Please try again.\033[0m")
                time.sleep(1)
            else:
                #Print new account details into registry
                with open("txt/registry/customer.txt", "a") as fregistry:
                    print(name, username, password, file=fregistry)
                print("\033[0;32;40m\nRegistration successful! Returning to main menu...\033[0m")
                time.sleep(1)
                main_menu()
    elif main_menu_choice==2:
        while True:
            for i in range(3):
                os.system('cls')
                print("\t\t\t   Login\n------------------------------------------------------------")
                name = input("Name (no spaces): ")
                username = input("Username: ")
                password = input("Password: ")
             # Call compare function to compare customer registry data
                success = compare(type="customer", name=name, username=username, password=password)
        # Detect if there are matching accounts
                if success == 1:
                    print("\033[0;32;40m\nLogin success! Redirecting to main page...\033[0m")
                    time.sleep(1)
                    main(username)
                    return
                else:
                    print(f"\033[0;31;40m\nLogin failed! You have {2-i} attempts left. Please try again.\033[0m ")
                    time.sleep(1)

    # if user failed to login after 3 attempts
            print("\033[0;31;40m\nLogin failed! Returning to main menu.\033[0m ")
            time.sleep(1)
            main_menu()
                        
                        
    elif main_menu_choice==3:
        while True:
            for i in range(3):
                os.system('cls')
                print("\t\t\tAdmin Login\n------------------------------------------------------------")   
                name=input("Name(no spaces): ")
                username=input("Username: ")
                password=input("Password: ")
                #Call compare function to compare admin registry data
                success=compare(type="admin", name=name, username=username, password=password)
                #Detect if there are matching accounts
                if success == 1:
                    print("\033[0;32;40m\nLogin success! Redirecting to admin menu...\033[0m")
                    time.sleep(1)
                    admin_menu()
                else:
                    print(f"\033[0;31;40m\nLogin failed! You have {2-i} attempts left. Please try again.\033[0m ")
                    time.sleep(1)
            # if user failed to login after 3 attempts    
            print("\033[0;31;40m\nLogin failed! Returning to main menu.\033[0m ")
            time.sleep(1)
            main_menu()
              
    elif main_menu_choice==4:
        os._exit(0)
    else:
        print("\033[0;31;40m\nInvalid choice. Try again.\033[0m")
        time.sleep(1)
        main_menu()

def main(username):
    def search_item():
        while True:
            os.system('cls')
            print("[0] Back\t\t   Search Item \n----------------------------------------------------------------")
            keyword = input("What are you looking for : ")

            if keyword == '0':
                main(username)
                break

            files = {
                "casual": "txt/catalogue/casual.txt",
                "sport": "txt/catalogue/sport.txt",
                "formal":"txt/catalogue/formal.txt",
                "fashion":"txt/catalogue/fashion.txt"
            }

            found = False  

            for filename, filepath in files.items():
                with open(filepath, "r") as file:
                    contents = file.read()
                    if keyword in contents:
                        found = True
                        print("")
                        print(f"Keyword '{keyword}' found in category {filename} ")
                        print(contents)

                if not found:
                
                    print(f"In category {filename} no found the keyword '{keyword}'.")

            input("Press enter to continue...")
            
    def buy():
        os.system('cls')
        print("[0] Back\t\t Catelogue \n------------------------------------------------------------\nBrowse a category:")
        print("\n1.Sport")
        print("2.Casual")
        print("3.Formal")
        print("4.Fashion")
        print("------------------------------------------------------------")
        #Prompt input
        choose = input("Select your choice: ")
        if (choose=="1"):
            choice=("Sport")
        elif (choose=="2"):
            choice=("Casual")
        elif (choose=="3"):
            choice=("Formal")
        elif (choose=="4"):
            choice=("Fashion")
        elif (choose=="0"):
            main(username)
        else:
            print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
            time.sleep(1)
            buy()
        
        while True:
            os.system('cls')
            print("[0] Back\t     Catalogue: {}\n------------------------------------------------------------".format(choice))
            print("No  Item Name\t\t\t\t     Price\n")
            #Open file to display catalogue list
            with open("txt/catalogue/{}.txt".format(choice), "r+") as f:
                lines = f.readlines()
                no = 1
                #Print all lines in the file
                for line in lines:
                    #Print autonumbering + item details
                    print(f"{no:<4}{line}", end="")
                    no += 1
                #Select the line of the item chosen
                line_number=int(input("\n------------------------------------------------------------\nSelect your choice: "))
                if line_number == 0:
                    buy()
                elif line_number <= len(lines):
                    # Print the selected line
                    item = lines[line_number - 1]
                    print(f"\nItem: {item[:40]}")
                colour=input("Colour: ")
                size=input("Size [XS-XL/-]: ")
                quantity=int(input("Quantity: "))
                #Extract the price from the line
                line = lines[line_number - 1]
                original_price=float(line[-6:])
                price=quantity*original_price
                print("\nTotal is RM {:.2f}".format(price))
                add=input("------------------------------------------------------------\nAdd to cart? [Y/N]: ")
                if add=='Y' or add =='y':
                    f=open("txt/customers/{}.txt".format(username),"a")
                    f.write("{} RM  {:<10.2f}  {:<8}  {:<15} {:<20}\n".format(item[:30], price, size, colour, quantity))
                    
                    f.close()
                    print("\033[0;33;40m\nAdding item(s) to cart...\033[0m")
                    time.sleep(1)
                elif add=='N' or add == 'n':
                    print("\033[0;37;40m\nCancelling...\033[0m")
                    time.sleep(1)
                else:
                    print("\033[0;31;40m\nInvalid input. Please try again...\033[0m")
                    time.sleep(1)
    def cart():
        os.system('cls')
        print("[0] Back \t\t\t    Your Cart \t\t\t     [1] Edit cart\n-----------------------------------------------------------------------------------")
        print("No  Item Name\t\t\t   Price\t   Size\t     Colour\t  Quantity\n")
        #Open file to display catalogue list
        with open("txt/customers/{}.txt".format(username), "r+") as f:
        # Read all lines from the file and store them in a list
            lines = f.readlines()
            no = 1
            # Print all lines in the file
            for line in lines:
                #Print autonumbering + item details
                print(f"{no:<4}{line}", end="")
                no += 1
            choose = int(input("-----------------------------------------------------------------------------------\nSelect your choice: "))
            #Prompt for which line to delete
            if choose==0:
                os.system('cls')
                main(username)
            elif choose==1:
                #Prompt for which line to delete
                f.seek(0)
                lines = f.readlines()
                f.seek(0)
                line_number = int(input("\nWhich line do you want to delete? : "))
                #Read if line is available
                if line_number <= 0:    
                    print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
                    time.sleep(1)
                    cart()
                elif line_number <= len(lines):
                    del lines[line_number-1]
                    f.writelines(lines)
                    f.truncate()
                    f.close()
                    print("\033[0;32;40m\nDeleting item from cart...\033[0m")
                else:    
                    print("\033[0;31;40m\nInvalid input! Please try again.\033[0m ")
                    time.sleep(1)
                    cart()
            else:
                print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
        time.sleep(1)
        cart()

    
    os.system('cls')
    print("[0] Back\t    Customer Main Page \n------------------------------------------------------------")
    print("Welcome {}! What would you like to do?".format(username))
    print("\n1.Browse catalogue")
    print("2.Check cart")
    print("3.Search")
    print("------------------------------------------------------------")
    #Prompt input
    choose = input("Select your choice: ")
    if (choose=="1"):
        buy()
    elif (choose=="2"):
        cart()
    elif (choose=="3"):
        search_item()
    elif (choose=="0"):
        main_menu()
    else:
        print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
        time.sleep(1)
        main(username)

def admin_menu():
    def add_clothes():
        os.system('cls')
        print("[0] Back\t  Catalogue: Admin mode (Add) \n------------------------------------------------------------\nAdd an item:\n")
        print("1.Sport")
        print("2.Casual")
        print("3.Formal")
        print("4.Fashion")
        print("------------------------------------------------------------")
        choose = input("Select your choice: ")
        #Prompt input
        if (choose=="1"):
            choice=("Sport")
        elif (choose=="2"):
            choice=("Casual")
        elif (choose=="3"):
            choice=("Formal")
        elif (choose=="4"):
            choice=("Fashion")
        elif (choose=="0"):
            admin_menu()
        else:
            print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
            time.sleep(1)
            add_clothes()
        #Loop until '0' is typed
        while True:
            os.system('cls')
            print("[0] Back\t  Catalogue: Admin mode (Add) \n------------------------------------------------------------")
            print("No  Item Name\t\t\t\t     Price\n")
            #Open file to display catalogue list
            with open("txt/catalogue/{}.txt".format(choice), "r+") as f:
            # Read all lines from the file and store them in a list
                lines = f.readlines()
                no = 1
                # Print all lines in the file
                for line in lines:
                    #Print autonumbering + item details
                    print(f"{no:<4}{line}", end="")
                    no += 1
            #Prompt input for name and price of new item
            clth=input("------------------------------------------------------------\nEnter clothing details.\n\nName : ")
            if clth == "0":
                add_clothes()
            f=open("txt/catalogue/{}.txt".format(choice),"a")
            prc=float(input("Price : RM "))
            f.writelines("{:<{width}}" " RM  {:.2f}\n".format( clth, prc, width=40))
            f.close()
            print("\033[0;33;40m\nAdding item...\033[0m")
            time.sleep(1)

    def remove_clothes():
        os.system('cls')
        print("[0] Back\tCatalogue: Admin mode (Remove) \n------------------------------------------------------------\nRemove an item:\n")
        print("1.Sport")
        print("2.Casual")
        print("3.Formal")
        print("4.Fashion")
        print("------------------------------------------------------------")
        #Prompt input
        choose = input("Select your choice: ")
        if (choose=="1"):
            choice=("Sport")
        elif (choose=="2"):
            choice=("Casual")
        elif (choose=="3"):
            choice=("Formal")
        elif (choose=="4"):
            choice=("Fashion")
        elif (choose=="0"):
            admin_menu()
        else:
            print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
            time.sleep(1)
            remove_clothes()
        #Loop until '0' is typed
        while True:
            os.system('cls')
            print("[0] Back\tCatalogue: Admin mode (Remove) \n------------------------------------------------------------")
            print("No  Item Name\t\t\t\t     Price\n")
            #Open file to display catalogue list
            with open("txt/catalogue/{}.txt".format(choice),"r+") as f:
                no=1
                for line in f:
                    #Print autonumbering + item details
                    print(f"{no:<4}{line}", end="")
                    no += 1
                #Prompt for which line to delete
                f.seek(0)
                lines = f.readlines()
                f.seek(0)
                line_number = int(input("------------------------------------------------------------\nWhich line do you want to delete? : "))
                if line_number==0:
                    os.system('cls')
                    remove_clothes()
                elif line_number <= len(lines):
                    del lines[line_number-1]
                f.writelines(lines)
                f.truncate()
                f.close()
            print("\033[0;33;40m\nDeleting item...\033[0m")
            time.sleep(1)

    def edit_clothes():
        os.system('cls')
        print("[0] Back\t  Catalogue: Admin mode (Edit) \n------------------------------------------------------------\nEdit details of an item:\n")
        print("1.Sport")
        print("2.Casual")
        print("3.Formal")
        print("4.Fashion")
        print("------------------------------------------------------------")
        choice = input("Select your choice: ")
        #Prompt input
        if (choice=="1"):
            category=("Sport")
        elif (choice=="2"):
            category=("Casual")
        elif (choice=="3"):
            category=("Formal")
        elif (choice=="4"):
            category=("Fashion")
        elif (choice=="0"):
            admin_menu()
        else:
            print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
            time.sleep(1)
            edit_clothes()
    
        #Loop until '0' is typed
        while True:
            os.system('cls')
            print("[0] Back\t  Catalogue: Admin mode (Edit) \n------------------------------------------------------------")
            print("No  Item Name\t\t\t\t     Price\n")
            #Open file to display catalogue list
            with open("txt/catalogue/{}.txt".format(category), "r+") as f:
                # Read all lines from the file and store them in a list
                lines = f.readlines()
                no = 1
                # Print all lines in the file
                for line in lines:
                    #Print autonumbering + item details
                    print(f"{no:<4}{line}", end="")
                    no += 1
                #Prompt input for line number to edit
                line_number = int(input("\n------------------------------------------------------------\nSelect line number to edit: "))
                if line_number == 0:
                    edit_clothes()
                elif line_number > len(lines):
                    print("\033[0;31;40m\nInvalid line number. Please try again...\033[0m")
                    time.sleep(1)
                else:
                    #Prompt input for name and price of the edited item
                    clth=input("Enter new name: ")
                    prc=float(input("Enter new price: RM "))
                    #Update the selected line with the new name and price
                    lines[line_number-1] = "{:<{width}}" " RM  {:.2f}\n".format(clth, prc, width=40)
                    #Rewrite the whole file with the updated lines
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                    print("\033[0;32;40m\nEditing item...\033[0m")
                    time.sleep(1)
           
    os.system('cls')
    print("[0] Back\t    Catalogue: Admin mode \n------------------------------------------------------------\n")
    print("1. Add clothes\n2. Remove clothes\n3. Edit clothes\n------------------------------------------------------------")
    choice=input("Select your choice: ")
    #Prompt for input
    if(choice=="1"):
        add_clothes()
    elif(choice=="2"):
        remove_clothes()
    elif(choice=="3"):
        edit_clothes()
    elif(choice=="0"):
        main_menu()
    else:
        print("\033[0;31;40m\nInvalid input! Please try again. \033[0m")
        time.sleep(1)
        admin_menu()

def compare(type, name, username, password):
    #Read contents of registry
    with open("txt/registry/{}.txt".format(type), "r") as fcompare:
        data_registry = fcompare.readline()
        data_login = "{} {} {}\n".format(name, username, password)
        while data_registry:
            if data_registry == data_login:
                return 1
            data_registry = fcompare.readline()
        if data_registry != data_login:
            return 0


main_menu()