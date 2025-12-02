class Student:
    school_name="GreenWood High School"# Class Variable
    # Constructor
    def __init__(self,name,marks):# Init is a constructor
        self.name=name
        self.marks=marks
    # Instance Method
    def average(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        return avg
    # Instance Method(Comparing Objects)
    def compare(self,other):
        if self.average()==other.average():
            return True
        else:
            return False
        # Class Method---
    @classmethod
    def change_school(cls,name):
        cls.school_name=name
    #Static Method
    @staticmethod
    def is_pass(mark):
        return mark>=35

# -------------MAIN PROGRAM#
s1=Student("Rahul",[80,70,90])
s2=Student("Anita",[80,70,90])
s3=Student("Rohit",[30,40,20])
print("Rahul Average :",s1.average())
print("Anita Average:",s2.average())
#Comparing Objects
if s1.compare(s2):
    print("Rahul and Anita have the same average")
else:
    print("Rahul and Anita have different average")
# Class Method Usage
Student.change_school("Delhi Public School")
print("School Name:",Student.school_name)
# Static Method Change:
print("Did Rohit pass  in Subject 1? ",Student.is_pass(s1.marks) )



