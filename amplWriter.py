import argparse
import readers.ClassFormat as CF
import readers.amfReader as AMFReader
import readers.stlReader as STLReader
from math import atan, sqrt, pi

OPTIPRINT_DESC = "Simple File Converter Functionality"

parser = argparse.ArgumentParser(description = OPTIPRINT_DESC)

input_file_type = parser.add_mutually_exclusive_group()
input_file_type.add_argument("--amf", action="store_true", help = "Parse file as .amf format")
input_file_type.add_argument("--stl", action="store_true", help = "Parse file as .stl format")

parser.add_argument('filename', metavar = 'FILE', help = "File to be read in")

args = parser.parse_args()

def write_ampl(filename, normals):
    filename = "out/" + filename + ".ampl"
    with open(filename, 'w') as f:
        f.write("param: normalX normalY normalZ area:=\n")
        for i, n in enumerate(normals):
            line = "{} {} {} {} {}\n".format(i+1, n.x, n.y, n.z, n.area)
            f.write(line)
        f.write("\nparam coneOfShameWindow := 0.707")

def normal_to_polarNorm(normal):
    x,y,z = normal.x, normal.y, normal.z
    phi = atan((sqrt(x^2+y^2))/z)
    theta = atan(y/x)
    if phi < pi/4 or theta < pi/4:
        phi = phi+2*pi
        theta = theta+2*pi
    if phi> 2*pi - pi/4 or theta > 2*pi - pi/4:
        phi = phi-2*pi
        theta = theta-2*pi
    return CF.PolarNorm(phi, theta, normal.area)

def cartesian_to_polar_writer(filename, normals):
    filename = "out/" + filename + ".ampl"
    polarNorms = [convert_to_polarNorm(n) for n in normals]
    with open(filename, 'w') as f:
        f.write("param: thetaFace phiFace area:=\n")
        for i, n in enumerate(polarNorms):
            line = "{} {} {} {}\n".format(i+1, n.theta, n.phi, n.area)
            f.write(line)
        f.write("\nparam coneOfShameWindow := 0.785398")

if args.amf:
    print args.filename
    faces, normals = AMFReader.read_amf(args.filename)
    if faces and normals:
        cartesian_to_polar_writer(args.filename, normals)
elif args.stl:
    faces, normals = STLReader.read_stl(args.filename)
    if faces and normals:
        cartesian_to_polar_writer(args.filename, normals)
else:
    print("No file type specified in command flags")
