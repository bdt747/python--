class TimeEmployee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
        return 
class QEmployee(TimeEmployee):
    def __init__(self,name,employee_id,monthly_salary):
        super().__init__(name,employee_id)
        self.monthly_salary = monthly_salary
        return
class HEmployee(TimeEmployee):
    def __init__(self,name,employee_id,hourly_wage):
        super().__init__(name,employee_id)
        self.hourly_wage = hourly_wage
        return
time_employee1 = TimeEmployee("Alice", "E12345")
q_employee1 = QEmployee("Bob", "E67890", 5000)
h_employee1 = HEmployee("Charlie", "E11111", 20)