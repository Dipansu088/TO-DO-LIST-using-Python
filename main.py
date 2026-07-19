tasks=[]

while True:
    print("\n===========| Welcome to the TO DO LIST App |===========")
    print('''
        1) Add Task
        2) View Task
        3) Complete Task
        4) Delete Task
        5) Exit
        6) Mark Incomplete
        ''')
    
    try:
        choice=int(input("Enter your choice: "))    
    
        if choice==1:
            print("\n============| Add Task |============")
            task=input("\nEnter task name: ")
            tasks.append({
                "task": task,
                "completed": False
            })
            
            print("Task added successfully!")
            
        elif choice==2:
            print("\n============| View Task |============")
            if not tasks:
                print("No tasks available")
            else:
                print("\n============| YOUR TASKS |============")
                for number, task_item in enumerate(tasks, start=1):
                    if task_item['completed'] is True:
                        print(f"{number}. {task_item['task']} - Completed") 
                    else:
                        print(f"{number}. {task_item['task']} - Incomplete")
                             
            
        elif choice==3:
            print("\n============| Complete Task |============")
            if not tasks:
                print("\nNo tasks available to mark.")
            else:
                print("\n=======| YOUR TASKS |=======")
                for number, task_item in enumerate(tasks, start=1):
                    print(f"{number}. {task_item['task']}")
                n=int(input("\nEnter task number to complete: "))
                if n>=1 and n<=len(tasks):
                    actual_index=n-1
                    tasks[actual_index]['completed']=True
                    print(f"Task {tasks[actual_index]['task']} marked as completed!")
                else:
                    print("Please enter a valid task number.")
        
        elif choice==4:
            print("\n============| Delete Task |============")
            if not tasks:
                print("\nNo tasks available to delete.")
            else:
                print("\n=======| YOUR TASKS |=======")
                for number, task_item in enumerate(tasks, start=1):
                    print(f"{number}. {task_item['task']}")
                n=int(input("\nEnter task number to delete: "))
                if n>=1 and n<=len(tasks):
                    actual_index=n-1
                    deleted=tasks.pop(actual_index)
                    print(f"Task '{deleted['task']}' deleted successfully!!")
                else:
                    print("Plz enter a valid task number.")
            

        elif choice==5:
            print("Exiting...")
            break
        
        elif choice==6:
            print("\n============| Mark as Incomplete |============")
            if not tasks:
                print("\nNo tasks available to mark.")
            else:
                print("\n=======| YOUR TASKS |=======")
                for number, task_item in enumerate(tasks, start=1):
                    print(f"{number}. {task_item['task']}")
                n=int(input("\nEnter task number to complete: "))
                if n>=1 and n<=len(tasks):
                    actual_index=n-1
                    tasks[actual_index]['completed']=False
                    print(f"Task {tasks[actual_index]['task']} marked as incomplete!")
                else:
                    print("Please enter a valid task number.")

        
        else:
            print("Invalid Choice")
        
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
    print("----------------------------------------")