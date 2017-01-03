from sys import argv

#We set future parameters, which give in command line
script, filename = argv

#open file by fure name
txt = open(filename)

#Print which file has been entered, and used new style for this purpose.
print "Here is your file {}".format(filename)

print txt.read()

#Reapet actions above.
print "Type  the filename again:"
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()
