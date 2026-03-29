# 2. Data Structures
# Data structures are used to store and organize data. In Python, we have several built-in data structures such as lists, tuples, sets, and dictionaries.
# 2.1 Tuples
# A tuple is an ordered collection of items. It is immutable, which means that we cannot change the values of a tuple after it is created. We can create a tuple using parentheses ().
my_tuple = (1, 2, 3, 'Hello', True)
print(my_tuple) # Output: (1, 2, 3, 'Hello', True)
print(type(my_tuple)) # Output: <class 'tuple'>
# We can also create a tuple without using parentheses. This is called tuple packing.
my_tuple2 = 1, 2, 3, 'Hello', True
print(my_tuple2) # Output: (1, 2, 3, 'Hello', True)
print(type(my_tuple2)) # Output: <class 'tuple'>
# We can access the elements of a tuple using indexing. The index starts from 0.
print(my_tuple[0]) # Output: 1
print(my_tuple[3]) # Output: 'Hello'
# we can also use negative indexing to access the elements of tuple. The last element of the tuple has an index of -1, the second last element has an index of -2, and so on.
print(my_tuple[-1]) # Output: True
print(my_tuple[-4]) # Output: 2
# We can also use slicing to access a portion of the tuple. The syntax for slicing is tuple[start:stop:step]. The start index is inclusive and the stop index is exclusive. The step is optional and it is used to specify the step size for slicing.
print(my_tuple[1:4]) # Output: (2, 3, 'Hello')
print(my_tuple[::2]) # Output: (1, 3, True)
# We can also use the len() function to get the length of a tuple.
print(len(my_tuple)) # Output: 5
# We can also use the count() method to count the number of occurrences of a specific value in a tuple.
print(my_tuple.count(2)) # Output: 1
# We can also use the index() method to get the index of the first occurrence of a specific value in a tuple.
print(my_tuple.index('Hello')) # Output: 3
# We can also create a tuple inside a tuple. This is called nested tuple.
nested_tuple = (1, 2, (3, 4), 'Hello')
print(nested_tuple) # Output: (1, 2, (3, 4), 'Hello')
print(nested_tuple[2]) # Output: (3, 4)
print(nested_tuple[2][0]) # Output: 3
# if we want to convert a list to a tuple, we can use the tuple() function.
my_list = [1, 2, 3, 'Hello', True]
my_tuple3 = tuple(my_list)
print(my_tuple3) # Output: (1, 2, 3, 'Hello', True)
# Finally, we can also use the unpacking operator * to unpack the elements of a tuple into separate variables.
a, b, c, d, e = my_tuple
print(a) # Output: 1

# We can also use the unpacking operator * to unpack the elements of a tuple into a list.
my_tuple4 = (1, 2, 3, 'Hello', True)
my_list2 = [*my_tuple4]
print(my_list2) # Output: [1, 2, 3, 'Hello', True]

# 2.2 lists
# A list is an ordered collection of items. It is mutable, which means that we can change the values of a list after it is created. We can create a list using square brackets [].
my_list = [1, 2, 3, 'Hello', True]
print(my_list) # Output: [1, 2, 3, 'Hello', True]
print(type(my_list)) # Output: <class 'list'>
# We can access the elements of a list using indexing. The index starts from 0.
print(my_list[0]) # Output: 1
print(my_list[3]) # Output: 'Hello'
# we can also use negative indexing to access the elements of list. The last element of the list has an index of -1, the second last element has an index of -2, and so on.
print(my_list[-1]) # Output: True
print(my_list[-4]) # Output: 2
# We can also use slicing to access a portion of the list. The syntax for slicing is list[start:stop:step]. The start index is inclusive and the stop index is exclusive. The step is optional and it is used to specify the step size for slicing.
print(my_list[1:4]) # Output: [2, 3, 'Hello']
print(my_list[::2]) # Output: [1, 3, True]  
# We can also use the len() function to get the length of a list.
print(len(my_list)) # Output: 5
# We can also use the count() method to count the number of occurrences of a specific value in a list.
print(my_list.count(2)) # Output: 1
# We can also use the index() method to get the index of the first occurrence of a specific value in a list.
print(my_list.index('Hello')) # Output: 3
# We can also create a list inside a list. This is called nested list.
nested_list = [1, 2, [3, 4], 'Hello']
print(nested_list) # Output: [1, 2, [3, 4], 'Hello']
print(nested_list[2]) # Output: [3, 4]
print(nested_list[2][0]) # Output: 3
# if we want to convert a tuple to a list, we can use the list() function.
my_tuple = (1, 2, 3, 'Hello', True)
my_list2 = list(my_tuple)
print(my_list2) # Output: [1, 2, 3, 'Hello', True]
# if we want to convert a string to a list, we can use the split() method. The split() method splits a string into a list of substrings based on a specified delimiter. The default delimiter is whitespace.
my_string = 'Hello World'
my_list3 = my_string.split() # this will split the string into a list of words, the default delimiter is whitespace but we can specify any delimiter we want
print(my_list3) # Output: ['Hello', 'World']
# if we want to convert a list to a string, we can use the join() method. The join() method joins the elements of a list into a single string using a specified delimiter.
my_list4 = ['Hello', 'World']
my_string2 = ' '.join(my_list4) # this will join the elements of the
print(my_string2) # Output: 'Hello World'
# For concatenating two lists, we can use the + operator.
list1 = [1, 2, 3]
list2 = ['Hello', True]
list3 = list1 + list2
print(list3) # Output: [1, 2, 3, 'Hello', True]
# also we can use the extend() method to concatenate two lists.
list1 = [1, 2, 3]
list2 = ['Hello', True]
list1.extend(list2)
print(list1) # Output: [1, 2, 3, 'Hello', True]
# if we want to repeat a list multiple times, we can use the * operator.
list1 = [1, 2, 3]
list2 = list1 * 3
print(list2) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# if we want to check if an element is present in a list, we can use the in operator.
print(2 in list1) # Output: True
print('Hello' in list1) # Output: False
# if we want to add an element to the end of a list, we can use the append() method.
list1 = [1, 2, 3]
list1.append('Hello')
print(list1) # Output: [1, 2, 3, 'Hello']
# if we want to insert an element at a specific index in a list, we can use the insert() method.
list1 = [1, 2, 3]
list1.insert(1, 'Hello') # this will insert 'Hello' at index 1
print(list1) # Output: [1, 'Hello', 2, 3]
# if we want to remove an element from a list, we can use the remove() method.
list1 = [1, 'Hello', 2, 3]
list1.remove('Hello')   
print(list1) # Output: [1, 2, 3]
# if we want to remove an element at a specific index from a list, we can use the pop() method.
list1 = [1, 2, 3]   
list1.pop(1) # this will remove the element at index 1
print(list1) # Output: [1, 3]
# Finally, we can also use the unpacking operator * to unpack the elements of a list into separate variables.
a, b, c, d, e = my_list
print(a) # Output: 1
# We can also use the unpacking operator * to unpack the elements of a list into a tuple.
my_list3 = [1, 2, 3, 'Hello', True]

