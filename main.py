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
            print("Add Task selected")
            task=input("\n Enter ur task name: ")
            tasks.append(task)
            
            print("Task added successfully!")
            print(tasks)
            
        elif choice==2:
            print("\n Option 2 - View Task selected")
            if tasks == []:
                print("No tasks available")
            else:
                print("============ YOUR TASKS ============")
                for task in tasks:
                    print(tasks)
            
        elif choice==3:
            print("Complete Task selected")
        
        elif choice==4:
            print("Delete Task selected")

        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
        
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
    print()