from contacts import contacts

def add_contact():
	print('create contact')

	name = input('\nname? ')
	phone = input('phone? ')

	contact = {
		'name': name,
		'phone': phone,
		'is_favorite': False
	}

	contacts.append(contact)
