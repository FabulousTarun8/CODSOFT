contact_book = {}

def input_taker(prompt, error="", constraints=False, length=0, integer=False):
    while True:
        value = input(prompt)
        if constraints:
            if integer:
                try:
                    value = int(value)
                except:
                    print(error)
                    continue
            if length:
                if len(str(value)) != length:
                    print(error)
                    continue
        print(value, end=", ")
        confirmation = input("Confirm? (yes/no): ").lower()
        if confirmation == "no":
            print("Please re-enter the data!")
            continue
        return value

def add_contact():
    print()
    name = input_taker("Enter name: ")
    number = input_taker("Enter number: ", "Invalid number, re-enter the number properly!", True, 10, True)
    email = input_taker("Enter e-mail: ")
    address = input_taker("Enter address: ")
    contact_book[name] = {
        "Number 📞": number,
        "Email 📧": email,
        "Address 🏠": address
    }
    print(f"{name} added successfully to your contacts! ✅")

def view_contact(name):
    print(f"{name}:-")
    for data in contact_book[name]:
        print(f"{data}: {contact_book[name][data]}")

def view_contacts():
    print()
    for name in contact_book:
        print()
        view_contact(name)

def search_contact():
    print()
    name = input_taker("Enter name: ")
    if name in contact_book:
        view_contact(name)
    else:
        print(f"{name} not in contact book! 🤷🏻‍♂️")

def delete_contact():
    print()
    name = input_taker("Enter name: ")
    if name in contact_book:
        view_contact(name)
        confirm = input("Confirm deletion? 🚮 (yes/no): ").lower()
        if confirm == "yes":
            contact_book.pop(name)
    else:
        print(f"{name} not in contact book! 🤷🏻‍♂️")

def menu():
    while True:
        print()
        print("""CHOICES:
1. Add contact
2. View contacts
3. Remove contact
4. Search contact
5. Quit""")
        print()
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            print()
            print("Thank you! 😊")
            break
        else:
            print()
            print("Invalid choice! 🥲")

menu()
