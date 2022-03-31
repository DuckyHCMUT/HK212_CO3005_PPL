grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: array_type EOF;

array_type: ARRAY LS domain_list RS OF data_type;

data_type: INTTYPE | FLOATTYPE | array_type;

domain_list: domain+;
domain: (INT DOTDOT INT) | (INT DOTDOT INT COMMA domain); 

INTTYPE: 'int';	

FLOATTYPE: 'float';

INT: SUB? ('0' | [1-9][0-9]*);
SUB: '-';
ARRAY: 'array';
OF: 'of';
LS: '[';
RS: ']';
COMMA: ',';
DOTDOT: '..';


STRING : ["]["] (["] STRING_CHAR | STRING_CHAR)* ["]["];

fragment STRING_CHAR: ~["];

WS: [ \t\n]+ -> skip;

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: .;

ILLEGAL_ESCAPE: .;