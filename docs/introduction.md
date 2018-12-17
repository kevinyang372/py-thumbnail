# Introduction

Pythumbnail is a Python 3 library created for quick access to the content of python files. As a developer, you may have encountered many badly written codes with messy indentations, long nested for loops and missing comments. It is a painful experience to read through these codes trying to understand what is going on in there. 

Pythumbnail is made for those hard situations. Using less than three lines of code, you will be able to see the overall tree structure of the code, get quick access to the parameters required in each function, and understand how different function groups (for loop, class, if statement...) are related to each other. It also provides more advanced search and summary functions that allow you to dig deeper into specific part of the code or get a summary of function group countings.

The library utilizes finite state machine (FSM) for language parsings with the time complexity of O(N), which helps it to remain a fast scanning speed even for long python files.

!!! note

    Pythumbnail is officially beta software. There will be occasional changes that break backward compatibility. Reporting of bugs and update suggestions are very welcomed!