

### Shift-reduce parser
this LR parser has
- a stack terminals and non terminals processes so far
- a buffer the rest of the input string yet to be processes
	- at first containing the entire input string

- shift input letters onto the stack OR
- when a string of top most stack symbols equal the right hand side of the production rule
	- reduce that string so use the production rule in reverse
do this until the stack has onlyh a start symbol and the buffer is empty

![[Pasted image 20231026140448.png]]


THe order you shift and reduce doesnt really matter but shift reduce conflct 

### [[Unix]] tools
- [[yacc]]
- [[Lex]]
- 