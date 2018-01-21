# .format can be treatedlike a list of characters
"This is a string"[0] # => 'T'

#.format can be used to format strings, like this:
"{} can be {}".format("String", "interpolated") # =>"String can be interpolated

#You can repeatthe formatting arguments to save some typing
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candlestick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"


# can use keywords if you don't want to count.
print "{name} wants to eat {food}".format(name="Bob", food="Lasagna")
# => "Bob wants to eat lasagna"


####################################################
## 2. Variables and Collections
####################################################

# By default the print function also prints out a newline at the end
# Use the optional argument end to change the end character
# print("Hello, Python", end="!")

#Simple way to get input data from console
# input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlierversions ofPython, input() method was named as raw_input()

# No need to declare varibles before assigning to them.
# Convention is to use lower_case_with_underscores
some_var = 5
some_var # => 5

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuffto the end of a list with append
li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]
li.append(4)  # li is now [1, 2, 4]
li.append(3)  # li isnowe [1, 2, 4, 3]

# Remove from the end with pop
li.pop() # => 3 and li is now [1, 2, 4]
print li
# Let'sput it back
li.append(3) # li is now [1, 2, 4, 3] again.

# Access a listlike you would any array
li[0] # => 1

# look at the last element
li[-1] # => 3

# Looking out of bounds is an IndexError
# li[4] # Raises an IndexError

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
li[1:3] # => [2, 4]

#Omit the beginning
li[:3]  # => [4, 3]

#Select every second entry
li[::2]  # => [1, 4]

# Return a reversed copy ofthe list
li[::-1] # => [3, 4, 2, 1]
#Use any combination of these to make advanced slices
#li[start:end:step]

# Makea one layer deep copy using slices
li2 = li[:] # => li2 = [1, 2, 4, 3] but(li2 is li) will resultin false

# Remove arbitrary elements from a list with "del"
del li[2] # liisnow [1, 2, 3]

# Remove first occurrence of a value
li.remove(2) # li is now [1, 3]
# li.remove(2) # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
# li.index(4) # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified
print li + other_li # => [1, 2 , 3, 4, 5, 6]

# Concatenate lists with "extend()"
print li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
print 1 in li # => 6



# Tuples are like lists but are immutable.
tup = (1, 2, 3)
print tup[0] # => 1
# print tup =[3] # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
print type((1)) # => <class 'int>
print type((1,)) # => <class 'tuple'>
print type(()) # => <class 'tuple'>

# You can do most of the list operations on tuples too
print len(tup)  #=> 3
print tup + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
print tup[:2]  # => (1, 2)
print 2 in tup # => True

# You can unpack tuples (or lists) into variables
a, b, c =(1, 2, 3) # a is now 1, b isnow 2 and c is now 3

# You can also do extended unpacking
# (Python3 )print a, *b, c = (1, 2, 3, 4) # a is now 1, bis now 2 and c is now 3


# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6

# Now look how easy it is to swap two values
e, d = d, e 
















