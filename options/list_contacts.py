from contacts import contacts

def list_contacts():
	print('contacts\n')

	if not len(contacts):
		input('\nyour contact list is empty, press any key to return... ')

		return

	for i, contact in enumerate(contacts):
		is_favorite = contact['is_favorite']
		favorite_status = ' - *' if is_favorite else ''

		print(f'{i + 1}. {contact["name"]} - {contact["phone"]}{favorite_status}')

	input('\npress any key to return... ')
