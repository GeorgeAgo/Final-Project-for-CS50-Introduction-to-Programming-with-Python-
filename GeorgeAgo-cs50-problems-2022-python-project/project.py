from tabulate import tabulate
import datetime

def main():
    print("Welcome to your Agenda")

    notes = []
    contacts = {}
    count = 0

    while True:
        print("Menu: date , contacts , notes ")
        action1 = input("What would you like to to do? ").strip().lower()

        if action1 == "date":
            date()

        elif action1 == "contacts":
            action2 = input("Which task would you like to perform: view, create, delete, update?")
            if action2 == "create":
                try:
                    contacts, count = add_contact(contacts, count)
                    print("Contact created successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "delete":
                try:
                    delete_contact(contacts)
                    print("Contact deleted successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "update":
                try:
                    update_contact(contacts)
                    print("Contact updated successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "view":
                view_contact(contacts)

            else:
                print("Invalid action. Choose between view, create, delete, update...")

        elif action1 == "notes":
            action2 = input("Which action would you like to perform: view, create, delete, update?")
            if action2 == "create":
                try:
                    notes, count = add_note(notes, count)
                    print("Note created successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "delete":
                try:
                    delete_note(notes)
                    print("Note deleted successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "update":
                try:
                    update_note(notes)
                    print("Note updated successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif action2 == "view":
                view_note(notes)

            else:
                print("Invalid action. Choose between view, create, delete, update...")

        else:
            print("Invalid action. Choose between date, contacts, notes")


def date():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Date and Time:", formatted_datetime)


def view_note(notes):
    print(tabulate(notes, headers="keys", tablefmt="rounded_grid"))


def add_note(notes, i):
    task = input("Task: ")
    i += 1
    notes.append({"ID": i, "Task": task})
    return notes, i


def delete_note(notes):
    view_note(notes)

    while True:
        try:
            note_id_to_delete = int(input("Which task ID would you like to delete?: "))
            if any(note["ID"] == note_id_to_delete for note in notes):
                break
            else:
                print("Invalid task ID, try again.")
        except ValueError:
            print("Invalid input, try again.")

    notes = [note for note in notes if note["ID"] != note_id_to_delete]

    print("Note deleted successfully.")
    return notes


def update_note(notes):
    numbers = [note["ID"] for note in notes]

    while True:
        view_note(notes)
        try:
            i = int(input("Which note would you like to update?: "))
            if i in numbers:
                break
            else:
                print("Invalid note ID, try again.")
        except ValueError:
            print("Invalid input, try again.")

    new_task = input("What do you want to update it to?: ")
    for note in notes:
        if note["ID"] == i:
            note["Task"] = new_task

    print("Note updated successfully.")
    return notes


def view_contact(contacts):
    print(tabulate(contacts.items(), headers=["Name", "Telephone Number"], tablefmt="pretty"))


def add_contact(contacts, i):
    name = input("Name: ")
    telephone_number = input("Telephone Number: ")
    contacts[name] = telephone_number
    i += 1
    return contacts, i


def delete_contact(contacts):
    view_contact(contacts)

    while True:
        try:
            contact_name_to_delete = input("Which contact name would you like to delete?: ")
            if contact_name_to_delete in contacts:
                break
            else:
                print("Contact not found, try again.")
        except ValueError:
            print("Invalid input, try again.")

    del contacts[contact_name_to_delete]

    print(f"Contact '{contact_name_to_delete}' deleted successfully.")
    return contacts


def update_contact(contacts):
    names = list(contacts.keys())

    while True:
        view_contact(contacts)
        try:
            name_to_update = input("Which contact would you like to update?: ")
            if name_to_update in names:
                break
            else:
                print("Invalid contact name, try again.")
        except ValueError:
            print("Invalid input, try again.")

    new_telephone_number = input("What do you want to update the telephone number to?: ")
    contacts[name_to_update] = new_telephone_number

    print(f"Contact '{name_to_update}' updated successfully.")
    return contacts


if __name__ == "__main__":
    main()