# 2.3 Sets
# A set is an unordered collection of unique items. It is mutable, which means that we can change the values of a set after it is created. We can create a set using curly braces {}.
my_set = {1, 2, 3, 'Hello', True}
print(my_set) # Output: {1, 2, 3, 'Hello', True}
print(type(my_set)) # Output: <class 'set'>
# We can also create a set using the set() function.
my_set2 = set([1, 2, 3, 'Hello', True])
print(my_set2) # Output: {1, 2, 3, 'Hello', True}
print(type(my_set2)) # Output: <class 'set'>
# We can also create a set from a string. This will create a set of unique characters in the string.
my_string = 'Hello World'
my_set3 = set(my_string)
print(my_set3) # Output: {'H', 'e', 'l', 'o', ' ', 'W', 'r', 'd'}
# We can also use the len() function to get the length of a set.
print(len(my_set)) # Output: 5
# A ser variable of type set can only contain unique values. If we try to add a duplicate value to a set, it will be ignored.
# we could use set operations such as union, intersection, difference, and symmetric difference to perform operations on sets.

# 2.4 Dictionaries
# A dictionary is an unordered collection of key-value pairs. It is mutable, which means that we can change the values of a dictionary after it is created. We can create a dictionary using curly braces {}.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(my_dict)) # Output: <class 'dict'>
# We can also create a dictionary using the dict() function.
my_dict2 = dict(name='John', age=30, city='New York')
print(my_dict2) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(my_dict2)) # Output: <class 'dict'>
# We can access the values of a dictionary using the keys. We can use the square brackets [] to access the values of a dictionary.
print(my_dict['name']) # Output: 'John'
print(my_dict['age']) # Output: 30
# We can also use the get() method to access the values of a dictionary. The get() method returns the value for the specified key if the key is in the dictionary, otherwise it returns None.
print(my_dict.get('name')) # Output: 'John'
print(my_dict.get('age')) # Output: 30
print(my_dict.get('country')) # Output: None
# We can also use the keys() method to get a list of all the keys in a dictionary.
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])
# We can also use the values() method to get a list of all the values in a dictionary.
print(my_dict.values()) # Output: dict_values(['John', 30, 'New York'])
# We can also use the items() method to get a list of all the key-value pairs in a dictionary.
print(my_dict.items()) # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
# We can also use the len() function to get the length of a dictionary.
print(len(my_dict)) # Output: 3
# if we want to add a new key-value pair to a dictionary, we can use the square brackets [] to add a new key-value pair to a dictionary.
my_dict['country'] = 'USA'
print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
# if we want to update the value of an existing key in a dictionary, we can use the square brackets [] to update the value of an existing key in a dictionary.
my_dict['age'] = 31
print(my_dict) # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}
# if we want to remove a key-value pair from a dictionary, we can use the pop() method to remove a key-value pair from a dictionary.
my_dict.pop('city')
print(my_dict) # Output: {'name': 'John', 'age': 31, 'country': 'USA'}
# if we want to remove a key-value pair from a dictionary, we can also use the del keyword to remove a key-value pair from a dictionary.
del my_dict['country']
print(my_dict) # Output: {'name': 'John', 'age': 31}