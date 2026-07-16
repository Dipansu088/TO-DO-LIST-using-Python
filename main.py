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
        print(f"You selected option {choice}.")
    
    
        if choice==1:
            print("Add Task selected")
            
        elif choice==2:
            print("View Task selected")
            
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
        print("Invalid Input. Plz enter INTEGER only.")