import tkinter as tk 
import sqlite3

# Create a SQLite database and a table to store contacts 
conn = sqlite3.connect("contacts2.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts ( id INTEGER PRIMARY KEY,
name TEXT, email TEXT
)''')
conn.commit()

# Function to add a new contact to the database 
def add_contact():
    name = name_entry.get() 
    email = email_entry.get()
    cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email)) 
    conn.commit()
    update_contact_list() 
    name_entry.delete(0, tk.END) 
    email_entry.delete(0, tk.END)

# Function to display contacts in the GUI 
def update_contact_list():
    contact_listbox.delete(0, tk.END) 
    cursor.execute("SELECT * FROM contacts") 
    contacts = cursor.fetchall()
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact[1]} - {contact[2]}")

# Create the main window 
root = tk.Tk() 
root.title("Contact Manager")

# Create GUI elements with increased width and spacing 
name_label = tk.Label(root, text="Name:", width=10) 
name_entry = tk.Entry(root, width=30)
email_label = tk.Label(root, text="Email:", width=10) 
email_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Contact", command=add_contact) 
contact_listbox = tk.Listbox(root, width=40, height=10)

# Place GUI elements with spacing using the grid layout manager 
name_label.grid(row=0, column=0, padx=10, pady=5) 
name_entry.grid(row=0, column=1, padx=10, pady=5) 
email_label.grid(row=1, column=0, padx=10, pady=5) 
email_entry.grid(row=1, column=1, padx=10, pady=5) 
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 
contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI application 
root.mainloop()

# Close the database connection when the GUI is closed 
conn.close()

