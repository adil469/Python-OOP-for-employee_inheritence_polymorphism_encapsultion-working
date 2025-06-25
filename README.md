# 🧑‍💼 Employee Management System - Python OOP

This is a simple Python project demonstrating core **Object-Oriented Programming (OOP)** concepts:
- Inheritance
- Encapsulation
- Polymorphism

The system includes:
- Employees (base class)
- Developers
- Designers
- Admins (who manage a team of employees)

---

## 🏗️ Project Structure

### Classes Used:

#### ✅ `Employee` (Base Class)
- Attributes: `name`, `id`, `salary`
- Method: `display_info()`

#### ✅ `Developer` (Inherits from `Employee`)
- Additional attribute: `language`
- Methods:
  - `display_info()` → Overridden
  - `is_backend_dev()` → Checks if language is Python or Java

#### ✅ `Designer` (Inherits from `Employee`)
- Additional attribute: `tool`
- Methods:
  - `display_info()` → Overridden
  - `uses_photoshop()` → Checks if the tool is Photoshop

#### ✅ `Admin` (Inherits from `Employee`)
- Manages a team (list of employees)
- Methods:
  - `add_employee()` → Adds employee to team
  - `display_team()` → Shows team info

---

## 💡 How It Works

The script:
- Creates Developer and Designer objects
- Adds them to an Admin's team
- Displays their individual and team details
- Checks backend developer and Photoshop user conditions

---


---

## 🛠️ Requirements

- Python 3.x

No external libraries required. Just run the `.py` file.

---

## 📚 Concepts Demonstrated

- **Encapsulation:** Using `_name` (protected attribute)
- **Inheritance:** All specialized roles inherit from `Employee`
- **Polymorphism:** Overriding `display_info()` method
- **Team Management:** Admin can add/display team members

---

## 📂 How to Run

1. Clone the repository or copy the code.
2. Save it as `main.py`
3. Run with Python:
   ```bash
   python main.py

