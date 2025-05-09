from database import add_entry, get_entries, create_table

menu = """
Please select one of the follwowing options:
1) Add new entry
2) View all entries
3) Exit

Your selection: """

welcome_message = "Welcome to the journal app!"

def prompt_new_entry():
    entry_content = input("What have you learned to day? ")
    entry_date = input("What is the date today? ")
    add_entry(entry_content, entry_date)

def view_entry(entries_list):
    for entry in entries_list:
        print(f"Date: {entry['date']}")
        print(f"Content: {entry['content']}")
        print("-" * 20)

create_table()
user_input = input(menu)

while user_input != "3":
    # for later use
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        entries = get_entries()
        view_entry(entries)
    else:
        print("Invalid selection. Please try again.")

    user_input = input(menu)

