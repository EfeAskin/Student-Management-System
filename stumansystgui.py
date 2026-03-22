import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

# -------------------------------
# Student class
# -------------------------------
class Student:
    def __init__(self, first_name, last_name, age, sex, major):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__sex = sex
        self.__major = major

    def get_first_name(self): return self.__first_name
    def get_last_name(self): return self.__last_name
    def get_age(self): return self.__age
    def get_sex(self): return self.__sex
    def get_major(self): return self.__major

    def set_first_name(self, v): self.__first_name = v
    def set_last_name(self, v): self.__last_name = v
    def set_age(self, v): self.__age = v
    def set_sex(self, v): self.__sex = v
    def set_major(self, v): self.__major = v

    def __str__(self):
        return f"{self.__first_name.title()} {self.__last_name.title()} | Age: {self.__age} | Sex: {self.__sex} | Major: {self.__major}"

# -------------------------------
# Global variables
# -------------------------------
students = [
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
]
FILE = "students.txt"

def clean(text): return text.strip().lower()

def save_to_file():
    with open(FILE, "w") as f:
        for s in students:
            f.write(f"{s.get_first_name()},{s.get_last_name()},{s.get_age()},{s.get_sex()},{s.get_major()}\n")

def load_from_file():
    try:
        with open(FILE, "r") as f:
            students.clear()
            for line in f:
                fn, ln, age, sex, major = line.strip().split(",")
                students.append(Student(fn, ln, int(age), sex, major))
    except FileNotFoundError:
        pass

load_from_file()

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("🎓 Student Management System")
root.configure(bg="#e0f0ff")
root.geometry("560x600")  # Daha büyük pencere

font_btn = tkFont.Font(family="Helvetica", size=12, weight="bold")
font_input = tkFont.Font(family="Helvetica", size=12)

# -------------------------------
# GUI Functions
# -------------------------------

def add_student_gui():
    win = tk.Toplevel(root)
    win.title("➕ Add Student")
    win.configure(bg="#fff0f5")
    labels = ["First Name", "Last Name", "Age", "Sex", "Major"]
    entries = []

    def submit():
        try:
            fn = clean(entries[0].get())
            ln = clean(entries[1].get())
            age = int(entries[2].get())
            sex = entries[3].get()
            major = entries[4].get()
        except:
            messagebox.showerror("Error", "Please fill all fields correctly!")
            return
        if len(students) >= 100:
            messagebox.showwarning("Limit", "Maximum student limit reached!")
            return
        students.append(Student(fn, ln, age, sex, major))
        save_to_file()
        messagebox.showinfo("Success", f"Student {fn.title()} {ln.title()} added!")
        win.destroy()

    for i, label in enumerate(labels):
        tk.Label(win, text=label+":", font=font_input, bg="#fff0f5").grid(row=i, column=0, padx=10, pady=5)
        e = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
        e.grid(row=i, column=1, padx=10, pady=5)
        entries.append(e)

    tk.Button(win, text="Submit", command=submit, font=font_btn, bg="#80c0ff").grid(row=len(labels), columnspan=2, pady=10)

def find_student_gui():
    win = tk.Toplevel(root)
    win.title("🔍 Find Student")
    win.configure(bg="#f0fff0")
    tk.Label(win, text="First Name:", font=font_input, bg="#f0fff0").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Last Name:", font=font_input, bg="#f0fff0").grid(row=1, column=0, padx=10, pady=5)
    e_fn = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_ln = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_fn.grid(row=0, column=1, padx=10, pady=5)
    e_ln.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        fn = clean(e_fn.get())
        ln = clean(e_ln.get())
        result = ""
        for s in students:
            if s.get_first_name() == fn and s.get_last_name() == ln:
                result += str(s) + "\n"
        if not result:
            result = "Student not found!\n"
        messagebox.showinfo("Result", result)
        win.destroy()

    tk.Button(win, text="Search", command=submit, font=font_btn, bg="#80c0ff").grid(row=2, columnspan=2, pady=10)

