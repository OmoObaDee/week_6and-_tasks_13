# coding along on examples of class
class student:
    def _init_(self, name, course, level):
        print("creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")