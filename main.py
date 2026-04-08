def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    
    with open("notes.txt", "a") as file:
        file.write(title + "|" + content + "\n")
    
    print("Note added successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            
            if not notes:
                print("No notes found!")
                return
            
            print("\n--- Your Notes ---")
            for i, note in enumerate(notes, start=1):
                title, content = note.strip().split("|")
                print(f"{i}. {title} - {content}")
    
    except FileNotFoundError:
        print("No notes found!")


def delete_note():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        
        if not notes:
            print("No notes to delete!")
            return
        
        print("\n--- Notes ---")
        for i, note in enumerate(notes, start=1):
            title, content = note.strip().split("|")
            print(f"{i}. {title} - {content}")
        
        num = int(input("Enter note number to delete: "))
        
        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            
            print("Note deleted successfully!")
        else:
            print("Invalid number!")
    
    except FileNotFoundError:
        print("No notes found!")


# MAIN MENU
while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
