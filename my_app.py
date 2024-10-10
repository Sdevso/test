todos=[]

while True:
    user_action = input("Type add,show,edit, complete or exit : ").strip().lower()
    match user_action:
        case'add':
            todo = input("Enter the todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate( todos):
                print(f"{index+1}-{item}")
        case 'edit':
            number= int(input("number of todo to edit:"))
            number=number-1
            new_todo=input("Enter new todo: ")
            todos[number]= new_todo
        case 'complete':
            number= int(input("number of todo to complete:"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("enter the correct choice")

print("bye")