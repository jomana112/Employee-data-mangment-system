import csv

class Employee:
    def __init__(self):
        self.__employee = {}  

    def get_info(self):
        try:
            self.__employee["name"] = input("Enter Employee's name: ").capitalize()
            self.__employee["id"] = input("Enter Employee ID: ")
            self.__employee["salary"] = float(input("Enter Employee salary: "))
            self.__employee["address"] = input("Enter Employee's address: ").capitalize()
            self.__employee["age"] = int(input("Enter Employee's age: "))
            self.__employee["department"] = input("Enter Employee's department: ").upper()
        except ValueError:
            print("Invalid input. Please enter the correct data type (e.g., numbers for salary and age).")

    def get_employee_data(self):
        return self.__employee

class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def add_employee(self):
        employee = Employee()
        employee.get_info()
        self.employee_list.append(employee.get_employee_data())
        print("Employee added successfully.")

    def display_all_employees(self):
        print("\nList of All Employees:")
        if not self.employee_list:
            print("No employees found.")
        else:
            for emp in self.employee_list:
                print("\nEmployee Information:")
                for key, value in emp.items():
                    print(f"{key.capitalize()}: {value}")  

    def update_employee(self):
        emp_id = input("Enter the Employee ID to update: ")
        employee = None
        for emp in self.employee_list:
            if emp['id'] == emp_id:
                employee = emp
                break

        if employee:
            print(f"\nEmployee found: {emp_id}")
            print("What would you like to update?")
            print("1. Name")
            print("2. Salary")
            print("3. Address")
            print("4. Age")
            print("5. Department")
            try:
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    new_name = input("Enter new name: ").capitalize()
                    employee["name"] = new_name
                elif choice == "2":
                    new_salary = float(input("Enter new salary: "))
                    employee["salary"] = new_salary
                elif choice == "3":
                    new_address = input("Enter new address: ").capitalize()
                    employee["address"] = new_address
                elif choice == "4":
                    new_age = int(input("Enter new age: "))
                    employee["age"] = new_age
                elif choice == "5":
                    new_department = input("Enter new department: ").upper()
                    employee["department"] = new_department
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid input for salary or age. Please enter valid data.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def delete_employee(self):
        emp_id = input("Enter the Employee ID to delete: ")
        employee = None
        for emp in self.employee_list:
            if emp['id'] == emp_id:
                employee = emp
                break

        if employee:
            self.employee_list.remove(employee)
            print(f"Employee with ID {emp_id} has been removed.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def save_to_csv(self):
        try:
            with open("employee_data.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "id", "salary", "address", "age", "department"])
                writer.writeheader()
                for emp in self.employee_list:
                    writer.writerow(emp)
            print("Employee data has been saved to 'employee_data.csv'.")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. Display All Employees")
            print("5. Save Data to CSV")
            print("6. Exit")

            try:
                choice = int(input("Please enter your choice: "))

                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.update_employee()
                elif choice == 3:
                    self.delete_employee()
                elif choice == 4:
                    self.display_all_employees()
                elif choice == 5:
                    self.save_to_csv()
                elif choice == 6:
                    print("Exiting the system.")
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

manager = EmployeeManager()
manager.menu()

