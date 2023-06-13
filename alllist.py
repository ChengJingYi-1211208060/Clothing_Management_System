import os
i={"Sport","Casual","Formal","Fashion"}

def list2():
    choose =0
    for choose in i:
        print("[0] Back\t     Catalogue: {}\n------------------------------------------------------------".format(choose))
        print("No  Item Name\t\t\t\t     Price\n")
        #Open file to display catalogue list
        with open("catalogue/{}.txt".format(choose), "r+") as f:
            lines = f.readlines()
            no = 1
            #Print all lines in the file
            for line in lines:
                #Print autonumbering + item details
                print(f"{no:<4}{line}", end="")
                no += 1  
list2()