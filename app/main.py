import argparse
from app.models import Contact

parser = argparse.ArgumentParser(description='Contact Book')

parser.add_argument('-c', '--create', metavar=('first_name', 'last_name', 'email'), nargs=3, help='Create a new contact')
parser.add_argument('-l', '--list', action='store_true', help='List all contacts')
parser.add_argument('-f', '--find', metavar='first_name', help='Find a contact by first name')

args = parser.parse_args()

if args.create:
    first_name, last_name, email = args.create
    contact = Contact.create(first_name=first_name, last_name=last_name, email=email)
    print('Contact created successfully.')

if args.list:
    contacts = Contact.select()
    for contact in contacts:
        print(f'{contact.first_name} {contact.last_name} - {contact.email}')

if args.find:
    first_name = args.find
    contacts = Contact.select().where(Contact.first_name == first_name)
    for contact in contacts:
        print(f'{contact.first_name} {contact.last_name} - {contact.email}')
