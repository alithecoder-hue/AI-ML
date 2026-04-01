import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            priority TEXT DAFAULT 'medium',
            created_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database created successfully")


def add_task(task_name , priority='medium'):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    created_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute('''
        INSERT INTO tasks (task_name, status, priority, created_date)
        VALUES (?, ?, ?, ?)
    ''',(task_name, 'pending', priority, created_date))
    conn.commit()
    conn.close()
    print(f"Task added: {task_name} (Priority: {priority})")

def view_tasks(filter_by=None):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    if filter_by == 'pending':
        cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
    elif filter_by == 'complete':
        cursor.execute("SELEXT * FROM tasks WHERE status = 'complete'")
    else:
        cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("\n No tasks found")
        return
    print("\n"+"="*60)
    print(f"{'ID':<4}{'Task':<30}{'Priority':<8}{'Created'}")
    print("="*60)

    for task in tasks:
        priority_icon = {
            'high' : '🔴',
            'medium' : '🟡',
            'low' : '🟢'
        }.get(task[3], '⚪')

        status_icon = '✅' if task[2] == 'complete' else '⏳'

        print(f"{task[0]:<4} {task[1]:<30}{status_icon}{task[2]:<8}{priority_icon}{task[3]:<6}{task[4]}")
        print("="*60)

def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET status = 'complete' WHERE id=?", (task_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Task {task_id} marked as complete")
    else:
        print(f"Task {task_id} not Found")
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor= conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE  id = ?", (task_id,))

    if cursor.rowcount >0 :
        conn.commit()
        print(f"Task {task_id} deleted")
    else:
        print(f"Task {task_id} not found")
    conn.close()

def main():
    create_database()

    while True:
        print("\n"+"="*50)
        print("To DO App Menu")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. view  Completed Tasks")
        print("5. Mask Task as complete")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("\n Choose (1-7): ")

        if choice == "1":
            task_name = input("Enter task: ")
            print("\n Priority Option:")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            priority_choice = input("Choose priority (1-3): ")

            priority_map ={'1': 'High', '2': 'medium', '3': 'low'}
            priority = priority_map.get(priority_choice , 'medium')

            add_task(task_name, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks('pending')
        elif choice == "4":
            view_tasks('complete')
        elif choice == "5":
            view_tasks('pending')
            task_id =input("Enter Task ID to mark Complete: ")
            complete_task(task_id)
        elif choice == "6":
            view_tasks()
            task_id =input("Enter Task ID to Delete: ")
            delete_task(task_id)
        elif choice == "7" :
            print("Good Bye")
            break
        else:
            print("Invalid Choice Please Choose between 1-7")

if __name__ == "__main__":
    main()