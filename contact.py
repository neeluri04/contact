class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, query):
        results = {name: details for name, details in self.contacts.items() if query in name or query in details['phone']}
        if not results:
            print(f"No contacts found for '{query}'.")
        else:
            for name, details in results.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated.")
        else:
            print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"No contact found with the name '{name}'.")

    def user_interface(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                phone = input("Enter new phone number (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                address = input("Enter new address (leave blank to keep current): ")
                self.update_contact(name, phone, email, address)
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Contact Management System
contact_manager = ContactManager()
contact_manager.user_interface()
