from math import *

class Vertex(object):
    
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)
    
    def __sub__(self, other):
        
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vertex(x, y, z)
              
    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return sqrt(dx**2 + dy**2 + dz**2)
                
class Face(object):
    
    def __init__(self, v1, v2, v3, color=None, normal=None):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.color = color
        self.normal = normal
        
    def __str__(self):
        return "({},{},{})".format(self.v1, self.v2, self.v3)        
    
    def area(self):
        d1 = self.v1.distance_from(self.v2)
        d2 = self.v1.distance_from(self.v3)
        d3 = self.v2.distance_from(self.v3)
        s = (d1 + d2 + d3) / 2
        area = sqrt(s * (s-d1) * (s-d2) * (s-d3))
        return area
    
class Normal(object):
    
    def __init__(self, x, y, z, area):
        length = sqrt(x**2 + y**2 + z**2)
        
        self.x = x / length
        self.y = y / length
        self.z = z / length
        self.area = area
        
    def __str__(self):
        return "({},{},{}). Area : {}".format(self.x, self.y, self.z, self.area)
        