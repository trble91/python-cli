# Python CLI-Project

## Contact Book Command Line Application

This is a command line application built in Python that allows users to create and manage contacts using a SQL database with PeeWee models.

## Prerequisites

- Python
- PeeWee

## Installation

1. Clone the repository:

2. Install the required dependencies:

## Usage

To run the application, navigate to the project directory and execute the `main.py` script:

### Options

- `-c`, `--create`: Create a new contact. Requires three arguments: `first_name`, `last_name`, and `email`.
- `-l`, `--list`: List all contacts.
- `-f`, `--find`: Find a contact by their first name. Requires the `first_name` argument.

### Examples

Create a new contact:
```.py
--create John Doe john.doe@example.com
```

List all contacts:
```
```

Find a contact by first name:
```
```


## Database

The application uses a SQLite database to store contacts. The database file is located at `database/contacts.db`. The tables are created automatically when you run the seed script.

## Seed Script

To create the database and tables, use the seed script `seed.py`. Run the following command:

## Contributing

Contributions are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).




