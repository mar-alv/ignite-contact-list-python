from contacts import contacts

def list_favorite_contacts():
	print('favorite contacts\n')

	if not len(contacts):
		input('\nyour contact list is empty, press any key to return... ')

		return

	if all(not contact['is_favorite'] for contact in contacts):
		input('\nyour favorite list is empty, press any key to return... ')

		return

	for i, contact in enumerate(contacts):
		is_favorite = contact['is_favorite']

		if is_favorite:
			print(f'{i + 1}. {contact["name"]} - {contact["phone"]} - *')

	input('\npress any key to return... ')
