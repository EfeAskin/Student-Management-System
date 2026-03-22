# 🎓 Student Management System

## 🚀 Project Overview
The **Student Management System** is a Python program to manage student records efficiently.  
It now comes with a **Tkinter GUI** for a more interactive experience, in addition to the original **console-based menu**.  

Users can **add, find, show, modify, delete, and search students**, with persistent storage in a text file (`students.txt`) to save data across sessions.  

This project demonstrates **Python object-oriented programming**, **file handling**, **menu-driven console apps**, and **basic GUI development with Tkinter**. Perfect for learning CRUD operations and building a practical portfolio project.  

---

## 📌 Features

* 🆕 Add new students  
* 🔍 Find students by first and last name  
* 📋 Show all students  
* 📊 Filter students by age range  
* ✏️ Modify student information  
* ❌ Delete student records  
* 🔎 Search by any criterion (first name, last name, age, sex, major)  
* 💾 Persistent storage using `students.txt`  
* 🖥 **GUI Interface** – Interactive buttons, pop-up forms, and message dialogs  

---

## 🛠 Technologies Used

* **Python 3**  
* **Tkinter** for GUI  
* File handling for persistent data storage  

---

## 🗄 File Structure
Student-Management-System/
│
├── student-management-system.py # Console version
├── stumansystgui.py # Tkinter GUI version
├── students.txt # Persistent student data
└── README.md # Documentation

| File                        | Purpose                                                                 |
| --------------------------- | ----------------------------------------------------------------------- |
| student-management-system.py | Original console program with `Student` class and menu-driven CRUD operations |
| stumansystgui.py             | Tkinter GUI version with interactive forms, buttons, and pop-up messages |
| students.txt                 | Stores student records in CSV format (`first_name,last_name,age,sex,major`) |
| README.md                    | Documentation and usage guide                                           |

---

## 🖥 Example Usage

**Menu (Console):**
Welcome to Student Management System
--- MENU ---
1 Add
2 Find
3 Show All
4 Age Range
5 Modify
6 Delete
7 Search (Bonus)
0 Quit
Choice:

**Sample Output (Show All Students):**
Ali Yilmaz | Age: 20 | Sex: M | Major: CS
Ayşe Demir | Age: 21 | Sex: F | Major: Math
Mehmet Kaya | Age: 22 | Sex: M | Major: Physics
Zeynep Aydin | Age: 19 | Sex: F | Major: Biology
Can Çelik | Age: 23 | Sex: M | Major: CS

**GUI Version:**
* Menu buttons for all operations  
* Pop-up forms for **First Name, Last Name, Age, Sex, Major**  
* Colored buttons and interactive dialogs  
* Quit button highlighted in **red**  

---

## 🌟 Future Improvements

* 🌐 **Web Interface** – Browser-based student management with Python backend and HTML/CSS frontend  
* 💾 **Database Integration** – Replace `students.txt` with SQLite or another database for faster queries and scalability  
* 🎨 **GUI Enhancements** – Tables, better layout, more colors, and usability improvements  

---

## 👨‍💻 Author

**Kamil Efe Aşkın**  
Computer Engineering Student  
Eastern Mediterranean University  

---

> “Çalışmadan, yorulmadan, öğrenmeden rahat yaşamak isteyenler; ne toplum içinde, ne de kendi hayatında başarılı olabilirler.”  
> — Mustafa Kemal Atatürk
