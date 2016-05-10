# simple-pythone
Simplest simulation model of using broadcast for a group of nodes to vote on an issue

## Usage instructions
- Pull the code, you should have two files:
  * __mobilephone.py__  : defines the class for the nodes
  * __simdriver.py__    : defines the main program to run which constructs the nodes, generates the question, generates responses, etc.
  
- Run:
`python simdriver.py 10 2` , where `10` is the number of nodes we want to create, and `2` is the number of options the questions have.

- At the end of the calculation you will receive output like this:
``` 
Key, count 1 3 
Key, count 2 7 
```
Key 2 wins here, because it has 7 votes over 3.

- Folders will be creates in the *Testdata*  directory. It will contain information respective to each node.
