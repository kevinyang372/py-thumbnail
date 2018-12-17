# Getting Started

## Installing Pythumbnail

Pythumbnail requires Python 3 to run. Once you've installed Python 3, you can install Pythumbnail using pip:

    $ pip install pythumbnail

Depending on environment setup, you might need to use the following:

    $ python3 -m pip install pythumbnail

Or you can clone from github and manually install:
    
    $ git clone https://github.com/kevinyang372/py-thumbnail.git
    $ cd py-thumbnail
    $ python setup.py install

## Simple Example

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
file.scan()
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