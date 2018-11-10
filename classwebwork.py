class Student:
    def __init__(self, ln, fn, color):
        assert(type(ln) == type(fn) == type(color) == type('a string'))
        self.Lastname = ln
        self.Firstname = fn
        self.FavoriteColor = color
    
    def Roster(self, CN):
        assert(type(CN) == type(ClassNetwork()))
        if CN.slookup(self) == "No entry":
            return Roster()
        return CN.slookup(self)


    def Shared(self, CN, otherstudent):
        assert(isinstance(CN, ClassNetwork) and isinstance(otherstudent, Student))
        share = []
        for self_each in self.Roster(CN).Courses:
            for other_each in otherstudent.Roster(CN).Courses:
                if self_each == other_each:                    
                    share += [self_each]
        return share

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.Lastname == other.Lastname and self.Firstname == other.Firstname and self.FavoriteColor == self.FavoriteColor
        else:
            return False
    
    def __repr__(self):
        return "(" + repr(self.Lastname) + ", " + repr(self.Firstname) + ", " + repr(self.FavoriteColor) + ")"


class Roster: #Roster of courses for a given student
    def __init__(self):
        self.Courses = []

    def add_course(self, course):
        self.Courses += [course]
        return self

    def __len__(self):
        return len(self.Courses)

    def __repr__(self):
        return str(self.Courses)


class SRoster: #Roster of students for a given course
    def __init__(self):
        self.Students = []

    def add_people(self, student):
        self.Students += [student]
        return self

    def __len__(self):
        return len(self.Students)

    def __repr__(self):
        return str(self.Students)
        
class ClassNetwork:
    def __init__(self):
        self.__listOfPairs = []

    def put(self, person, course): #extending CN
        assert(type(person) == type(Student("","","")) and type(course) == type("a string"))
        if self.slookup(person) == "No entry": #student not in network
            temp = Roster()
            self.__listOfPairs = [ (person, temp.add_course(course)) ] + self.__listOfPairs
        else: #the student is in the network
            for index in range(len(self.__listOfPairs)):        
                if self.__listOfPairs[index][0] == person:
                    self.__listOfPairs[index][1].add_course(course)   

        if self.clookup(course) == "No entry": #course not in network
            temp = SRoster()
            self.__listOfPairs = [ (course, temp.add_people(person)) ] + self.__listOfPairs
        else: #the course is in the network
            for index in range(len(self.__listOfPairs)):
                if self.__listOfPairs[index][0] == course:
                     self.__listOfPairs[index][1].add_people(person)

    
    def slookup(self, student): #lookup a student in the network, return Roster()
        assert(isinstance(student, Student))
        for pair in self.__listOfPairs:
            if pair[0] == student:
                return pair[1] 
        return "No entry"


    def clookup(self, course): #lookup a course in the network, return SRoster()
        assert(not isinstance(course,Student))
        for pair in self.__listOfPairs:
            if (not isinstance(pair[0], Student)) and pair[0] == course:
                return pair[1]
        return "No entry"

   
    def graph(self, classlist): #to import ClassList
        assert(type(classlist) == type([]))
        for [ln, fn, course, color] in classlist[1:]:
            self.put(Student(ln, fn, color), course) #build the Student type object

       
    def StudentCount(self, course):
        assert(not isinstance(course,Student))
        if self.clookup(course) != 'No entry':
            return len(self.clookup(course))
        else:
            return 'No entry'


    def CourseCount(self, course):
        assert(not isinstance(course,Student))
        answer = 0
        if self.clookup(course) != 'No entry':
            for student in self.clookup(course).Students:
                answer += len(self.slookup(student))
            return answer
        else:
            return 'No entry'

            
    def Popular(self):
        popcount = 0
        popcourse = ""                    
        for pair in self.__listOfPairs:
            if not isinstance(pair[0], Student):
                if self.StudentCount(pair[0]) >= popcount: #take the most recent popular course
                     popcount = self.StudentCount(pair[0])
                     popcourse = str(pair[0])
        return popcourse


    def Second(self):
        popcount = 0
        popcourse = ""
        lesscount = 0
        lesspopcourse = ""                   
        for pair in self.__listOfPairs:
            if not isinstance(pair[0], Student):
                if self.StudentCount(pair[0]) >= popcount:
                    lesspopcourse = popcourse #take the most recent second popular course
                    lesscount = popcount
                    popcount = self.StudentCount(pair[0])
                    popcourse = str(pair[0])
                if lesscount <= self.StudentCount(pair[0]) < popcount:
                    lesspopcount = self.StudentCount(pair[0])
                    lesscourse = str(pair[0])
        return lesspopcourse


    def CourseColor(self, course):
        assert(not isinstance(course,Student))
        colors = []
        if self.clookup(course) != "No entry":            
            for student in self.clookup(course).Students:
                colors += [student.FavoriteColor] #get a list of colors in the given course
           
        popcount = 0
        popcolor = ""
        for each in colors:
            each_count = count(each, colors)
            if each_count >= popcount: #pick the most recent one when they have the same popcount
                popcount = each_count
                popcolor = each
                
        return popcolor


    def __repr__(self):
        answer = ''
        for pair in self.__listOfPairs:
            answer += str(pair) + '\n'
        return answer


def count(any_color, list_of_colors):
    assert(type(list_of_colors) == type([]))
    count = 0
    for each in list_of_colors:
        if any_color == each:
            count += 1
    return count
            



    
