# How it Works

Pythumbnail parses python files on two levels. On the higher level, it detects the key identifiers at the beginning of the line (e.g. def, for, if...). It also keeps track of the number of indentations to construct the inheritance relationship between different lines. When the key identifier is found, it passes the string of that line to the lower level parser, which utilizes finite state machine to further divide it into function group names, logical operators and parameters.

!!! Tip "Finite State Machine"

    A finite state machine (sometimes called a finite state automaton) is a computation model that can be implemented with hardware or software and can be used to simulate sequential logic and some computer programs. Finite state automata generate regular languages. Finite state machines can be used to model problems in many fields including mathematics, artificial intelligence, games, and linguistics.

Pythumbnail generates finite state machine maps for three different types of function group: function, for loop and while/if statement.

## Time Complexity Analysis

Although the commonly used recursive approach in parsing is able to maintain an O(N) time complexity handling simple logic like maths equations, its complexity grows quickly as the objective complicates when parsing normal Python expressions. At the same time, however, with the limited number of states in FSM, a combination of higher level tree traversal and finite state machine could always maintain the time complexity at O(N).

The time complexity of the algorithm is tested using the code below:

```python
    def write_line(directory,i):
        with open (directory, "w") as myfile:
            for i in range(100*i):
                myfile.write('def yes(par1, par2):\n')
                myfile.write('\n')
            myfile.close()
            
    times = []
    for i in range(100):
        write_line(directory, i)
        start_time = time.time()
        pythumbnail.read_file(directory, silent=False)
        times.append(time.time() - start_time)
        
    plt.plot(range(0,10000,100),times)
    plt.xlabel("number of lines in the code")
    plt.ylabel("time")
    plt.show()
```

![Time Complexity](img/Time_FSM.png)

As shown in the graph, although there are small fluctuations, the overall time complexity is increasing in a linear manner.

## FSM for Functions

![Finite State Machine for DEF](img/Def_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences

There are four different states in a function (def) statement. The sequential logic starts with stating the name of the function (S_NAME). Then the left parenthesis marks the end of function name state and start of parameter definition state (S_PARA). Individual parameters are separated by commas (S_COMMA). The sequential logic ends with a right parenthesis (S_END_RULE).

## FSM for For Loops

![Finite State Machine for FOR](img/For_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_LOGIC*: &nbsp;&nbsp;defining logical relationships<br>
*S_STRING*: &nbsp;&nbsp;inputing information into a string (spaces do not cause state changes)<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences

For loop has six different states. The sequential logic starts with defining the name of variables (S_NAME). Individual variables are separated by commas (S_COMMA). " in " marks the logical operator (S_LOGIC) followed by an iterable (S_PARA). The sequential logic ends with a colon (S_END_RULE). Note that an additional string stage (S_STRING) is defined here to avoid triggering the mis-transition from S_NAME to S_LOGIC with spaces in a string.

## FSM for While/If Statements

![Finite State Machine for FOR](img/WhileIf_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_LOGIC*: &nbsp;&nbsp;defining logical relationships<br>
*S_STRING*: &nbsp;&nbsp;inputing information into a string (spaces do not cause state changes)<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences

While/If statement has six different states. The sequential logic starts with defining the name of variables (S_NAME). The difference with for loop here is while/if could end directly with S_NAME when the variable is a boolean. Individual variables are separated by commas (S_COMMA). "</>/=/in/not/and/or..." marks the logical operator (S_LOGIC) followed by another variable(S_PARA). The sequential logic ends with a colon (S_END_RULE). Note that an additional string stage (S_STRING) is defined here to avoid triggering the mis-transition from S_NAME to S_LOGIC with spaces in a string.

## Next Step

Given that Finite State Machine is able to parse python language down to key components like function name, logical operators and parameters. It should also be able to reverse engineer it and create python codes from the key information feeds to the algorithm. That would greatly simply the process of python programming where a higher level processor could be built on top of the python compiler.
