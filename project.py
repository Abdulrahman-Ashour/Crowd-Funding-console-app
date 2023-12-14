import re
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, password, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.projects = []

class Project:
    def __init__(self, title, details, target, start_time, end_time):
        self.title = title
        self.details = details
        self.target = target
        self.start_time = start_time
        self.end_time = end_time

users = []

def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    phone = input("Enter your phone number: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format")
        return

    if len(password) < 8 or password != confirm_password:
        print("Password must be at least 8 characters and match the confirmed password")
        return

    if not re.match(r"^01[0-2]{1}[0-9]{8}$", phone):
        print("Invalid phone number. It should be an Egyptian phone number starting with 01 and followed by 9 digits.")
        return

    user = User(first_name, last_name, email, password, phone)
    users.append(user)

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user.email == email and user.password == password:
            return user
        else:
            print("Not Registered User")

    #return None

def create_project(user):
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    target = input("Enter the total target: ")
    start_time = input("Enter the start time (YYYY-MM-DD): ")
    end_time = input("Enter the end time (YYYY-MM-DD): ")

    if len(title) == 0 or len(details) == 0:
        print("Title and details cannot be empty")
        return

    if not re.match(r"^\d+$", target):
        print("Total target must be a number")
        return

    try:
        start_time = datetime.strptime(start_time, "%Y-%m-%d")
        end_time = datetime.strptime(end_time, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    if start_time >= end_time:
        print("End time must be after start time")
        return

    project = Project(title, details, target, start_time, end_time)
    user.projects.append(project)

def view_projects(user):
    for project in user.projects:
        print(f"Title: {project.title}, Details: {project.details}, Target: {project.target}, Start time: {project.start_time}, End time: {project.end_time}")

def edit_project(user):
    title = input("Enter the title of the project you want to edit: ")
    for project in user.projects:
        if project.title == title:
            new_title = input("Enter the new title: ")
            new_details = input("Enter the new details: ")
            new_target = input("Enter the new total target: ")
            new_start_time = input("Enter the new start time (YYYY-MM-DD): ")
            new_end_time = input("Enter the new end time (YYYY-MM-DD): ")

            if len(new_title) == 0 or len(new_details) == 0:
                print("Title and details cannot be empty")
                return

            if not re.match(r"^\d+$", new_target):
                print("Total target must be a number")
                return

            try:
                new_start_time = datetime.strptime(new_start_time, "%Y-%m-%d")
                new_end_time = datetime.strptime(new_end_time, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format")
                return

            if new_start_time >= new_end_time:
                print("End time must be after start time")
                return

            project.title = new_title
            project.details = new_details
            project.target = new_target
            project.start_time = new_start_time
            project.end_time = new_end_time
            break
        else:
            print("There is no project with this name")

def delete_project(user):
    title = input("Enter the title of the project you want to delete: ")
    for project in user.projects:
        if project.title == title:
            user.projects.remove(project)
            print("Deleted Successfuly")
            break
        else:
            print("There is no project with this name")

def search_project(user):
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    for project in user.projects:
        if project.start_time <= date <= project.end_time:
            print(f"Title: {project.title}, Details: {project.details}, Target: {project.target}, Start time: {project.start_time}, End time: {project.end_time}")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user is not None:
                while True:
                    print("1. Create project")
                    print("2. View projects")
                    print("3. Edit project")
                    print("4. Delete project")
                    print("5. Search project")
                    print("6. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        create_project(user)
                    elif choice == "2":
                        view_projects(user)
                    elif choice == "3":
                        edit_project(user)
                    elif choice == "4":
                        delete_project(user)
                    elif choice == "5":
                        search_project(user)
                    elif choice == "6":
                        break
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
