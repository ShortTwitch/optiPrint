import argparse
import readers.ClassFormat as CF
import readers.amfReader as AMFReader
import readers.stlReader as STLReader
import solve.circleMesh as CM

OPTIPRINT_DESC = "Determine optimum orientation of 3D-printed object"

parser = argparse.ArgumentParser(description = OPTIPRINT_DESC)

file_group = parser.add_mutually_exclusive_group()
file_group.add_argument("--amf", action="store_true", help = "Parse file as .amf format")
file_group.add_argument("--stl", action="store_true", help = "Parse file as .stl format")

parser.add_argument('filename', metavar = 'FILE', help = "File to be read in")

parser.add_argument("-g","--graph", action="store_true", help = "Graph the normal sphere")

args = parser.parse_args()

if args.amf:
    vertices = AMFReader.read_amf(args.filename)
    CM.convexHullTest(vertices)
    #faces, normals = AMFReader.read_amf(args.filename)
    #if faces and normals:
    #    CM.separate_norms(normals)
elif args.stl:
    faces, normals = STLReader.read_stl(args.filename)
    if faces and normals:
        CM.separate_norms(normals)
else:
    print("No file type specified in command flags")