grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+ EOF;// write for program rule here using vardecl and funcdecl

// Variable declaration and function declaration
vardecl: DATA_TYPE (param)+ SEMI;

funcdecl: DATA_TYPE ID LB param_list? RB body;

// List of parameters
param_list: (DATA_TYPE (param)+) (SEMI (DATA_TYPE (param)+))*;

param: ID | COMMA ID;

DATA_TYPE: INT | FLOAT;

INT: 'int';

FLOAT: 'float';

body: LP (vardecl | stmt)* RP;

// 3 statements
stmt: (call | return_stmt | assign_stmt) SEMI;

call: ID LB list_of_expr? RB;

list_of_expr: (expr (COMMA expr)*);

return_stmt: 'return' expr;

assign_stmt: ID '=' expr;

expr: expr1 ADD expr | expr1;

expr1: expr2 SUBTRACT expr2 | expr2; 

expr2: expr2 (MULTIPLY | DIVISION) expr3 | expr3; 

expr3: LB expr3 RB | operands;

operands: ID | INTEGER_LITERAL | FLOAT_LITERAL | call;

ADD: '+';

SUBTRACT: '-';

MULTIPLY: '*';

DIVISION: '/';

FLOAT_LITERAL: (INTEGER_LITERAL)? DOT INTLIT;

INTEGER_LITERAL: '0' | [1-9][0-9]*;

INTLIT: [0-9]+;

ID: [a-zA-Z]+;

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';
DOT: '.';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;