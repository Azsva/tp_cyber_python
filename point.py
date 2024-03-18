class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
              
              #decorateur transforme la methode x en get_x
              #et l'attribut x devient des lors prives
    @property  
    def x(self):
         return self._x  

    @x.setter
    def x(self, x):
        self._x = x 
        
    
    
#main
p1 = Point(23.4, 24.2)
print(f"x={p1.x}, y={p1.y}")    