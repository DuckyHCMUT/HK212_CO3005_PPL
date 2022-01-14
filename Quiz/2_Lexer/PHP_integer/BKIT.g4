grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

PHP_ID : '0' | [1-9][0-9_]* {self.text = self.text.replace('_','')};

WS: [ \t\n]+ -> skip;

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: .;

ILLEGAL_ESCAPE: .;