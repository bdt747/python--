class CuteCat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return 
    def meow(self):    
        return "Meow!"
cat1 = CuteCat("Tom", 3)
print(f"{cat1.name} is {cat1.age} years old.")
print(cat1.meow())

class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        return print(1112223333)
    def set_age(self, new_age):
        self.age = new_age
student1 = Student("Alice", "S12345", 20)
student2 = Student("Bob", "S67890", 22)
print(f"{student1.name} is {student1.age} years old and has student ID {student1.student_id}.")
print(f"{student2.name} is {student2.age} years old and has student ID {student2.student_id}.")
student1.set_age(21)
print(f"After updating age, {student1.name} is now {student1.age} years old.")