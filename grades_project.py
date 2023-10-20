#We define a class named Student that will be our data model at School of Athens.
#We add a constructor for Student taking in two parameters: a name and a year.
#We declare self.grades as an empty list. This list will contain students' grades.
#We declare self.attendance, this will be a dictionary, containing students' school attendance.
#We add an .add_grade() method to Student that takes one parameter, grade.
# .add_grade() should verify that grade is of type Grade and if so, we add it to the Student‘s .grades.
#We modify the Student class to include the attendance dictionary-self.attendance- as an instance variable.

class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

#we declare a Student method .get_average() in Grade, that returns the student’s average score.
  def get_average(self):
   return sum(grade.score for grade in self.grades)/len(self.grades)

#The mark_attendance method allows us to add entries to this dictionary, 
# where the keys are dates and the values are boolean values indicating 
# whether the student attended school on those dates.
  def mark_attendance(self,date, attended=True):
    self.attendance[date] = attended

#We create a Grade class, with .minimum_passing as an attribute set to 65
#We give Grade a constructor. Take in a parameter score 
#We declare a Grade method .is_passing() that returns whether a Grade has a passing .score
class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    if self.score >= self.minimum_passing:
      return "is passing with a Grade of {score} ".format(score=self.score)
    else:
      return "unfortunately doesn't pass the exams"

#example
#grade_of_90=Grade(90)
#print(grade_of_90.is_passing())

#We create three instances of the Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#ADD GRADES USING .add_grade
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(70))
sandro.add_grade(Grade(35))
sandro.add_grade(Grade(75))


#ADD ATTENDANCE USING .mark_attendance
pieter.mark_attendance('2023-09-10', True)
pieter.mark_attendance('2023-09-11', False)
pieter.mark_attendance('2023-09-12', True)
pieter.mark_attendance('2023-09-13', False)
sandro.mark_attendance('2023-10-10', False)
sandro.mark_attendance('2023-10-11', True)
sandro.mark_attendance('2023-10-12', False)
sandro.mark_attendance('2023-10-13', True)
print("\nThe attendance of {name} is the following:".format(name=pieter.name),pieter.attendance, "\n")
print("The attendance of {name} is the following:".format(name=sandro.name),sandro.attendance, "\n")

#GET AVERAGE GRADES
pieter_avg = pieter.get_average()
sandro_avg = sandro.get_average()

print("\nThe avegare grade of {name} is {average}".format(name=pieter.name, average = pieter_avg))
print("The avegare grade of {name} is {average}".format(name=sandro.name, average = sandro_avg))

#IS PASSING
print("\n"+pieter.name, Grade(pieter_avg).is_passing())
print(sandro.name, Grade(sandro_avg).is_passing(),"\n")