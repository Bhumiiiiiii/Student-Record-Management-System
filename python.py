import sqlite3

# Connect to database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

# Functions
def add_student(name, age):
    c.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Student added successfully.")

def update_student(student_id, name, age):
    c.execute("UPDATE students SET name=?, age=? WHERE id=?", (name, age, student_id))
    conn.commit()
    print("Student updated successfully.")

def view_students():
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    for row in rows:
        print(row)

def delete_student(student_id):
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")

# Menu
while True:
    print("\n1. Add Student\n2. Update Student\n3. View Students\n4. Delete Student\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        add_student(name, age)
    elif choice == '2':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        update_student(student_id, name, age)
    elif choice == '3':
        view_students()
    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)
    elif choice == '5':
        break
    else:
        print("Invalid choice")
