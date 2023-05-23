import mysql.connector
from tkinter import Tk, Button, StringVar, OptionMenu, Text, messagebox, Toplevel

# Step 1: Read the file
filename = "Marvel.txt"
with open(filename, "r") as file:
    lines = file.readlines()

# Step 2: Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS marvel_movies (
    ID INT PRIMARY KEY,
    MOVIE VARCHAR(255),
    DATE DATE,
    MCU_PHASE VARCHAR(50)
)
"""

# Step 3: Populate the table
insert_query = "INSERT INTO marvel_movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"

def populate_table():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()
    for line in lines:
        data = line.split("\t")
        movie_id = int(data[0])
        movie_title = data[1]
        release_date = data[2]
        mcu_phase = data[3]
        values = (movie_id, movie_title, release_date, mcu_phase)
        cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Step 4: Design the interface
root = Tk()

def add_button_clicked():
    popup = Toplevel(root)
    popup.title("Add Movie")
    label = Label(popup, text="Enter movie details:")
    label.pack()
    movie_entry = Entry(popup)
    movie_entry.pack()
    ok_button = Button(popup, text="Ok", command=lambda: add_movie_to_database(movie_entry.get()))
    ok_button.pack()
    cancel_button = Button(popup, text="Cancel", command=popup.destroy)
    cancel_button.pack()

def add_movie_to_database(movie_title):
    # Add the movie to the database using the provided title
    # Execute the database insertion query

def list_all_button_clicked():
    # Retrieve all data from the database and display in the text box

add_button = Button(root, text="Add", command=add_button_clicked)
add_button.pack()

list_all_button = Button(root, text="LIST ALL", command=list_all_button_clicked)
list_all_button.pack()

movie_ids = [1, 2, 3, ...]  # List of movie IDs from the database

selected_movie_id = StringVar()
dropdown = OptionMenu(root, selected_movie_id, *movie_ids)
dropdown.pack()

text_box = Text(root, height=10, width=50)
text_box.pack()

root.mainloop()
