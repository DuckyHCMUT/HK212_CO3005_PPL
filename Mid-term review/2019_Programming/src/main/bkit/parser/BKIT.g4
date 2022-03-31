grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: expr EOF;

expr: expr '?' expr1 | expr1; 
expr1: expr2 '^' expr2 | expr2;
expr2: expr3 '@' expr2 | expr3;
expr3: LP expr RP | INT | ID | element_op;

element_op: ID LB expr RB | element_op LB expr RB;

LP: '(';
RP: ')';
LB: '[';
RB: ']';

INT: '0' | [1-9][0-9]*;

ID: [a-z][a-zA-Z0-9_]*;

// DATE: DAY DASH MONTH DASH YEAR;

// fragment DAY: [0][1-9] | [1-2][0-9] | [3][0-1];
// fragment MONTH: [0][1-9] | [1][0-2];
// fragment YEAR: ('19' | '20')[0-9][0-9];
// fragment DASH: '/';

WS: [ \t\n]+ -> skip;

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: .;

ILLEGAL_ESCAPE: .;