import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import CENTER

# Connecting to the SQLite database
connection = sqlite3.connect("banco.sqlite")
cursor = connection.cursor()

# Creating the table if it doesn't exist
creating_sql_to_execute = """
CREATE TABLE IF NOT EXISTS product
    (
        id_product INTEGER PRIMARY KEY,
        name_product CHAR(60),
        price_product FLOAT(9, 2)
    )
"""
cursor.execute(creating_sql_to_execute)


def insert_data():
    id_product = entry_id.get()
    name_product = entry_name.get()
    price_product = entry_price.get()

    try:
        cursor.execute(f"INSERT INTO product VALUES ({id_product}, '{name_product}', {price_product})")
        connection.commit()
        messagebox.showinfo("Sucesso", "Inserido com sucesso")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def retrieve_data():
    id_product = entry_id.get()
    if id_product:
        result_returned = cursor.execute(f"SELECT * FROM product WHERE id_product={id_product}")
    else:
        result_returned = cursor.execute("SELECT * FROM product")
    products = result_returned.fetchall()

    # Clearing previous data in the listbox
    listbox_data.delete(0, tk.END)

    # Displaying the retrieved data in the listbox
    for product in products:
        listbox_data.insert(tk.END, f"ID: {product[0]} | Nome do produto: {product[1]} | Preço: {product[2]}")


def update_data():
    id_product = entry_id.get()
    name_product = entry_name.get()
    price_product = entry_price.get()

    try:
        cursor.execute(
            f"UPDATE product SET name_product='{name_product}', price_product={price_product} WHERE id_product={id_product}")
        connection.commit()
        messagebox.showinfo("Sucesso", "Atualizado com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def delete_data():
    id_product = entry_id.get()
    try:
        cursor.execute(f"DELETE FROM product WHERE id_product={id_product}")
        connection.commit()
        messagebox.showinfo("Success", "Deletado com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Here, you can implement your own logic to authenticate the user
    # For demonstration purposes, let's assume the username is "admin" and the password is "password"
    if username == "Dayvd" and password == "123":
        login_window.destroy()
        create_main_window()
    else:
        messagebox.showerror("Login Failed", "Senha ou usuário inválido")


# Function to create the main application window
def create_main_window():
    # Creating the Tkinter window
    window = tk.Tk()
    window.title("Produtos")

    # Centering the window on the screen
    window_width = 350
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Creating labels
    label_id = tk.Label(window, text="ID:")
    label_id.grid(row=0, column=0, padx=10, pady=5)
    label_name = tk.Label(window, text="Nome:")
    label_name.grid(row=1, column=0, padx=10, pady=5)
    label_price = tk.Label(window, text="Preço:")
    label_price.grid(row=2, column=0, padx=10, pady=5)

    # Creating entry fields
    global entry_id
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)
    global entry_name
    entry_name = tk.Entry(window)
    entry_name.grid(row=1, column=1, padx=10, pady=5)
    global entry_price
    entry_price = tk.Entry(window)
    entry_price.grid(row=2, column=1, padx=10, pady=5)

    # Creating buttons
    button_insert = ttk.Button(window, text="Inserir", command=insert_data)
    button_insert.grid(row=3, column=0, padx=10, pady=5)
    button_retrieve = ttk.Button(window, text="Ver tudo", command=retrieve_data)
    button_retrieve.grid(row=3, column=1, padx=10, pady=5)
    button_update = ttk.Button(window, text="Atualizar", command=update_data)
    button_update.grid(row=4, column=0, padx=10, pady=5)
    button_delete = ttk.Button(window, text="Deletar", command=delete_data)
    button_delete.grid(row=4, column=1, padx=10, pady=5)

    # Creating a listbox to display data
    global listbox_data
    listbox_data = tk.Listbox(window, width=50)
    listbox_data.grid(row=5, columnspan=2, padx=10, pady=5, sticky='nsew')

    # Starting the Tkinter event loop
    window.mainloop()


# Creating the login window
login_window = tk.Tk()
login_window.title("Login")

# Centering the login window on the screen
login_window_width = 200
login_window_height = 150
login_screen_width = login_window.winfo_screenwidth()
login_screen_height = login_window.winfo_screenheight()
login_x = int((login_screen_width / 2) - (login_window_width / 2))
login_y = int((login_screen_height / 2) - (login_window_height / 2))
login_window.geometry(f"{login_window_width}x{login_window_height}+{login_x}+{login_y}")

# Creating labels and entry fields for username and password
label_username = tk.Label(login_window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1, padx=10, pady=5)
label_password = tk.Label(login_window, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Creating a login button
button_login = ttk.Button(login_window, text="Login", command=login)
button_login.grid(row=2, columnspan=2, padx=10, pady=5, sticky='nsew')

# Starting the login window event loop
login_window.mainloop()

# Closing the database connection
connection.close()