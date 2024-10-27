import os

from options.add_contact import add_contact
from options.list_contacts import list_contacts
from options.edit_contact import edit_contact
from options.favorite_contact import favorite_contact
from options.list_favorite_contacts import list_favorite_contacts
from options.delete_contact import delete_contact

def menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		option = input('''contact list

1. add contact
2. list contacts
3. edit contact
4. favorite contact
5. list favorites contacts
6. delete contact
7. exit

what would you like to do? ''')

		os.system('cls' if os.name == 'nt' else 'clear')

		match option:
			case '1': add_contact()
			case '2': list_contacts()
			case '3': edit_contact()
			case '4': favorite_contact()
			case '5': list_favorite_contacts()
			case '6': delete_contact()
			case '7': return False

menu()
