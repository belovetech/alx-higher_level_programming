# Python inheritance

## Basic inheritance

Technically, every class we create uses inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only), but it does allow Python to treat all objects in the same way.

If we don’t explicitly inherit from a different class, our classes will automatically inherit from object. However, we can openly state that our class derives from object using the following syntax:

```Python
class MySubClass(object):
 pass

```
