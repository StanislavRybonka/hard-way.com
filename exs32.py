the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print 'This is count {}'.format(number)

for fruit in fruits:
    print 'A fruit of type: {}'.format(fruit)

for i in change:
    print 'I got {}'.format(i)

elements = []
for i in range(0, 6):
    print 'Add this {}, to the list.'.format(i)
    elements.append(i)

for i in elements:
    print 'This is new elements:{}'.format(i)

elements_new = []
numbers = range(0, 6)
elements_new.append(numbers)

print elements_new
for key in elements_new:
    print 'This is new list of elements:{}'.format(key)
    for key1 in key:
        print 'Separeted list at list by one:{}'.format(key1)
