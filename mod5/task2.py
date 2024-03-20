class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        if self.gender == 'male':
            print("Hello, Mr. " + self.name)
        elif self.gender == 'female':
            print("Hello, Ms. " + self.name)
        else:
            print("Hello, " + self.name)

    def get_age_group(self):
        if self.age < 18:
            return "Child"
        elif self.age < 60:
            return "Adult"
        else:
            return "Senior Citizen"
# Пример использования
person1 = Person("Alice", 30, "female")
person2 = Person("Bob", 25, "male")
person3 = Person("Chris", 18, "male")
person4 = Person("Diana", 10, "female")
person5 = Person("Eve", 50, "female")
person6 = Person("Frank", 35, "male")
person7 = Person("Grace", 68, "female")
person8 = Person("Harry", 55, "male")
person9 = Person("Ivy", 15, "female")

person_list = [person1, person2, person3, person4, person5, person6, person7, person8, person9]

for person in person_list:
    person.greet()
    print(person.get_age_group())
    print()