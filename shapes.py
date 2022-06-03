class Circle:
    def __init__(self,radius) :
        self.radius = radius


    def areaof_circle(self) :
     pie=3.14
     total_radius=self.radius*self.radius 
     area=pie*total_radius
     return area 



    def circumference(self):
        pie=2*3.14
        radius=self.radius*self.radius
        circum=pie*radius
        return circum

class Square:    
    def __init__(self,side) :
        self.side=side

    def areaof_square(self)  :
        area=self.side*self.side  
        return area
        
    def perimeter(self) :
        perimeter=4*self.side 
        return perimeter

class Rectangle:
    def __init__(self,length,width) :
        self.length=length
        self.width=width

    def areaof_rectangle(self)  :
        area=self.width*self.length
        return area  

    def perimeter(self):
        total_sides=self.length + self.width
        perimeter=2*total_sides
        return perimeter

class Sphere:
    def __init__(self,radius) :
        self.radius=radius

    def areaof_sphere(self) :
        pie=3.14
        total_radius=self.radius * self.radius   
        area=4*pie*total_radius
        return area       

    def volume(self):
        pie=3.14
        radius=self.radius * self.radius * self.radius
        area=4/3 *pie *radius
        return area   