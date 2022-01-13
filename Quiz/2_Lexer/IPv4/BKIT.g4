grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

fragment DIGIT: [0-9];
fragment NATURAL_DIGIT: [1-9]; 
fragment IP_COMPONENT: [0] | (NATURAL_DIGIT)(DIGIT)?(DIGIT)?;

IPV4: (IP_COMPONENT)[.](IP_COMPONENT)[.](IP_COMPONENT)[.](IP_COMPONENT);

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: .;

ILLEGAL_ESCAPE: .;