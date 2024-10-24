import mysql.connector
import functions as f

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="to_do_list"
)

while True:

    print("===== ToDo List Menu =====")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("===========================")

    choice = f.get_user_choice()

    if choice == 1:
        f.create_task()
    elif choice == 2:
        if f.check_table():
            f.view_task()
        else:
            print("No task registred, please create one in order to access it")
    elif choice == 3:
        if f.check_table():
            f.delete_task()
        else: print("No tasks registred")
    else:
        break

connection.disconnect()
    



