
class Vertex(object):
    
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)
    
        
class Face(object):
    
    def __init__(self, v1, v2, v3, color=None):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.color = color
        
    def __str__(self):
        return "({},{},{})".format(self.v1, self.v2, self.v3)
        
