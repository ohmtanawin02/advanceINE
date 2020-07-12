class grade:
    def __init__(self, name, sub1,sub2,sub3,sub4,sub5):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.grades_list = [self.sub1,self.sub2,self.sub3,self.sub4]
        self.gpa_list= []
        self.gpa = 0
    
    def convert(self):
        for i in self.grades_list:
            if i == 'A':
                self.gpa_list.append(4)
            elif i == 'B+' :
                self.gpa_list.append(3.5)
            elif i == 'B' :
                self.gpa_list.append(3)
            elif i == 'C+' :
                self.gpa_list.append(2.5)
            elif i == 'C' :
                self.gpa_list.append(2)
            elif i == 'D+' :
                self.gpa_list.append(1.5)
            elif i == 'D' :
                self.gpa_list.append(1)
            elif i == 'F' :
                self.gpa_list.append(0)
        self.gpa = ((self.gpa_list[0] * self.sub1) + (self.gpa_list[1] * self.sub2) + (self.gpa_list[2] * self.sub3) + (self.gpa_list[3] * self.sub4))/(self.sub1 + self.sub2 + self.sub3 + self.sub4)

    def __str__(self):
        return 'Name : {} , GPA : {}'.format(self.name,self.convert)

name = grade('Tanawin Jenkunnaphat',2.5,3,3,2,['C+','B','B','C'])
print(name)