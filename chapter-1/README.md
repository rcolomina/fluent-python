# The Python Data Model

## A deck as a squence of cards

The chapter starts with an example about **magic methods** or **dunder methods** applied to a Pythonic Card Deck

It creates a deck of cards with collection and a class with `__len__` and `__getitem__` implemented. 

See example 1.1

## How Special Methods Are Used

Special methods are meant to be called by the Python interpreter (built-in features)

As example:

`my_object.__len__()`

or

`len(my_object)`


Notice that the expresion 

`for i i x:` 

casues the invocations of 

`iter(x)` 

or 

`x.__iter__()`


Calling these methods directly allows to do mateprogramming

build-ins: `len`, `iter`, `str`,...  faster!! than method calls

WARNING! Don't create attributes like `__foo__` because its syntax may adquire special meaning


## Emulating Numerical Types

Creates an example of class of Euclidean vectors used in maths and physics

For that dunder methods: `__abs__`, `__mul__`, `__add__` were implemanted accordantly 
sum of vectors and scalar per vector linear algebra operations

See example 1.2

## String Representation

Here `__repr__` and `__str__` are discussed, which both are used to represent the object, but:

`__repr__` is for developers
`__str__`  is for the user

Notice that, if `__str__` not defined, then `__repr__` is used as fallback

## Arithmetic Operators

In the example, these operators treat objects as immutable, and new ones 
creatd out of the operations `__mul__` and `__add__`

In the example 1-2, the `__mul__` is NOT commutative!(this will be fixed in Chapter 13)


## Boolean Value of a Custom Type

`__bool__` is implemented on objects to define its behaviour when it is used as expressons passed to if-else statements 

By default classes are considerd truthy

If `__bool__` or `__len__` implemented, then `__bool__` is used first and if the latter is not implemented, then `__len__`

In the example, `__bool__` has been implemented in function of the moduel of the vector is 0 or not.

## Overview of Special Methods

In this section special methods are listed in two tables, the ones that are not for operators and the ones that are

| Category                        | Special Methods | Explanation |
|---------------------------------|----------------|-------------|
| **String/Bytes**                | `__str__` | Returns the informal string representation (used by `str()`). |
|                                 | `__repr__` | Returns the official string representation (used by `repr()`). |
|                                 | `__bytes__` | Converts the object to bytes (used by `bytes()`). |
|                                 | `__format__` | Customizes formatting using `format()`. |
| **Conversion to Number**        | `__int__` | Converts the object to an integer (used by `int()`). |
|                                 | `__float__` | Converts the object to a float (used by `float()`). |
|                                 | `__bool__` | Defines the truth value of an object (used by `bool()`). |
|                                 | `__index__` | Converts the object to an integer index (used in slicing). |
| **Emulating Collections**       | `__len__` | Returns the length of a collection (used by `len()`). |
|                                 | `__getitem__` | Retrieves an item using indexing (`obj[key]`). |
|                                 | `__setitem__` | Sets an item using indexing (`obj[key] = value`). |
|                                 | `__contains__` | Implements membership testing (`item in obj`). |
| **Iteration**                   | `__iter__` | Returns an iterator (used in `for` loops). |
|                                 | `__next__` | Returns the next item in an iterator (used by `next()`). |
| **Emulating Callables**         | `__call__` | Makes an object callable like a function (`obj()`). |
| **Instance Creation and Destruction** | `__new__` | Controls instance creation (before `__init__`). |
|                                 | `__init__` | Initializes a new instance. |
|                                 | `__del__` | Called before an object is destroyed (not recommended for cleanup). |
| **Attribute Management**        | `__getattr__` | Handles attribute access for missing attributes. |
|                                 | `__getattribute__` | Intercepts every attribute access. |
|                                 | `__setattr__` | Customizes behavior when setting an attribute. |
|                                 | `__delattr__` | Handles attribute deletion. |
| **Class Services**              | `__instancecheck__` | Defines `isinstance(instance, Class)` behavior. |
|                                 | `__subclasscheck__` | Defines `issubclass(Subclass, Class)` behavior. |
|                                 | `__class_getitem__` | Supports generics (`MyClass[int]`). |

## Special Methods for Operators

