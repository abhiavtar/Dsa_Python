class Student:
	def __init__(self, name, roll,marks):
		self.rollno=roll
		self.name=name
		self.marks=marks
	def showdata(self):
		print(self.name)
		print(self.rollno)
	def showmarks(self):
		print(self.marks)
name=input("Enter the name of student:")
roll=int(input("Enter the roll number of student:"))
marks=(list(map(int,(input("Enter marks:")).split())))
s1=Student(name,roll, marks)
s1.showdata()
s1.showmarks()
