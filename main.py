tasks=[]

while True:
    print("=========== Welcome to the TO DO LIST App ===========")
    print('''
        1) Add Task
        2) View Task
        3) Complete Task
        4) Delete Task
        5) Exit
        ''')
    
    try:
        choice=int(input("Enter your choice: "))
        # print(f"You selected option {choice}.")
    
    
        if choice==1:
            print("===| Add Task |===")
            task=input("\nEnter ur task name: ")
            tasks.append(task)
            
            print("Task added successfully!")
            
        elif choice==2:
            print("===| View Task |===")
            if not tasks:
                print("No tasks available")
            else:
                print("============| YOUR TASKS |============")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            
        elif choice==3:
            print("===| Complete Task |===")
        
        elif choice==4:
            print("===| Delete Task |===")
            # n=int(input("Enter the task number to delete: "))
            if not tasks:
                print("No tasks available to delete.")
            else:
                print("=======| YOUR TASKS |=======")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                n=int(input("Enter task number to delete! : "))
                if n>=1 and n<=len(tasks):
                    actual_index=n-1
                    deleted=tasks.pop(actual_index)
                    print(f"Task '{deleted}' deleted successfully!!")
                else:
                    print("Plz enter a valid task number...")
            

        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
        
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
    print()