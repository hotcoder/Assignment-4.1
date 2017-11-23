'''
Created on Nov 21, 2017

@author: z002krv
'''
class ParentClass(object):
         
    def input_sides_of_triangle(self):
                self.a = input("Provide the value for first side of triangle a  : ")
                self.b = input("Provide the value for second side of triangle b : ")
                self.c = input("Provide the value for third side of triangle c  : ")
            

class ChildClass(ParentClass):
    
    def calculateAreaOfTraingle(self):
        try:
            ParentClass.input_sides_of_triangle(self)
            s = (self.a + self.b + self.c)/2
            area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
            print("Area of the triangle is :{0}".format(area))
        except:
            print("Please provide valid numbers only for a , b and c")
        
        
c = ChildClass()
c.calculateAreaOfTraingle()