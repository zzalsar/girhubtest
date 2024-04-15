import argparse
parser = argparse.ArgumentParser(description='Search some files')
parser.add_argument(dest='filenames',metavar='filename', nargs=1, default='mrs.yml')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
args = parser.parse_args()

# Output the collected arguments
print(args.filenames) 
print(args.verbose) 
print(args.outfile) 
