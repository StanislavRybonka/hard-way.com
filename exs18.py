#Work with functions

def print_two(*args):
    arg1, arg2 = args

    print "arg1: {}, arg2: {}".format(arg1, arg2)


print_two('Stanislav', 'Rybonka')

def checklist(index_card):
    if index_card is not None:
        print index_card


checklist(1)
