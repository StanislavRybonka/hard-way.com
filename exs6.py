
#Here we embed digits using new format type
x = "There are {} types of people.".format(10)

binary = "binary"

do_not = "Don't"

#Here we used old formating types
y = "Thouse who know %s those who %s " % (binary, do_not)

print x

print y

print "I sad: %r " % x

print "I also said: %s" % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r "

print joke_evaluation % hilarious

w = "This is the left side of ..."

e = "a string with a right side ."

#And concatinate variables above

print w + e
