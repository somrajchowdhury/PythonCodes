class Student(object):
    
    """
    Returns a ```Student``` object with the given name and branch.
    """
    def __init__(self, name, branch):
            self.name = name
            self.branch = branch
            print("A student object is created.")

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)

stu1 = Student('Som','CSE')
print(stu1.print_details())

