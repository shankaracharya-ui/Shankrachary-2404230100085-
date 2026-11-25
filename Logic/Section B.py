# (Section - B (Python))

# ANSWER - 11
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s = Student("Shankracharya", 89)
s.display()

# ANSWER - 12
try:
    f = open("students.txt", "r")
    data = f.read()
    print("Lines:", len(data.splitlines()))
    print("Words:", len(data.split()))
except FileNotFoundError:
    print("File not found")