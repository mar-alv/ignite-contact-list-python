from contacts import contacts

def favorite_contact():
	print('favorite contact\n')

	if not len(contacts):
		input('\nyour contact list is empty, press any key to return... ')

		return

	for i, contact in enumerate(contacts):
		is_favorite = contact['is_favorite']
		favorite_status = ' - *' if is_favorite else ''

		print(f'{i + 1}. {contact["name"]} - {contact["phone"]}{favorite_status}')

	contact_index = int(input('\nwhich contact would you like to favorite? '))

	try:
		contact = contacts[contact_index - 1]

		contact['is_favorite'] = True
	except Exception:
		input('\ncontact not found, press any key to return... ')
