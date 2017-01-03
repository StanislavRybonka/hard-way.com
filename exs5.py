my_name = "Stanislav Rybonka"

my_age = 25.5

my_height = 180

my_weight = 80

my_eyes = "Blue"

my_teeth = "White"

my_hair = "Brown"

my_test_var = "This is string"

print "My name is: %s" % my_name

print "I'm %d iches tall." % my_height

print "I'm %d heavy" % my_weight

print "I have %s eyes and %s hair" % (my_eyes, my_hair)

print "My teeth are usually %s depending on the coffee" % my_teeth

print "My test var {} ".format(my_test_var)

class Data(object):
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


print "{0!r}{0!s}".format(Data())
