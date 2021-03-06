# Pythumbnail

What is Pythumbnail?
---------------------

Pythumbnail is a quick thumbnail creator for python codes. You can get an overview of the available functions, for/while loops and if conditions without even running the code.

Suppose you have the following python file:

```python
class someclass:
    def __init__(self):
        self.a = 10

    def do_something(self):
        for i in range(len(self.a)):
            if i == 2:
                print(i)

    def do_something_else(self, num):
        while self.a < 100:
            self.a += num
```


Here is a small example to show what Pythumbnail could do (Python 3):

```python
import pythumbnail

file = pythumbnail.read_file('some_file.py')
print(file.tree)
```

The output will look like:

```python
'File some_file.py()'
    'class someclass()'
        'def __init__(self)'
        'def do_something(self)'
            'for i in range(len(self.a))'
                'if[i,2] LOGIC: [==]'
        'def do_something_else(self,num)'
            'while[self.a,100] LOGIC: [<]'
```

Quick Start
-----------

To install Pythumbnail, you need python version 3.6.0 or above. Pythumbnail could be installed from pypi:

    $ python3 -m pip install pythumbnail

Running Pythumbnail:

```python
import pythumbnail
```

Documentation
-------------

Full documentation is available [here](https://kevinyang372.github.io/py-thumbnail/)

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
-------

[Apache License 2.0](http://www.apache.org/licenses/)