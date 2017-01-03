from sys import argv
from os.path import exists


script, from_lile, to_file = argv

print "Copying from {} to {}".format(from_lile, to_file)

indata = open(from_lile).read()

print "The input file is {} bytes long".format(len(indata))

print "Does the output file exist? {}".format(to_file)

print "Ready, hit RETURN to continue, EXIT for abort."

raw_input()

out_file = open(to_file, 'w').write(indata)

print "All right, all done."
