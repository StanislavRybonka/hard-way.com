print "You enter a dark room wih two doors.Choose door 1 or 2."

door = raw_input(">")

if door == '1':
    print 'There is a giant bear here eating a cheese cake. What do you do?'
    print '1. Take the cake.'
    print '2. Scream at the bear.'

    bear = raw_input('>')

    if bear == '1':
        print 'The bear won, bad job'
    elif bear == '2':
        print 'The bear lose, bad job'
    else:
        print 'Well, doing {} is probably better.Bear runs away!'.format(bear)
elif door == '2':
    print 'You stage into the endless abyss'
    print 'Blueberries'
    print 'Yellow jecket'

    insanity = raw_input('>')

    if insanity == '1' or '2':
        print 'Your body survives powered by amind of jello.'
    else:
        print 'Bad job.'
else:
    print 'You stumble around.'
