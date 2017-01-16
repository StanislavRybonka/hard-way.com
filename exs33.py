
numbers = []

def get_numbers(arg1,arg2):
    i = 0
    while i < arg1:
        print 'At the top i is {}'.format(i)
        numbers.append(i)

        i += arg2
        print 'Numbers now:', numbers
        print 'At the bottom i is {}'.format(i)

    print 'The numbers:'
    for key in numbers:
         print key


get_numbers(10,1)
