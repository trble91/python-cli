from peewee import *

# Connect to the SQLite database
database = SqliteDatabase('database/contacts.db')

# Define the Contact model
class Contact(Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=40)

    class Meta:
        database = database
