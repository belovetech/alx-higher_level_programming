# Python inheritance

## Basic inheritance

Technically, every class we create uses inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only), but it does allow Python to treat all objects in the same way.

If we don’t explicitly inherit from a different class, our classes will automatically inherit from object. However, we can openly state that our class derives from object using the following syntax:

```Python
class MySubClass(object):
 pass

```

All `main.py` files contain code that utilize the class object and function created. Also, tests directory contains test files for task number one and seven.

### Files in the directory

| Filename              | Description                                                                     |
| --------------------- | ------------------------------------------------------------------------------- |
| 0-lookup.py           | Function that returns the list of available attributes and methods of an object |
| 1-my_list.py          | Class `MyList` that inherits from list                                          |
| 2-is_same_class.py    | Chech if exact same object                                                      |
| 3-is_kind_of_class.py | Chech if same class or inherit                                                  |
| 4-inherits_from.py    | Chech if Only sub class of                                                      |
| 5-base_geometry.py    | An empty class `BaseGeometry`.                                                  |
| 6-base_geometry.py    | Improve Geometry                                                                |
| 7-base_geometry.py    | Integer validator                                                               |
| 8-rectangle.py        | Class `Rectangle` that inherits from `BaseGeometry`                             |
| 9-rectangle.py        | Class `Rectangle` that inherits from `BaseGeometry`                             |
| 10-square.py          | Class `Square` that inherits from `Rectangle`                                   |
| 11-square.py          | Class `Square` that inherits from `Rectangle`                                   |
| 100-my_int.py         | Class `MyInt` that inherits from int                                            |
| 101-add_attribute.py  | Function that adds a new attribute to an object if it’s possible:               |

### PS

This is a project done during Full Stack Software Engineering studies at ALX_AFRICA. The objectives of the project is teach ALX-SE students about `inheritance` in Python, differences between `isinstance`, `issubclass`, `type` and `super` and how to use them.
