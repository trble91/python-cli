from peewee import *

db = PostgresqlDatabase('contacts', user='banana', password='123',
                        host='localhost', port=5432)

db.connect()

# Define the Contact model
class BaseModel(Model):
    class Meta:
        database = db
    
class Contact(BaseModel):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=40)

john = Contact(first_name='John', last_name='Doe', email='john.doe@example.com').save
bobby = Contact(first_name='Bobby', last_name='Brown', email='brown.bobby@example.com').save
ricky = Contact(first_name='Ricky', last_name='Bell', email='Ricky.doe@example.com').save