def show_all_gui():
    win = tk.Toplevel(root)
    win.title("📋 All Students")
    win.configure(bg="#f0fff0")
    text_area = tk.Text(win, width=60, height=20, font=font_input, bg="#ffffe0")
    text_area.pack(padx=10, pady=10)
    if not students:
        text_area.insert(tk.END, "No students in system.\n")
    else:
        for s in students:
            text_area.insert(tk.END, str(s)+"\n")
    tk.Button(win, text="Close", command=win.destroy, font=font_btn, bg="#80c0ff").pack(pady=10)

def show_by_age_range_gui():
    if not students:
        messagebox.showinfo("Info", "No students in system.")
        return
    min_age = min([s.get_age() for s in students])
    max_age = max([s.get_age() for s in students])
    win = tk.Toplevel(root)
    win.title("📊 Age Range")
    win.configure(bg="#fff8dc")
    tk.Label(win, text=f"Select Age Range (System: {min_age}-{max_age})", font=font_input, bg="#fff8dc").grid(row=0, columnspan=2, padx=10, pady=5)
    tk.Label(win, text="Min Age:", font=font_input, bg="#fff8dc").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Max Age:", font=font_input, bg="#fff8dc").grid(row=2, column=0, padx=10, pady=5)
    e_min = tk.Entry(win, font=font_input, width=10, bg="#ffffe0")
    e_max = tk.Entry(win, font=font_input, width=10, bg="#ffffe0")
    e_min.grid(row=1, column=1, padx=10, pady=5)
    e_max.grid(row=2, column=1, padx=10, pady=5)

    def submit():
        try:
            min_val = int(e_min.get())
            max_val = int(e_max.get())
        except:
            messagebox.showerror("Error", "Enter valid numbers!")
            return
        result = ""
        for s in students:
            if min_val <= s.get_age() <= max_val:
                result += str(s) + "\n"
        if not result:
            result = "No students in this range!"
        messagebox.showinfo("Result", result)
        win.destroy()

    tk.Button(win, text="Show", command=submit, font=font_btn, bg="#80c0ff").grid(row=3, columnspan=2, pady=10)

def modify_student_gui():
    win = tk.Toplevel(root)
    win.title("✏️ Modify Student")
    win.configure(bg="#fff0f5")
    tk.Label(win, text="First Name of Student to Modify:", font=font_input, bg="#fff0f5").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Last Name of Student to Modify:", font=font_input, bg="#fff0f5").grid(row=1, column=0, padx=10, pady=5)
    e_fn = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_ln = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_fn.grid(row=0, column=1, padx=10, pady=5)
    e_ln.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        fn = clean(e_fn.get())
        ln = clean(e_ln.get())
        for s in students:
            if s.get_first_name() == fn and s.get_last_name() == ln:
                win2 = tk.Toplevel(win)
                win2.title("Update Field")
                win2.configure(bg="#f0fff0")
                fields = ["first_name", "last_name", "age", "sex", "major"]
                tk.Label(win2, text="Choose field to update:", font=font_input, bg="#f0fff0").pack(pady=5)
                var = tk.StringVar(win2)
                var.set(fields[0])
                tk.OptionMenu(win2, var, *fields).pack(pady=5)

                tk.Label(win2, text="New Value:", font=font_input, bg="#f0fff0").pack(pady=5)
                e_val = tk.Entry(win2, font=font_input, width=25, bg="#ffffe0")
                e_val.pack(pady=5)

                def update():
                    val = e_val.get()
                    field = var.get()
                    try:
                        if field == "first_name": s.set_first_name(clean(val))
                        elif field == "last_name": s.set_last_name(clean(val))
                        elif field == "age": s.set_age(int(val))
                        elif field == "sex": s.set_sex(val)
                        elif field == "major": s.set_major(val)
                    except:
                        messagebox.showerror("Error", "Invalid value!")
                        return
                    save_to_file()
                    messagebox.showinfo("Updated", f"{fn.title()} {ln.title()} updated!")
                    win2.destroy()
                    win.destroy()

                tk.Button(win2, text="Update", command=update, font=font_btn, bg="#80c0ff").pack(pady=10)
                return
        messagebox.showerror("Not Found", "Student not found!")
        win.destroy()

    tk.Button(win, text="Submit", command=submit, font=font_btn, bg="#80c0ff").grid(row=2, columnspan=2, pady=10)

