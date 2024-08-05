import re
def main():
    while True:
        contacts = {}
        ans = input('''
"Welcome to the Contact Management System!!!
Please enter a number to select an option:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit 
''')
        if ans == '1':
            add_contact(contacts)
            print('Contact added successfully.')
        elif ans == '2':
            edit_contact(contacts)
        elif ans == '3':
            delete_contact(contacts)
        elif ans == '4':
            search_contact(contacts)
        elif ans == '5':
            display_contacts(contacts)
            print()
        elif ans == '6':
            export_to_text(contacts)
            print('Contacts exported successfully to contacts.txt.')
            
        elif ans == '7':
            contacts = import_from_text()
            print('Contacts imported successfully from contacts.txt.')
            print()
           
        elif ans == '8':    
            print('Thank you for using the Contact Management System. Goodbye!')
            break
       

def add_contact(contacts):   
    name = input('Enter the name of the contact: ')
    phone = input('Enter the phone number of the contact: ')
    email = input('Enter the email address of the contact: ')
    contacts[name] = {'phone': phone, 'email': email}
    return contacts

def edit_contact(contacts):
    name = input('Enter the name of the contact you want to edit: ')
    if name in contacts.keys():                                              
        phone = input('Enter the new phone number of the contact: ')
        email = input('Enter the new email address of the contact: ')
        contacts[name] = {'phone': phone, 'email': email}
        print('Contact edited successfully.')
    else:
        print('Contact not found.')
    
def delete_contact(contacts):
    option = int(input("Choose a contact to delete:"))
    contacts = contacts.pop(option -1)
    print(f"{contacts['name']} deleted")

def search_contact(contacts):
    for name, email in contacts:
        if re.match(r"(^[A-Z]{1)", name):  #if name starts with a capital letter - print FAiled HArd- need Help 
            print(f'Name: {name}, Email: {email}')
        else: (f"{name} is Invalid")

def display_contacts(contacts):             #GOLD
    if len(contacts) == 0:
        print('No contacts to display.')
    else:
        for name in contacts.keys():
            print(f'Name: {name}, Phone: {contacts[name]["phone"]}, Email: {contacts[name]["email"]}')

def export_to_text(contacts):
    with open('contacts.txt', 'w') as file:
        for name, details in contacts.items():
            file.write(f'{name},{details["phone"]},{details["email"]}\n')

def import_from_text():
    contacts = {}
    with open('contacts.txt', 'r') as file:
        for line in file:
            name, phone, email = line.strip().split(',')
            contacts[name] = {'phone': phone, 'email': email}
    return contacts

main()




    




    
