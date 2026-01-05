contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        name = input("Enter contact name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact {name} added.")

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"Contact found: {name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter contact name to delete:")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print("Contact not found.")

    elif choice == '5':
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new phone number:")
            email = input("Enter new email: ")
            contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact {name} updated.")
        else:
            print("Contact not found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Book. Goodbye!")
        break