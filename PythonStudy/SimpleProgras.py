#3 For loop, bult-in enumerate function, new style formatting
friends = ['Alice', 'pat', 'gray', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)

# 4 Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 10:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)

# 5 Functions
def greet(name):
    print 'Hello', name
greet('Jack')
greet('Jill')
greet('Bob')

#6 Import, regular expressions
import re
for test_string in ['886-7245', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'
#7 Dictionres, generator expressions
prices = {'apple': 0.5, 'banana': 0.}
my_phrchase = {
    'apple' : 1,
    'banana': 7}

grocery_bill = sum(prices[fruit] * my_phrchase[fruit]
                   for fruit in my_phrchase)
print 'I owe the grocer $ %.2f ' %  grocery_bill
