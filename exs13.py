from sys import argv

# argv alow us pass arg from command line, here we combine it's with raw_input

script, first, second, third = argv, raw_input('Enter first element:'), raw_input('Enter second element:'), raw_input('Enter third element:')

four = raw_input('Enter fout element')

print "The script is called:", script

print "You first variable is:",first

print "Your second variable is:",second

print "Your third variable is:", third

print "Your four variable is:", four
