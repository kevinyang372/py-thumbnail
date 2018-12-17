# How it Works:

Pythumbnail parses python files on two levels. On the higher level, it detects the key identifiers at the beginning of the line (e.g. def, for, if...). It also keeps track of the number of indentations to construct the inheritance relationship between different lines. When the key identifier is found, it passes the string of that line to the lower level parser, which utilizes finite state machine to further divide it into function group names, logical operators and parameters.

!!! Tip "Finite State Machine"

    A finite state machine (sometimes called a finite state automaton) is a computation model that can be implemented with hardware or software and can be used to simulate sequential logic and some computer programs. Finite state automata generate regular languages. Finite state machines can be used to model problems in many fields including mathematics, artificial intelligence, games, and linguistics.

Pythumbnail generates finite state machine maps for three different types of function group: function, for loop and while/if statement.

## FSM for Functions

![Finite State Machine for DEF](img/Def_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences

## FSM for For Loops

![Finite State Machine for FOR](img/For_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_LOGIC*: &nbsp;&nbsp;defining logical relationships<br>
*S_STRING*: &nbsp;&nbsp;inputing information into a string (spaces do not cause state changes)<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences

## FSM for While/If Statements

![Finite State Machine for FOR](img/WhileIf_FSM.png)

** FSM States: **

*S_NAME*: &nbsp;&nbsp;defining name of the function<br>
*S_PARA*: &nbsp;&nbsp;defining parameters of the function<br>
*S_COMMA*: &nbsp;&nbsp;adding new parameters<br>
*S_LOGIC*: &nbsp;&nbsp;defining logical relationships<br>
*S_STRING*: &nbsp;&nbsp;inputing information into a string (spaces do not cause state changes)<br>
*S_END_RULE*: &nbsp;&nbsp;end of sentences