def delete_student_gui():
    win = tk.Toplevel(root)
    win.title("🗑️ Delete Student")
    win.configure(bg="#fff8dc")
    tk.Label(win, text="First Name:", font=font_input, bg="#fff8dc").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Last Name:", font=font_input, bg="#fff8dc").grid(row=1, column=0, padx=10, pady=5)
    e_fn = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_ln = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_fn.grid(row=0, column=1, padx=10, pady=5)
    e_ln.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        fn = clean(e_fn.get())
        ln = clean(e_ln.get())
        for s in students:
            if s.get_first_name() == fn and s.get_last_name() == ln:
                students.remove(s)
                save_to_file()
                messagebox.showinfo("Deleted", f"{fn.title()} {ln.title()} deleted!")
                win.destroy()
                return
        messagebox.showerror("Not Found", "Student not found!")

    tk.Button(win, text="Delete", command=submit, font=font_btn, bg="#80c0ff").grid(row=2, columnspan=2, pady=10)

def search_student_gui():
    win = tk.Toplevel(root)
    win.title("🔎 Search by Criterion")
    win.configure(bg="#fff0f5")
    tk.Label(win, text="Search by (first_name, last_name, age, sex, major):", font=font_input, bg="#fff0f5").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Value:", font=font_input, bg="#fff0f5").grid(row=1, column=0, padx=10, pady=5)
    e_key = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_val = tk.Entry(win, font=font_input, width=25, bg="#ffffe0")
    e_key.grid(row=0, column=1, padx=10, pady=5)
    e_val.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        key = clean(e_key.get())
        val = e_val.get()
        result = ""
        for s in students:
            if key == "first_name" and s.get_first_name() == val:
                result += str(s)+"\n"
            elif key == "last_name" and s.get_last_name() == val:
                result += str(s)+"\n"
            elif key == "age":
                try:
                    if s.get_age() == int(val):
                        result += str(s)+"\n"
                except: continue
            elif key == "sex" and s.get_sex().lower() == val.lower():
                result += str(s)+"\n"
            elif key == "major" and s.get_major().lower() == val.lower():
                result += str(s)+"\n"
        if not result:
            result = "No results found!"
        messagebox.showinfo("Result", result)
        win.destroy()

    tk.Button(win, text="Search", command=submit, font=font_btn, bg="#80c0ff").grid(row=2, columnspan=2, pady=10)

# -------------------------------
# Main Menu Buttons
# -------------------------------
buttons = [
    ("➕ Add Student", add_student_gui),
    ("🔍 Find Student", find_student_gui),
    ("📋 Show All", show_all_gui),
    ("📊 Age Range", show_by_age_range_gui),
    ("✏️ Modify Student", modify_student_gui),
    ("🗑️ Delete Student", delete_student_gui),
    ("🔎 Search (Bonus)", search_student_gui),
    ("🚪 Quit", root.destroy)
]

for text, cmd in buttons:
    if "Quit" in text:
        tk.Button(root, text=text, font=font_btn, width=32, height=2, bg="#ff4d4d", fg="white", command=cmd).pack(pady=6)
    else:
        tk.Button(root, text=text, font=font_btn, width=32, height=2, bg="#80c0ff", fg="white", command=cmd).pack(pady=6)

tk.Label(root, text="Created by Kamil Efe Aşkın", font=("Helvetica", 10), bg="#e0f0ff", fg="black").pack(side="bottom", pady=5)

root.mainloop()