# Python - Everything is object

![Background Context](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```bash
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```bash
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

## Files

|   Filename   | Description                                                                                         |
| :----------: | --------------------------------------------------------------------------------------------------- |
| 0-answer.txt | What function would you use to print the type of an object?                                         |
| 1-answer.txt | How do you get the variable identifier (which is the memory address in the CPython implementation)? |

## PS

This is a project done during Full Stack Software Engineering studies at ALX_AFRICA. The objectives of the project is teach ALX-SE students about the difference between a class and an object or instance, the difference between immutable object and mutable object, reference and assignment