| Category                        | Special Methods | Explanation |
|---------------------------------|----------------|-------------|
| **Unary Numeric Operators**     | `__neg__` | Implements negation (`-obj`). |
|                                 | `__pos__` | Implements unary plus (`+obj`). |
|                                 | `__abs__` | Implements absolute value (`abs(obj)`). |
|                                 | `__invert__` | Implements bitwise negation (`~obj`). |
| **Rich Comparison Operators**   | `__eq__` | Implements equality (`==`). |
|                                 | `__ne__` | Implements inequality (`!=`). |
|                                 | `__lt__` | Implements less than (`<`). |
|                                 | `__le__` | Implements less than or equal (`<=`). |
|                                 | `__gt__` | Implements greater than (`>`). |
|                                 | `__ge__` | Implements greater than or equal (`>=`). |
| **Arithmetic Operators**        | `__add__` | Implements addition (`+`). |
|                                 | `__sub__` | Implements subtraction (`-`). |
|                                 | `__mul__` | Implements multiplication (`*`). |
|                                 | `__truediv__` | Implements true division (`/`). |
|                                 | `__floordiv__` | Implements floor division (`//`). |
|                                 | `__mod__` | Implements modulus (`%`). |
|                                 | `__pow__` | Implements exponentiation (`**`). |
| **Reversed Arithmetic Operators** | `__radd__` | Implements reversed addition (`other + self`). |
|                                 | `__rsub__` | Implements reversed subtraction (`other - self`). |
|                                 | `__rmul__` | Implements reversed multiplication (`other * self`). |
|                                 | `__rtruediv__` | Implements reversed true division (`other / self`). |
|                                 | `__rfloordiv__` | Implements reversed floor division (`other // self`). |
|                                 | `__rmod__` | Implements reversed modulus (`other % self`). |
|                                 | `__rpow__` | Implements reversed exponentiation (`other ** self`). |
| **Augmented Assignment Operators** | `__iadd__` | Implements `+=`. |
|                                 | `__isub__` | Implements `-=`. |
|                                 | `__imul__` | Implements `*=`. |
|                                 | `__itruediv__` | Implements `/=`. |
|                                 | `__ifloordiv__` | Implements `//=`. |
|                                 | `__imod__` | Implements `%=`. |
|                                 | `__ipow__` | Implements `**=`. |
| **Bitwise Operators**           | `__and__` | Implements bitwise AND (`&`). |
|                                 | `__or__` | Implements bitwise OR (`|`). |
|                                 | `__xor__` | Implements bitwise XOR (`^`). |
|                                 | `__lshift__` | Implements left shift (`<<`). |
|                                 | `__rshift__` | Implements right shift (`>>`). |
| **Reversed Bitwise Operators**  | `__rand__` | Implements reversed bitwise AND (`other & self`). |
|                                 | `__ror__` | Implements reversed bitwise OR (`other \| self`). |
|                                 | `__rxor__` | Implements reversed bitwise XOR (`other ^ self`). |
|                                 | `__rlshift__` | Implements reversed left shift (`other << self`). |
|                                 | `__rrshift__` | Implements reversed right shift (`other >> self`). |
| **Augmented Assignment Bitwise Operators** | `__iand__` | Implements `&=`. |
|                                 | `__ior__` | Implements `\|=`. |
|                                 | `__ixor__` | Implements `^=`. |
|                                 | `__ilshift__` | Implements `<<=`. |
|                                 | `__irshift__` | Implements `>>=`. |



Important to understand that the reversed operators are called as fallbacks when are swapped (`b * a` instead of `a * b`)


## Why len is Not a Method

Getting the number of items in a collections is a common operation and must work efficiently

## Chapter Summary

* Build-in methods
* Example on implementation of `__repr__`,`__str__`,`__len__` and `__getitem__` handling a collection of French Deck
* Rich selection of numericla types from build-ins
* Next chapters will cover 

## Further Reading

* [The "Data Model"](http://docs.python.org/3/reference/datamodel.html)
* [Python in a Nutshell](http://stackoverflow.com/users/95810/alex-martelli)
* Python 3 : Python Essential Reference
* Python cookbook
* The Art of the Metaobjects Protocol (MOP)

## Soapbox

### Data Model or Object Model?
Documentation favors **Data Model** over **Object Model**, however some authors woulde say "Python object model" instead of "Python data Model"
### Magic Methods
Obviously these are not magic (difficult to implement), and Python community enables users to leverage the same tools available to core developers
### Metaobjects
* **The Art of Metaobject Protocol (AMOP) book is recommended**. Metaobject protocol is an API for core language constructs
* Finally mention that a rich metaobject protocol leads to aspect-oriented programming becomes easier, such as the dynamic language Python. Reference to interface programming in Python at [`zope.interface`](https://zopeinterface.readthedocs.io/en/latest/README.html)

