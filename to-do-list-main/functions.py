import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="to_do_list"
)

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice not in (1, 2, 3, 4):
                raise ValueError()
            return choice
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")

def create_task():
    cursor = connection.cursor()
    query = "INSERT INTO task (title, dsc) VALUES (%s, %s)"
    data = (input("insert the title of the task: ").upper() , input("insert the description of the task: "))
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

def delete_task():
    id = show_tasks()
    cursor = connection.cursor()
    query = f"DELETE FROM task WHERE id = {id};"
    cursor.execute(query)
    connection.commit()
    cursor.close()

def view_task():
# Get the task ID using the show_tasks() function
    id = show_tasks()
    cursor = connection.cursor()
    query = f"SELECT * FROM task WHERE id = {id}"
    cursor.execute(query)
    task = cursor.fetchone()

    if task:
        # Assuming the column order in the 'task' table is: id, title, dsc
        task_id, title, description, date = task
        date = date.strftime("%Y-%m-%d %H-%M-%S")
        print(f"\n{task_id}. {title}\n   {description}\n{date}\n")

def show_tasks():
    cursor = connection.cursor()

    query = "SELECT id, title FROM task"
    cursor.execute(query)

    # Fetch the rows and store them in a variable
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
        return None

    print("===== Your Task Titles =====")
    for index, (task_id, title) in enumerate(tasks, start=1):
        print(f"{index}. {title}")
    print("=============================")

    selected_index = int(input("Select the task to operate: "))

    if 1 <= selected_index <= len(tasks):
        selected_task_id = tasks[selected_index - 1][0]
        return selected_task_id
    else:
        print("Invalid task selection. Please choose a valid task.")
        return None

def check_table():
    #returns true if table doesn't have data
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM task"
    cursor.execute(query)
    count_result = cursor.fetchone()
    if count_result and count_result[0] > 0:
        return True
    else:
        return False

