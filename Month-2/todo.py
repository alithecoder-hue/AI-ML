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
            category TEXT DEFAULT 'personal' ,
            due_date TEXT ,
            created_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database created successfully")


def add_task(task_name , priority='medium', category ='personal', due_date = None):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    created_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute('''
        INSERT INTO tasks (task_name, status, priority, category, due_date, created_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''',(task_name, 'pending', priority, category, due_date, created_date))
    conn.commit()
    conn.close()
    print(f"Task added: {task_name} (Priority: {priority} | category: {category})")

def view_tasks(filter_by=None):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    if filter_by == 'pending':
        cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
    elif filter_by == 'complete':
        cursor.execute("SELECT * FROM tasks WHERE status = 'complete'")
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

def search_tasks(keyword):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tasks
        WHERE task_name LIKE ?
        ORDER BY due_date
    ''' , (f'%{keyword}%',))

    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print(f"\n No tasks found containing {keyword}")
        return
    
    print(f"Search Result for {keyword}")
    print("="*80)
    print(f"{'ID':<4}, {'Task':<25}, {'Status':<10}, {'Priority':<8}, {'category':<10}, {'Due Date':<12}")
    print("="*80)

    for task in tasks:
        status_icon = '✅' if task[2] == 'complete' else '⏳'
        priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
        category = task[4].capitalize() if task[4] else 'Personal'
        due = task[5] if task[5] else 'No date'

        print(f"{'task[0]':<4},  {'task[1]':<25}, {status_icon}, {'task[2]':<8}, {priority_icon}, {'task[3]':<6}, {category:<10}, {due:<12}")
        print("="*80)

def filter_by_status():
    print("Filter by Status: ")
    print("1. Pending")
    print("2. Completed")

    choice = input("\n Choose (1-2): ")

    if choice == "1":
        view_tasks('pending')
    elif choice == "2":
        view_tasks('complete')
    else:
        print("Invalid choice")

def filter_by_category():
    print("\n Filter by category: ")
    print("1. Work")
    print("2. Personal")
    print("3. Study")
    print("4. other")

    choice = input("\n Choose (1-4): ")

    category_map = {'1':'work', '2':'personal', '3':'study', '4':'other'}
    category = category_map(choice)

    if not category:
        print("\n Invalid choice")
        return
    
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE categoty = ? ORDER BY due_date", (category,))
    tasks= cursor.fetchall()
    conn.close()

    if not tasks:
        print(f"\n No tasks in {category} category")
        return
    
    print(f"Tasks in {category.upper()} Category")
    print("="*80)
    print(f"{'ID':<4}, {'Task':<25}, {'Status':<10}, {'priority':<8}, {'Due Date':<12}")
    for task in tasks:
        status_icon = '✅' if task[2] == 'complete' else '⏳'
        priority_icon = {'high':'🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
        due = task[5] if task[5] else 'No date'

        print(f"{task[0]:<4} {task[1]:<25} {status_icon} {task[2]:<8} {priority_icon} {task[3]:<6} {due:<12}")
    print("="*80)

def filter_by_priority():
    print("Filter by priority: ")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("\n Choose (1-3): ")
    priority_map = {'1':'high', '2':'medium', '3':'low'}
    priority = priority_map.get(choice)

    if not priority:
        print("Invalid choice")
        return
    
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE priority = ? ORDER BY due_date", (priority,))
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print(f"No tasks with {priority} priority!")
        return
    priority_icon = {'high':'🔴', 'medium':'🟡', 'low':'🟢'}.get(priority,'⚪')

    print(f"\n TASKS WITH {priority.upper()} PRIORITY {priority_icon}")
    print("="*80)
    print(f"{'ID':<4}, {'Task':<25}, {'Status':<10}, {'Due Date':<12}")
    print("="*80)
    
    for task in tasks:
        status_icon = '✅' if task[2] == 'complete' else '⏳'
        category = task[4].capitalize() if task[4] else 'Personal'
        due = task[5] if task[5] else 'No date'

        print(f"{task[0]:<4} {task[1]:<25} {status_icon} {task[2]:<8} {category:10} {due:<12}")
    print("="*80)

def view_by_category():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT category FROM tasks")
    categories = cursor.fetchall()

    if not categories:
        print("\n No task found")
        conn.close()
        return
    print("\n Available Categories: ")
    for i , cat in enumerate(categories, 1):
        print(f"{i}. {cat[0].capitalize()}")

    choice = input("\n Choose category number: ")
    try:
        cat_index = int(choice) - 1
        selected_category = categories[cat_index][0]

        cursor.execute("SELECT * FROM tasks WHERE category = ? ORDER BY due_date" , (selected_category,))
        tasks = cursor.fetchall()

        if not tasks:
            print(f"\n No task in {selected_category} category")
        else :
            print(f"No task in {selected_category.upper()} category")
            print("="*80)
            print(f"{'ID':<4}, {'task':<25}, {'status':<10}, {'priority':<8}, {'Due Date':<12}")
            print("="*80)

            for task in tasks:
                status_icon = '✅' if task[2] == 'complete' else '⏳'
                priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
                due = task[5] if task[5] else 'No date'
                
                print(f"{task[0]:<4} {task[1]:<25} {status_icon} {task[2]:<8} {priority_icon} {task[3]:<6} {due:<12}")
            print("="*80)
    except:
        print("❌ Invalid choice!")
    
    conn.close()

def view_overdue_tasks():
    """Show tasks with due date before today"""
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute('''
        SELECT * FROM tasks 
        WHERE due_date IS NOT NULL 
        AND due_date < ? 
        AND status = 'pending'
        ORDER BY due_date
    ''', (today,))
    
    tasks = cursor.fetchall()
    conn.close()
    
    if not tasks:
        print("\n✅ No overdue tasks! Great job!")
        return
    
    print("\n⚠️ OVERDUE TASKS ⚠️")
    print("="*80)
    print(f"{'ID':<4} {'Task':<25} {'Priority':<8} {'Due Date':<12}")
    print("="*80)
    
    for task in tasks:
        priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
        print(f"{task[0]:<4} {task[1]:<25} {priority_icon} {task[3]:<6} {task[5]:<12}")
    
    print("="*80)

def view_due_today():
    """Show tasks due today"""
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute('''
        SELECT * FROM tasks 
        WHERE due_date = ? 
        AND status = 'pending'
        ORDER BY priority
    ''', (today,))
    
    tasks = cursor.fetchall()
    conn.close()
    
    if not tasks:
        print("\n🎉 No tasks due today! Enjoy your day!")
        return
    
    print("\n📅 TASKS DUE TODAY")
    print("="*80)
    print(f"{'ID':<4} {'Task':<25} {'Priority':<8}")
    print("="*80)
    
    for task in tasks:
        priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
        print(f"{task[0]:<4} {task[1]:<25} {priority_icon} {task[3]:<6}")
    
    print("="*80)

def view_sorted_by_date():
    """View all tasks sorted by due date"""
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM tasks 
        ORDER BY 
            CASE WHEN due_date IS NULL THEN 1 ELSE 0 END,
            due_date
    ''')
    
    tasks = cursor.fetchall()
    conn.close()
    
    if not tasks:
        print("\n📭 No tasks found!")
        return
    
    print("\n📅 TASKS SORTED BY DUE DATE")
    print("="*90)
    print(f"{'ID':<4} {'Task':<25} {'Status':<10} {'Priority':<8} {'Category':<10} {'Due Date':<12}")
    print("="*90)
    
    for task in tasks:
        status_icon = '✅' if task[2] == 'complete' else '⏳'
        priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(task[3], '⚪')
        due = task[5] if task[5] else 'No date'
        category = task[4].capitalize() if task[4] else 'Personal'
        
        print(f"{task[0]:<4} {task[1]:<25} {status_icon} {task[2]:<8} {priority_icon} {task[3]:<6} {category:<10} {due:<12}")
    
    print("="*90)




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
        print("7. View by category")
        print("8. View overdue tasks")
        print("9. View tasks due today")
        print("10. Sort by due date")
        print("11. Search tasks")
        print("12. Filter by status")
        print("13. Filter by category")
        print("14. Filter by priority")
        print("15. Exit")

        choice = input("\n Choose (1-15): ")

        if choice == "1":
            task_name = input("Enter task: ")
            print("\n Priority Option:")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            priority_choice = input("Choose priority (1-3): ")

            priority_map ={'1': 'high', '2': 'medium', '3': 'low'}
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
        elif choice == "7":
            view_by_category()
        elif choice == "8":
            view_overdue_tasks()
        
        elif choice == "9":
            view_due_today()
        
        elif choice == "10":
            view_sorted_by_date()
        elif choice == "11":
            keyword = input("\n enter keyword to search: ")
            search_tasks(keyword)
        elif choice == "12":
            filter_by_status()
        elif choice == "13":
            filter_by_category()
        elif choice == "14":
            filter_by_priority()
        elif choice == "15":
            print("\n Goodbye! Stay productive")
            break
        else:
            print("\n❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()