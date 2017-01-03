from sys import argv

#Set var, and take arg from terminal
script, input_file = argv

#This function only read from file
def print_all(f):
    print f.read()
#Take index
def rewind(f):
    f.seek(0)
#Print by line
def print_a_line(line_count, f):
    print line_count, f.readline()

#Set active file
current_file = open(input_file)

print "First let's point the all file:\n"

#Print all
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Return index
rewind(current_file)

print "Let's print three lines:"

#Set line, pass to function, show by line
current_line = 1

print_a_line(current_line, current_file)

current_line += current_line

print_a_line(current_line, current_file)

current_line += current_line

print_a_line(current_line, current_file)
