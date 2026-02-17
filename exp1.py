class Student: #created a class
    def __init__(self, name, student_id, grades): #constructor 
        self.name = name #self refers to current object
        self.student_id = student_id
        self.grades = grades      # dictionary: subject -> grade points
        self.next = None          # for linked list # refers to next node 

    def calculate_gpa(self): #a method to calculate gpa
        if not self.grades: # to check if the dict is empty
            return 0.0 #if yes 
        total_points = sum(self.grades.values()) #if no #values() exyracted from dict , sum () adds them
        return round(total_points / len(self.grades), 2) #divide points by grade , round gpa to 2 decimal point


class StudentList: # a class that will managr student_linked list
    def __init__(self): #runs the studentll is created
        self.head = None #head points to first 

    def add_student(self, name, student_id, grades): #to add details of student
        new_student = Student(name, student_id, grades) #add new obj
        new_student.next = self.head #points to next student to the current 1st student
        self.head = new_student #makes new student the head

    def display_students(self):#to display all students 
        if not self.head: #checks if the dict / list is empty
            print("No students in the list.") #if yes
            return

        current = self.head #traverse from head
        while current: #loop until end of list
            print(
                f"Name: {current.name}, "
                f"ID: {current.student_id}, "
                f"GPA: {current.calculate_gpa()}" #print student detail
            )
            current = current.next #moves to next student

    def calculate_average_gpa(self): #calculate gpa fpr the entire class
        if not self.head: #check idf the list is empty
            return 0.0 #if yes

        total_gpa = 0.0 #if no
        total_students = 0
        current = self.head #traverse from 1st student

        while current: #loop
            total_gpa += current.calculate_gpa() #to add gpa of each student
            total_students += 1 #counts students
            current = current.next #moves to next student

        return round(total_gpa / total_students, 2) #converting gpa to grade

    def get_gpa_grade(self):
        average_gpa = self.calculate_average_gpa()

        if average_gpa >= 3.7:
            return 'A'
        elif 3.0 <= average_gpa < 3.7:
            return 'B'
        elif 2.0 <= average_gpa < 3.0:
            return 'C'
        elif 1.0 <= average_gpa < 2.0:
            return 'D'
        else:
            return 'F'


# Example Usage
if __name__ == "__main__": # ensures the code runs when the file is executed 
    student_list = StudentList()

    # Add students details to dictonary
    student_list.add_student(
        "Alice", "A001",
        {"Math": 3.5, "Science": 3.8, "English": 3.7}
    )
    student_list.add_student(
        "Bob", "A002",
        {"Math": 3.9, "Science": 4.0, "English": 3.7}
    )
    student_list.add_student(
        "Charlie", "A003",
        {"Math": 2.5, "Science": 2.8, "English": 2.7}
    )

    print("List of Students:")
    student_list.display_students()

    gpa_grade = student_list.get_gpa_grade()
    print(f"\nOverall Class GPA Grade: {gpa_grade}")
