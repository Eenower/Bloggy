if you have a [[Context-Free Grammers]] and a string of letters
parsing is to determine wheter a string is a word in the [[Languages]] and if it is finding a parse tree or derivation from this. so a parser is a program that does this. 

## LR Parser
- bottom up parser
- scans input left to right
- constructs a rightmost derivation in reverse
- implemented using a deterministic PDA
- not all CFG have such a parser