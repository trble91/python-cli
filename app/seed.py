from models import db, Contact

# Create the database tables
db.drop_tables([Contact])
db.create_tables([Contact])

