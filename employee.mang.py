class Employee():
  def __init__(self, name, id, salary:int):
    self._name = name.title() # Encapsulation (protected attribute)
    self.id = id
    self.salary = salary

  def display_info(self):
    print(f'Name: {self._name} \nID: {self.id} \nSalary: {self.salary}')

class Developer(Employee):  # Inheritance(get data from parent or base class)
  def __init__(self, name, id, salary, language):
    super().__init__(name, id, salary)
    self.language = language.title()

  def display_info(self): # polymorphism (Method overriding)
    super().display_info()
    print(f'Prog language: {self.language}')

  def is_backend_dev(self):
    return self.language in["Python" , 'Java']


class Designer(Employee): # Inheritance(get data from parent or base class)
  def __init__(self, name, id, salary, tool):
    super().__init__(name, id, salary)
    self.tool = tool.title()

  def display_info(self): # polymorphism (Method overriding)
    super().display_info()
    print(f'Design tool: {self.tool}')

  def uses_photoshop(self): 
    return self.tool == "Photoshop"

class Admin(Employee): # Inheritance(get data from parent or base class)
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)
        self.team = []  # List to hold other employees

    def add_employee(self, employee):
        self.team.append(employee) # append() a builten function of list to add

    def display_team(self): # polymorphism (method overriding)
        print(f"\nAdmin: {self._name}'s Team:")
        for emp in self.team:
            print("----")
            emp.display_info()
     
dev1 = Developer('adil',654123,50000,'python')
print('\nDeveloper info: ')
dev1.display_info()
print('is Developer:', "Yes" if dev1.is_backend_dev() else "No")

des1 = Designer('sana',654741,55000,'figma')
print('\nDesigner info: ')
des1.display_info()
print('is Designer: ',"Yes" if des1.uses_photoshop() else "No")

admin = Admin("ali", 100, 100000)
admin.add_employee(dev1)
admin.add_employee(des1)
admin.display_team()

 # Results
# Developer info: 
# Name: Adil 
# ID: 654123 
# Salary: 50000
# Prog language: Python
# is Developer: Yes

# Designer info: 
# Name: Sana 
# ID: 654741 
# Salary: 55000
# Design tool: Figma
# is Designer:  No

# Admin: Ali's Team:
# ----
# Name: Adil 
# ID: 654123 
# Salary: 50000
# Prog language: Python
# ----
# Name: Sana 
# ID: 654741 
# Salary: 55000
# Design tool: Figma