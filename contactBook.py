# #2. Build a Contact Book to store, view, update, and delete contact names and numbers.


contact_list = []
def add_contacts():
    cname = str(input("Enter the name: "))
    cnum = int(input("Enter the number: "))
    data = {
        "Name" : cname,
        "Number" : cnum
    }
    contact_list.append(data)
    # print(contact_list)
    return contact_list
def view_contact():
    print("Your Contacts!!!")
    if not contact_list:
        print("No contacts yet!")
    else:
        for i in range(len(contact_list)):
            print(f"{i+1}.{contact_list[i]}")
def update_contact():
    name = str(input("Enter the name you want to update: "))
    for contact in contact_list:
        if contact["Name"].lower() == name.lower():
            new_num  = input("Enter the new number: ")
            contact["Number"] = new_num
            print("Contact updated**")
            return
    print("Contact not found")
def delete_contact():
    view_contact()
    name = str(input("Enter the name you want to delete: "))
    for i,contact in contact_list:
        if contact["Name"].lower() == name.lower():
            del  contact_list[i]
            # contact_list.pop(name)
            print("Contact removed**")
            return

def contactBook():
    while True:
        print("\n1.Add contact")
        print("2.View contact")
        print("3.Update contact")
        print("4.Delete contact")
        print("5.Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("All Done")
            break
        else:
            "Invalid Choice"
contactBook()

