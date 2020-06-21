"""Limited List
Without using inheritence, creation of a class called LimitedList, initialized with a maximum number of
elements it can hold.
After the object reached its limit, if someone tries to append an additional value to the list – the new
member will be appended, and the first member in the list will be erased.
Object  should support append, as well as assignment and receiving items using [].
Object  should implement the __repr__ slot.
For example:
>>> my_list = LimitedList(3)
>>> my_list
[]
>>> my_list.append(5)
>>> my_list.append(2)
>>> my_list.append(10)
>>> my_list
[5, 2, 10]
>>> my_list.append("hello")
>>> my_list
[2, 10, 'hello']
>>> my_list[1] = "changed"
>>> my_list
[2, 'changed', 'hello'].   Hint: Google __getitem__ and __setitem__."""

from collections import deque

# create our custom list class
class LimitedList(object):
    # created a simple class  called limited_list
    # constructor __init__ initiializes my_limited_list with elements, a number the user specifies
    def __init__(self, elements=1):
        self.my_list = [0] * elements
    def __repr__(self):
        return 'These are my contents: ' + repr(self.my_list)
print(LimitedList())

# For setting the value
def __setitem__(self, index, value):
    self.my_list[index] = value

# For getting the value from our custom_list
def __getitem__(self, index):
    return "Hey you are accessing {} element whose value is: {}".format(index, self.my_list[index])



# Create my_custom_list with 12 elements
obj = LimitedList(12)

# Set value at index 0 to 1
# obj[0]=1
print('my_list index 0',obj[0])

# print value at index 0
# print(obj[0])

# print the whole my_custom_list
print(obj)

"""Python __repr__() function returns the object representation. It could be any valid python
    expression such as tuple, dictionary, string etc.
    This method is called when repr() function is invoked on the object, in that case, __repr__() 
    function must return a String otherwise error will be thrown"""

"""items = deque([1, 2])
items.append(3)        # deque == [1, 2, 3]
items.rotate(1)        # The deque is now: [3, 1, 2]
items.rotate(-1)       # Returns deque to original state: [1, 2, 3]
item = items.popleft() # deque == [2, 3]"""