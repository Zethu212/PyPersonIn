
class Person:
    def __init__(self):
        self.__firstname = ''
        self.__surname = ''
        self.__idnumber = ''
        self.__birthdate = ''
    def setfirstname(self, firstname):
        self.__firstname = firstname

    def getfirstname(self):
        return self.__firstname

    def setsurname(self, surname):
        self.__lastname = surname

    def getsurname(self):
        return self.__surname

    def setidnumber(self, idnumber):
        self.__idnumber = idnumber

    def getidnumber(self):
        return self.__idnumber

    def setbirthdate(self, birthdate):
        self.__birthdate = birthdate

    def getbirthdate(self):
        return self.__birthdate

    firstname = property(getfirstname, setfirstname)
    lastname = property(getsurname, setsurname)
    idnumber = property(getidnumber, setidnumber)
    birthdate = property(getbirthdate, setbirthdate)

    def reportLines(self):
        text = "First name : " + self.firstname
        text = text + "\n" + "Surname : " + self.surname
        text = text + "\n" + "ID number : " + self.idnumber
        text = text + "\n" + "Birth date: " + self.birthdate
        return text

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.__studentno = ''
        self.__internalmark = 0
        self.__externalmark = 0

    def setstudentno(self, studentno):
        self.__studentno = studentno

    def getstudentno(self):
        return self.__studentno

    def setinternalmark(self, internalmark):
        self.__internalmark = internalmark

    def getinternalmark(self):
        return self.__internalmark

    def setexternalmark(self, externalmark):
        self.__externalmark = externalmark

    def getexternalmark(self):
        return self.__externalmark

    studentno = property(getstudentno, setstudentno)
    internalmark = property(getinternalmark, setinternalmark)
    externalmark = property(getexternalmark, setexternalmark)

    def fmark(self):
        return (self.internalmark + self.externalmark) / 2

    def reportLines(self):
        text = "Report of PhD Student"
        text = text + "\n" + Person.reportLines(self)
        text = text + "\n" + "student number : " + self.studentno
        text = text + "\n" + "internal mark : " + str(self.internalmark)
        text = text + "\n" + "external mark : " + str(self.externalmark)
        text = text + "\n" + "Final mark is : " + str(self.fmark)
        return text

class Examiner(Person):
    def __init__(self):
        Person.__init__(self)
        self.__staffno = ''
        self.__hourrate = 0
        self.__hours = 0

    def setstaffno(self, studentno):
        self.__staffno = studentno

    def getstaffno(self):
        return self.__staffno

    def sethourrate(self, hourrate):
        self.__hourrate = hourrate

    def gethourrate(self):
        return self.__hourrate

    def sethours(self, hours):
        self.__hours = hours

    def gethours(self):
        return self.__hours

    staffno = property(getstaffno, setstaffno)
    hourrate = property(gethourrate, sethourrate)
    hours = property(gethours, sethours)

    def Salary(self):
        return self.hourrate * self.hours

    def reportLines(self):
        text = "Report of PhD Examiner"
        text = text + "\n" + Person.reportLines(self)
        text = text + "\n" + "staff number : " + self.staffno
        text = text + "\n" + "rate per hour : " + str(self.hourrate)
        text = text + "\n" + "number of hours : " + str(self.hours)
        text = text + "\n" + "Salary: " + str(self.Salary)
        return text

