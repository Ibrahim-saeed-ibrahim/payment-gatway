class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def calculate_area(self):

        return(self.length*self.width)

    def calculate_perimeter(self):
        return(2*(self.length+self.width))

    def is_square(self):
        if self.length == self.width:
            print("is square")

    def scale_rectangle(self, scale_factor):
        
        self.length *= scale_factor
        self.width *= scale_factor
        print(self.length , self.width)
    
    def __add__(self, other):
         return Rectangle (self.length+other.length , self.width + other.width)
        

    
    def __sub__(self, other):
        return Rectangle (self.length-other.length , self.width - other.width)
    
    def __eq__(self, other):
        return Rectangle (self.length==other.length and self.width == other.width)
    
    def __ne__(self, other):
        return Rectangle (self.length!=other.length and self.width != other.width)
    
    def __str__(self):
        print( f"length equal={self.length},width= {self.width}")

          

r1=Rectangle(10,20)          