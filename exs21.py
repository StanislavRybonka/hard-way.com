def add(a, b):
    print "Adding: {} + {}".format(a, b)

    return a + b

def subtract(a, b):
    print "Subtracting: {} - {}".format(a, b)

    return a - b


def multiply(a, b):
    print "Multiplying:{} * {}".format(a, b)

    return a * b

def divide(a, b):
    print "Dividing: {} / {}".format(a, b)

    return a / b


print "Let's go do some math!"

age = add(20, 5)
height = subtract(200, 20)
weight = multiply(40, 2)
iq = divide(100, 2)

print "My age:{}, my height:{}, my weight:{}, my iq:{}".format(age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight, divide(iq, 2))))

print " That becomes: ", what, "Can you do it by hand?"
