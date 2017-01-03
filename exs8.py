formatter = '%r %r %r %r'

#Maked variables and put content inside.

print formatter % (1, 2, 3, 4)

print formatter % ('One', 'Two', 'Three', 'Four')

print formatter % (formatter, formatter, formatter, formatter)
