import os 
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "journal.txt")

open(FILE_NAME, "w").close()



def add_entry():
    print("\nAdd New Entry:")
    print("User Input:")

    print("\nEnter your journal entry:")
    entry = input()

    with open(FILE_NAME, "w") as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{date_time}]\n")
        file.write(entry + "\n")

    print("\nEntry added successfully!")


def view_entries():
    print("\nView All Entries:")
    print("User Input:")


    print("\nOutput (If the file exists):")

    if not os.path.exists(FILE_NAME):
        print("No journal entries found. Start by adding a new entry!")
        return

    with open(FILE_NAME, "r") as file:
        data = file.read()

    if data.strip():
        print("Your Journal Entries:")
        print(data)
    else:
        print("No journal entries found. Start by adding a new entry!")


def search_entry():
    print("\nSearch for Entry:")
    print("User Input:")

    print("\nEnter a keyword or date to search:")
    keyword = input()

    print("\nOutput (If a match is found):")
    print("Matching Entries:")
    print("-------------------------")

    if not os.path.exists(FILE_NAME):
        print("No journal entries found for the keyword:", keyword)
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    for i in range(0, len(lines), 3):
        if i + 1 < len(lines):
            date_line = lines[i].strip()
            entry_line = lines[i + 1].strip()

            if keyword.lower() in date_line.lower() or keyword.lower() in entry_line.lower():
                print(date_line)
                print(entry_line)
                print()
                found = True

    print("\nOutput (If no match is found):")

    if not found:
        print("No entries were found for the keyword:", keyword)


def delete_entries():
    print("\nDelete All Entries:")
    print("User Input:")

    print("\nAre you sure you want to delete all entries? (yes/no):")
    choice = input()

    if choice.lower() == "yes":
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

        print("\nOutput (If the file is deleted successfully):")
        print("All journal entries have been deleted.")
    else:
        print("\nNo journal entries were deleted.")

#-------------main menu-----------#
def main():
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:\n")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    while True:
        print("\nEnter your choice:")
        choice = input()

        if choice == "1":
            add_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            search_entry()

        elif choice == "4":
            delete_entries()

        elif choice == "5":
            print("\nExit:")
            print("User Input:")
            print("5")

            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid Input:")
            print("Output:")
            print("Invalid option. Please select a valid option from the menu.")


main()