
def write_ampl(normals):
    
    with open('sample.ampl', 'w') as f:
        for i, n in enumerate(normals):
            line = "{} {} {} {} {}\n".format(i+1, n.x, n.y, n.z, n.area)
            f.write(line)
