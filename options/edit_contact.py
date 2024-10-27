from contacts import contacts

def edit_contact():
	print('edit contact\n')

	if not len(contacts):
		input('\nyour contact list is empty, press any key to return... ')

		return

	for i, contact in enumerate(contacts):
		is_favorite = contact['is_favorite']
		favorite_status = ' - *' if is_favorite else ''

		print(f'{i + 1}. {contact["name"]} - {contact["phone"]}{favorite_status}')

	contact_index = int(input('\nwhich contact would you like to edit? '))

	try:
		contact = contacts[contact_index - 1]

		name = input('\nname? ')
		phone = input('phone? ')

		contact['name'] = name
		contact['phone'] = phone
	except Exception:
		input('\ncontact not found, press any key to return... ')
