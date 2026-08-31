"""
You are tasked with developing a system to manage a school's enrollment.
The system should allow for adding students to a course,
  calculating the average grade of the students,
  and determining the total number of students enrolled.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

course = Course("Math 101")
course.add_student(Student("Alice", 85))
course.add_student(Student("Bob", 92))

print(course.get_average_grade())  # Prints 88.5
print(course.get_total_students())  # Prints 2


Once your classes are complete, copy and paste the above example below them in order to test their functionality.
"""

"""
Write a class that meets these requirements.

Name:       Course

Required state:
   * course name, the name of the course

Behavior:
   * add_student(student)     # Add a Student to the Course
   * get_average_grade()      # Returns the average grade of all students in the course
   * get_total_students()     # Returns the total number of students enrolled in the course

"""
class Course:

   def __init__(self, course_name):
      self.course_name = course_name
      self.students = []

   def add_student(self, student):
      self.students.append(student)

   def get_average_grade(self):
      grade_total = 0

      for student in self.students:
         grade_total += student.get_grade()

      return grade_total / len(self.students)

   def get_total_students(self):
      return len(self.students)
"""
Write a class that meets these requirements.

Name:       Student

Required state:
   * name, the name of the student
   * grade, the grade of the student

Behavior:
   * get_grade()          # Returns the grade of the student

Example:
   student = Student("Alice", 85)

   print(student.get_grade())    # Prints 85

"""
class Student:
   def __init__(self, name, grade):
      self.name = name
      self.grade = grade

   def get_grade(self):
      return self.grade

course = Course("Math 101")
course.add_student(Student("Alice", 85))
course.add_student(Student("Bob", 92))

print(course.get_average_grade())  # Prints 88.5
print(course.get_total_students())  # Prints 2