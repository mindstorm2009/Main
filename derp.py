"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: YOUR NAME HERE
"""

from dataclasses import dataclass
from typing import Union


@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str


@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
############################################################################## 

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    if tokens != []:
        element = tokens.pop(0)
        if element.isdigit():
            return LiteralNode(int(element))
        elif element.isidentifier():
            return VariableNode(element)
        else:
            return MathNode(parse(tokens), element, parse(tokens))
    else:
        raise SyntaxError("Invalid token string")


##############################################################################
# infix
##############################################################################

def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if isinstance(node, LiteralNode):
        return node.val
    elif isinstance(node, VariableNode):
        return node.name
    else:
        return "(" + str(infix(node.left)) + " " + node.op + " " + str(infix(node.right)) + ")"


##############################################################################
# evaluate
##############################################################################    

def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    left = node.left
    right = node.right
    if isinstance(node.left, MathNode):
        left = evaluate(node.left, symTbl)
    if isinstance(node.right, MathNode):
        right = evaluate(node.right, symTbl)
    if node.op == "*":
        return multiply(left, right, symTbl)
    elif node.op == "//":
        return divide(left, right, symTbl)
    elif node.op == "+":
        return add(left, right, symTbl)
    elif node.op == "-":
        return subtract(left, right, symTbl)


##############################################################################
# main
##############################################################################
def create_symtbl(filename):
    file = open(filename)
    symtbl = {}
    for line in file:
        line = line.strip()
        values = line.split()
        symtbl[values[0]] = int(values[1])
    file.close()
    return symtbl


def display_symtbl(symTbl):
    print("Derping the Symbol Table (variable name => integer value)...")
    for keys in symTbl:
        print(keys, "=>", symTbl[keys])


def add(left, right, symTbl):
    if isinstance(left, VariableNode):
        left = symTbl[left.name]
    elif isinstance(left, LiteralNode):
        left = left.val
    if isinstance(right, VariableNode):
        right = symTbl[right.name]
    elif isinstance(right, LiteralNode):
        right = right.val
    return left + right


def subtract(left, right, symTbl):
    if isinstance(left, VariableNode):
        left = symTbl[left.name]
    elif isinstance(left, LiteralNode):
        left = left.val
    if isinstance(right, VariableNode):
        right = symTbl[right.name]
    elif isinstance(right, LiteralNode):
        right = right.val
    return left - right


def multiply(left, right, symTbl):
    if isinstance(left, VariableNode):
        left = symTbl[left.name]
    elif isinstance(left, LiteralNode):
        left = left.val
    if isinstance(right, VariableNode):
        right = symTbl[right.name]
    elif isinstance(right, LiteralNode):
        right = right.val
    return left * right


def divide(left, right, symTbl):
    if isinstance(left, VariableNode):
        left = symTbl[left.name]
    elif isinstance(left, LiteralNode):
        left = left.val
    if isinstance(right, VariableNode):
        right = symTbl[right.name]
    elif isinstance(right, LiteralNode):
        right = right.val
    return left / right


def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""

    print("Hello Herp, welcome to Derp v1.0 :)")

    inFile = input("Herp, enter symbol table file: ")
    symtbl = create_symtbl(inFile)
    display_symtbl(symtbl)
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
        prefixExp = prefixExp.strip()
        tokens = prefixExp.split()
        node = parse(tokens)
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", infix(node))
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", evaluate(node, symtbl))

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
