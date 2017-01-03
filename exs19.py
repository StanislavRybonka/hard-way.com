#Here we describe our function, for future purpose.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    cheese_count = raw_input('How much cheeses?')
    boxes_of_crackers = raw_input('How much crackers?')
    print "You have {} cheeses!".format(cheese_count)
    print "You have {} boxes of crackers!".format(boxes_of_crackers)
    print "Man that's enough for party!"
    print "Get a blanket. \n"



print "We can give function numbers directly:"

#Here we pass arg to function directly
cheese_and_crackers(20, 30)

print "Or we can use variable from our scripts."

amount_of_cheese = 10
amount_of_crackers = 20

#Here we use variables like a arg for function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside to."

#Here we use math with function
cheese_and_crackers(10 + 15, 20 + 5)

print "And we can combine, variables and math."

#Here we pass to the function variable and set nubber directly
cheese_and_crackers(amount_of_cheese + 30, amount_of_crackers + 20)
