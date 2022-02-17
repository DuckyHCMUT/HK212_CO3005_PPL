grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment NATURAL_DIGIT: [1-9]; 

REAL: SIGN?DIGIT+([.]DIGIT+)?([e]*SIGN?DIGIT+)?;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: .;

ILLEGAL_ESCAPE: .;