grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+;// write for program rule here using vardecl and funcdecl

vardecl: 'vardecl';

funcdecl: 'funcdecl';

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;