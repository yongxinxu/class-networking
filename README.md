# class-networking

Here is the outline of this project:
```
class Student: # has Lastname, Firstname, and FavoriteColor
	X.Roster(CN)  # given a student, what courses are they taking
	X.Shared(CN, Y)  # given two students, what courses are they sharing

class Roster:  #Roster of courses for a given student
	R.add_course(course) # add a course to the roster of a given student
	R.__len__() # the length of the given roster

class SRoster: #Roster of students for a given course
	SR.add_people(student) # add a new student to the roster of a given course
	SR.__len__() # the length of the given roster

class ClassNetwork:
	CN.put(Student, course) # extend CN
	CN.slookup(student) # lookup a student in the network, return Roster()
	CN.clookup(course) # #lookup a course in the network, return SRoster()
	CN.graph(classlist) # to import ClassList

	CN.StudentCount(course) # how many students in a given course
	CN.CourseCount(course) # how many course are taken by students in a given course
	CN.Popular() # the most popular course (take the most recent one)
	CN.Second() # the second popular course (take the most recent one)
	CN.CourseColor() # the most popular color in a given course (take the most recent one)
```
