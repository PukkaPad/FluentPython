# Fluent Python

I'm going through the book and I'll add important concepts (IMO) that I come upon each chapter. 

## Chapter 01:

* **object.__getitem__(self, key)**: called to implement evaluation of `self[key]`

* **object.__len__(self)**: called to implement the built-in function `len()`

* **doctest.ELLIPSIS**: when the tests include values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the ELLIPSIS option to tell doctest to ignore portions of the verification value. More [here](https://pymotw.com/3/doctest/)