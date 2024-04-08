import sqlite3

# Function to create a new database if not exists
def create_database():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add a new contact
def add_contact(name, phone, email):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

# Function to view all contacts
def view_contacts():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Function to update a contact
def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()

# Function to delete a contact
def delete_contact(contact_id):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

# Main function to run the application
def main():
    create_database()

    while True:
        print("\n===== Address Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            contact_id = int(input("Enter contact id to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            update_contact(contact_id, name, phone, email)
        elif choice == '4':
            contact_id = int(input("Enter contact id to delete: "))
            delete_contact(contact_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

