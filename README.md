# Fluent Python

I'm going through the book and I'll add important concepts (IMO) that I come upon each chapter. 

## Chapter 01:

* **object.__getitem__(self, key)**: Called to implement evaluation of `self[key]`

* **object.__len__(self)**: Called to implement the built-in function `len()`

* **doctest.ELLIPSIS**: when the tests include values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the ELLIPSIS option to tell doctest to ignore portions of the verification value. More [here](https://pymotw.com/3/doctest/)

* **ranks**: Compute numerical data ranks (1 through n) along axis. Equal values are assigned a rank that is the average of the ranks of those values. More [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rank.html). All values get assigned a high score.

* **math.hypot(x, y)**: Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).

* **object.__repr__(self)**: It is convenient to be able to output the value of an instance of an object by using a print statement. When this is done, it's wanted that the value to be represented in the output in some understandable unambiguous format. The `__repr__` special method can be used to arrange for this to happen. More [here](https://docs.python.org/3/reference/datamodel.html), [here](https://www.codecademy.com/en/forum_questions/551c137f51b887bbc4001b73) and [here](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr). The goal of `__repr__` is to be unambiguous while the goal of `__str__` is readability. So `str` should be friendly humand readable, while `repr` includes detailed information about the object's content. String formatting [here](https://docs.python.org/dev/library/string.html#string-formatting).
Example:
```python
>>> print(str('sunshine'))
sunshine

>>> print(repr('sunshine'))
'sunshine'
```

## Chapter 02:

* **Container sequences**: Hold reference to the objects they contain. These objects can be os any type. `list`, `tuple` and `collections.deck` are examples.

* **Flat sequences**: Physically store the value of each item in own memory space, not as distinct objects. They are more compact, but they are limited to holding primitive values like characters, bytes, and numbers. `str`, `bytes`, `bytearray`, `memoryview`, and `array.array` are examples. They hold items of one type. Flat sequences only hold atomic types like integer, floats or characters.

* **Mutable sequences**: `list`, `bytearray`, `array.array`, `collections.deque`, and `memoryview` 

* **Immutable sequences**: `tuple`, `str`, and `bytes`
* **Generator expression**: It saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor. They use the same syntax as `list comprehensions`, but are enclose by paranheses. More [here](https://www.python.org/dev/peps/pep-0289/)

* **`ellipsis`**: It is recognized as a token by the Python parser. It is written with three full stops `(...)` and it is an alias to the `Ellipsis` object, the single instance of the `ellipsis` class. As such, it can be passed as an argument to functions and as part of a slice specification, as in` f(a, ..., z)` or `a[i:...]`. NumPy uses ... as a shortcut when slicing arrays of many dimensions; for example, if x is a 4D array, `x[i, ...]` is a shortcut for `x[i, :, :, :,]`.

* **bisect(obj to insert, insertion value, lo, hi)**: This function return the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. It maintains a list in sorted order without having to call sort each time an item is added to the list. `bisect_let(obj to insert, insertion value)`: If the insertion value is already present in the list, the insertion point will be before (to the left of) any existing entries. `bisect_right` is similar to `bisect_left` but it returns an insertion point which comes after (to the right of) any existing entries of insertion value in the object. A pair of optional arguments, lo and hi, allow narrowing the region in the sequence to be searched when inserting. lo defaults to 0 and hi to the len() of the sequence.

* **Data types in C**: good info [here](https://www.studytonight.com/c/datatype-in-c.php) and also [here](https://www.thoughtco.com/definition-of-double-958065) about `float` and `double`

* **memoryview**: A `memoryview` is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLlite databases, NumPy arrays, etc.) without first copying. This is very important for large data sets. The method `memoryview.cast` will cast a `memoryview` to a new format or shape (reah more [here](https://docs.python.org/3/library/stdtypes.html#binaryseq)). The return value is a new memoryview, but the buffer itself is not copied. One of the destination formats must be a byte format (‘B’, ‘b’ or ‘c’). The byte length of the result must be the same as the original length.

* **`time.perf_counter`**: Return the value (in fractional seconds) of a performance counter. More [here](https://stackoverflow.com/a/25787875)

## Chapter 03:

* **`re.compile`**: The purpose of `compile`  is to compile the regular expression pattern that will be used for matching later. Great reminder about `special sequences` [here](https://www.regular-expressions.info/characters.html#special). For instance, `\w` matches one alphanumeric character. It is short for `[a-zA-Z0-9]` The `+` siggn is  a `quantifier`. It means *one or more*

* **match**: This method determine if the regurlar expression matches at the beginning of the string. It returns a match object or None (in case no match was found)

* **finditer**: Returns an iterator over all non-overlapping matches. More [here](https://www.saltycrane.com/blog/2007/10/python-finditer-regular-expression/)

* **group()**: Return the string matched by the regular expression

* **strat()** Returns the start position of the string. For example:
```python
>>> import re
>>> mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
>>> mo.group()
'232454'
mo.start()
17
```
More [here](https://www.python-course.eu/python3_re.php)

* **MappingProxyType**: It returns a m`mappingproxy` instance that is read-only. [Info](https://docs.python.org/3/library/types.html)


## Chapter 05

* **Higher-Order Functions**: a function that takes a function as argument or returns a function as the result 

