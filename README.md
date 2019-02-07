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
