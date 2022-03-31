grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: struct EOF;

struct: STRUCT LB mem+ RB;

mem: data_type ID (COMMA ID)* SEMI;

data_type: INTTYPE | FLOATTYPE | struct;

STRUCT: 'struct';

INTTYPE: 'int';

FLOATTYPE: 'float';

LB: '{';

RB: '}';

ID: [a-z][a-zA-Z0-9_]*;

COMMA: ',';

SEMI: ';';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
