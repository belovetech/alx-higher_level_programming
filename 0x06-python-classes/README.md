# Classes and Objects

![image.png](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

Python is an Object Oriented Programming Language (OOP). Classes and Objects are the two main aspect of OOP. A class creates a new type while objects are instances of the class.

## Classes

The simplest definition of class in python is shown in the example below `(save as simple_class.py):`

```bash
#!/usr/bin/python3
class Square:
"""An empty class Square that defines a square"""
    pass  # An empty block

Object1 = Square()
print(Object1)
```

## Output

```bash
$ ./simple_class.py
<class '__main__.Square'>
```

### Files in the directory

| Filename                  | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| 0-square.py               | Empty class `Square` that defines a square                             |
| 1-square.py               | Class `Square` that defines a square by its size                       |
| 2-square.py               | Class `Square` that validate its sizemethods                           |
| 3-square.py               | Class `Square` that defines area of square                             |
| 4-square.py               | Class `Square` that access and update private attribute                |
| 5-square.py               | Class `Square` that prints in stdout the qquare with the character `#` |
| 6-square.py               | Class `Square` that defines coordinates of a square                    |
| 100-singly_linked_list.py | class Node that defines a `node` of a singly linked list               |
| 101-square.py             | Class `Square` that print Square instance                              |
| 102-square.py             | Class `Square` that compare 2 squares                                  |
| 103-magic_class.py        | Python class MagicClass                                                |

### PS

This is a project done during Full Stack Software Engineering studies at ALX_AFRICA. The objectives of the project is teach ALX-SE students about object oriented programming (OOP), `__init__` method, `__dict__` method, `getattr` function, Data Abstraction, Data Encapsulation, and Information Hiding, Public, Protected, and Private Attributesin Python.
