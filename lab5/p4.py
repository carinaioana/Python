# Build an employee hierarchy with a base class Employee.
# Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
# Each subclass should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name {self.name}, Salary {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manage_team(self):
        return f"{self.name} is managing the team."


class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."


class Salesperson(Employee):
    def __init__(self, name, salary, sales_target):
        super().__init__(name, salary)
        self.sales_target = sales_target

    def meet_sales_target(self):
        return f"{self.name} is working to meet the sales target of {self.sales_target}."


def main():
    manager = Manager("John Doe", 80000, "Marketing")
    engineer = Engineer("Jane Smith", 70000, "Python")
    salesperson = Salesperson("Bob Johnson", 60000, 100000)

    print(manager.display_info())
    print(manager.manage_team())

    print(engineer.display_info())
    print(engineer.write_code())

    print(salesperson.display_info())
    print(salesperson.meet_sales_target())


if __name__ == "__main__":
    main()
