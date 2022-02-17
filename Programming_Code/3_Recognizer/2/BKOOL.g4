grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+ EOF;// write for program rule here using vardecl and funcdecl

vardecl: DATA_TYPE (param)+ SEMI;

funcdecl: DATA_TYPE ID LB param_list? RB body;

param_list: (DATA_TYPE (param)+) (SEMI (DATA_TYPE (param)+))*;

param: ID | COMMA ID;

DATA_TYPE: INT | FLOAT;

INT: 'int';

FLOAT: 'float';

body: 'body';

ID: [a-zA-Z]+;

INTLIT: [0-9]+;

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;