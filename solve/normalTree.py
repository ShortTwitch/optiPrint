from bisect import bisect

class NormalLookup:
    
    def __init__(self, normals):
        
        self.xs = sorted(normals, key = lambda n : n.x)
        self.ys = sorted(normals, key = lambda n : n.y)
        self.zs = sorted(normals, key = lambda n : n.z)
        
    def normalsWithinRange(self, normal, radius):
        loX, hiX = normal.x - radius, normal.x + radius
        loY, hiY = normal.y - radius, normal.y + radius
        loZ, hiZ = normal.z - radius, normal.z + radius
        x_vals = [n.x for n in self.xs]
        y_vals = [n.y for n in self.ys]
        z_vals = [n.z for n in self.zs]
        
        x_range_bot = bisect(x_vals, loX) + 1
        x_range_top = bisect(x_vals, hiX) + 1
        validX = self.xs[x_range_bot : x_range_top]

        y_range_bot = bisect(y_vals, loX) + 1
        y_range_top = bisect(y_vals, hiX) + 1
        validY = self.ys[y_range_bot : y_range_top]
        
        z_range_bot = bisect(z_vals, loX) + 1
        z_range_top = bisect(z_vals, hiX) + 1
        validZ = self.zs[z_range_bot : z_range_top]
                
        return list(set(validX) & set(validY) & set(validZ))