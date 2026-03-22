# -------------------------------
# Student Management System
# Author: Kamil Efe Aşkın
# Description: Python console program to manage students with persistent storage.
# Features: Add, Find, Show All, Show by Age Range, Modify, Delete, Search by Criterion
# -------------------------------
# Student class with encapsulated attributes and getter/setter methods
# -------------------------------
class Student:
    def __init__(self, first_name, last_name, age, sex, major):
        # Initialize private attributes for each student
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__sex = sex
        self.__major = major

    # Getter methods to access private attributes
    def get_first_name(self): return self.__first_name
    def get_last_name(self): return self.__last_name
    def get_age(self): return self.__age
    def get_major(self): return self.__major

    # Setter methods to modify private attributes
    def set_first_name(self, v): self.__first_name = v
    def set_last_name(self, v): self.__last_name = v
    def set_age(self, v): self.__age = v
    def set_sex(self, v): self.__sex = v
    def set_major(self, v): self.__major = v

    # String representation of student object for printing
    def __str__(self):
        return f"{self.__first_name.title()} {self.__last_name.title()} | Age: {self.__age} | Sex: {self.__sex} | Major: {self.__major}"


# Global variables
# students list stores all Student objects
# FILE stores persistent data on disk
students = []
# Initialize default 10 students for the first run
students.extend([
    Student("Ali", "Yilmaz", 20, "M", "CS"),
    Student("Ayşe", "Demir", 21, "F", "Math"),
    Student("Mehmet", "Kaya", 22, "M", "Physics"),
    Student("Zeynep", "Aydin", 19, "F", "Biology"),
    Student("Can", "Çelik", 23, "M", "CS"),
    Student("Elif", "Şahin", 20, "F", "Chemistry"),
    Student("Ahmet", "Koç", 24, "M", "CS"),
    Student("Fatma", "Arslan", 22, "F", "Math"),
    Student("Burak", "Yildiz", 21, "M", "Engineering"),
    Student("Selin", "Kurt", 20, "F", "CS"),
])
FILE = "students.txt"

# Utility function to normalize input
# Strip whitespace and convert to lowercase
def clean(text):
    return text.strip().lower()

# Save current student list to file for persistent storage
# Each student's info is stored as comma-separated values
def save_to_file():
    with open(FILE, "w") as f:
        for s in students:
            f.write(f"{s.get_first_name()},{s.get_last_name()},{s.get_age()},{s.get_sex()},{s.get_major()}\n")


# Load student data from file into memory
# Clears current list first to avoid duplicates
def load_from_file():
    try:
        with open(FILE, "r") as f:
            students.clear()
            for line in f:
                fn, ln, age, sex, major = line.strip().split(",")
                students.append(Student(fn, ln, int(age), sex, major))
    except FileNotFoundError:
        # File not found: first run scenario
        pass


# Add a new student to the list and save to file
def add_student():
    if len(students) >= 100:
        print("Limit reached!")
        return

    fn = clean(input("First name: "))
    ln = clean(input("Last name: "))
    age = int(input("Age: "))
    sex = input("Sex: ")
    major = input("Major: ")

    students.append(Student(fn, ln, age, sex, major))
    save_to_file()
    print("Student added & saved.")


# Find a student by first and last name
# If found, display all infomation about the student
def find_student():
    fn = clean(input("First name: "))
    ln = clean(input("Last name: "))

    for s in students:
        if s.get_first_name() == fn and s.get_last_name() == ln:
            print("Found!:", s)
            return

    print("Student not found!!!")


# Show all students in the system
def show_all():
    if not students:
        print("No students")
        return
    for s in students:
        print(s)


# Show students within a given age range
def show_by_age_range():
    if not students:
        print("No students")
        return
    
    ages = [s.get_age() for s in students]
    print(f"System range: {min(ages)} - {max(ages)}")

    # Ask user for filtering range
    min_a = int(input("Min: "))
    max_a = int(input("Max: "))

    for s in students:
        if min_a <= s.get_age() <= max_a:
            print(s)


# Modify a student's attribute
# User specifies student and field to modify
def modify_student():
    fn = clean(input("First name: "))
    ln = clean(input("Last name: "))

    for s in students:
        if s.get_first_name() == fn and s.get_last_name() == ln:

            print("Fields: first_name, last_name, age, sex, major")
            field = input("Field: ").lower()
            val = input("New value: ")

            if field == "first_name":
                s.set_first_name(clean(val))
            elif field == "last_name":
                s.set_last_name(clean(val))
            elif field == "age":
                s.set_age(int(val))
            elif field == "sex":
                s.set_sex(val)
            elif field == "major":
                s.set_major(val)
            else:
                print("Invalid field")
                return

            save_to_file()
            print("Updated")
            return

    print("Student not found!!!")

# Delete a student from the list and file
def delete_student():
    fn = clean(input("First name: "))
    ln = clean(input("Last name: "))

    for s in students:
        if s.get_first_name() == fn and s.get_last_name() == ln:
            students.remove(s)
            save_to_file()
            print("Deleted!")
            return

    print("Student not found!!!")

# Bonus: Search by any criterion (first_name, last_name, age, sex, major)
def find_by_criterion():
    key = input("Search by (first_name, last_name, age, sex, major): ").lower()
    val = input("Value: ")

    if key != "age":
        val = clean(val)

    found = False

    for s in students:
        if key == "first_name" and s.get_first_name() == val:
            print(s); found = True
        elif key == "last_name" and s.get_last_name() == val:
            print(s); found = True
        elif key == "age" and s.get_age() == int(val):
            print(s); found = True
        elif key == "sex" and s.get_sex().lower() == val:
            print(s); found = True
        elif key == "major" and s.get_major().lower() == val:
            print(s); found = True

    if not found:
        print("No results!")


# Load students from file at startup
load_from_file()

# Main program menu loop
while True:
    print("\nWelcome to Student Management System")
    print("\n--- MENU ---")
    print("1 Add")
    print("2 Find")
    print("3 Show All")
    print("4 Age Range")
    print("5 Modify")
    print("6 Delete")
    print("7 Search (Bonus)")
    print("0 Quit")

    c = input("Choice: ")

    if c == "1": add_student()
    elif c == "2": find_student()
    elif c == "3": show_all()
    elif c == "4": show_by_age_range()
    elif c == "5": modify_student()
    elif c == "6": delete_student()
    elif c == "7": find_by_criterion()
    elif c == "0":
        print("Goodbye!")
        break
    else:
        print("X Invalid choice!")
        