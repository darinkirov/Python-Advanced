import os


def create_file(file_name):
    with open(file_name, "w"):
        pass


def add_content(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + "\n")


def replace_content(file_name, old_string, new_string):
    try:
        with open(file_name, "r+") as file:
            file_content = file.read()
            updated_content = file_content.replace(old_string, new_string)
            file.seek(0)
            file.write(updated_content)
            file.truncate()
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input("Enter a command: ")
    if command == "End":
        break

    command_parts = command.split("-")
    action = command_parts[0]
    file_name = command_parts[1]

    if action == "Create":
        create_file(file_name)
    elif action == "Add":
        content = command_parts[2]
        add_content(file_name, content)
    elif action == "Replace":
        old_string = command_parts[2]
        new_string = command_parts[3]
        replace_content(file_name, old_string, new_string)
    elif action == "Delete":
        delete_file(file_name)
