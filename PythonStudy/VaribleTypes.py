#Multi-variable assignment
a = b = c = 1

a ,b ,c = 1, 2, "john"
print a ,b ,c


#String
str = 'Ilovepython'
print str
print str[0] #first string
print str[2:5]
print str[2:]
print str * 2
print str + "Too"

#List
list = [ 'abcd', 521 , 2.23 , 'alice', 70.2 ]
tinylist = [123, 'alice']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list +tinylist

print '--------------'
#Tuple

tuple = ( 'ada', 152 , 2.36, 'Jake', 23.6 )
tinytuple =(178 , 'jay')

print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple
#print tuple[2] = 1000 Note allow updates


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'Alice','code':156852, 'dept': 'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()



