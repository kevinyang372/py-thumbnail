# Documentation

## Read File

To start scanning, you need to input the directory of python file.

```python
import pythumbnail

# reads in a new python file
file = pythumbnail.read_file('some_file.py')

# turns on logging mode (will output all state changes)
file = pythumbnail.read_file('some_file.py', silent = False) 

# customizes the keywords to capture (default: 'class', 'def', 'for', 'if', 'elif','else:', 'while')
file = pythumbnail.read_file('some_file.py', keys = ['for']) 
```

## Print Tree

Once the directory is successfully passed to Pythumbnail. You are able to print out tree structure of the Python file using *file.tree*

```python
# reads in a new python file
file = pythumbnail.read_file('some_file.py')

# print tree
print(file.tree)
```

## Search

You could also search for a specific function with *object.search('name')*

```python
# reads in a new python file
file = pythumbnail.read_file('some_file.py')

# search for a specific fucntion
some_function = file.search('some_name')

# print tree
print(some_function)
```

## Show Summary

Pythumbnail provides a dictionary containing the count of each function group

```python
# reads in a new python file
file = pythumbnail.read_file('some_file.py')

# show summary of the file
summary = file.show_summary()

# print summary
print(summary)
```

## Show Text File

Print the file

```python
# reads in a new python file
file = pythumbnail.read_file('some_file.py')

# get the file
file_text = file.show_text()

# print file
print(file_text)
```