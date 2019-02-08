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

