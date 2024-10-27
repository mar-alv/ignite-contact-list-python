from contacts import contacts

def delete_contact():
	print('delete contact\n')

	if not len(contacts):
		input('\nyour contact list is empty, press any key to return... ')

		return

	for i, contact in enumerate(contacts):
		is_favorite = contact['is_favorite']
		favorite_status = ' - *' if is_favorite else ''

		print(f'{i + 1}. {contact["name"]} - {contact["phone"]}{favorite_status}')

	contact_index = int(input('\nwhich contact would you like to delete? '))

	try:
		contact = contacts[contact_index - 1]

		contacts.remove(contact)
	except Exception:
		input('\ncontact not found, press any key to return... ')
