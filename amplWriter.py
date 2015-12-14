import argparse
import readers.ClassFormat as CF
import readers.amfReader as AMFReader
import readers.stlReader as STLReader

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

if args.amf:
    faces, normals = AMFReader.read_amf(args.filename)
    if faces and normals:
        write_ampl(args.filename, normals)
elif args.stl:
    faces, normals = STLReader.read_stl(args.filename)
    if faces and normals:
        write_ampl(args.filename, normals)
else:
    print("No file type specified in command flags")
