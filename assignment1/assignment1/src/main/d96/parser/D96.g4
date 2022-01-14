grammar D96;

@lexer::header {
from lexererr import *
id = 1953097
}

options {
	language = Python3;
}

// Program's main structure
program: mptype 'main' LB RB LP body? RP EOF;

// Main program type (int or void)
mptype: INTTYPE | VOIDTYPE;

INTTYPE: 'int';
VOIDTYPE: 'void';

// Section 2.1: Class declaration
class_declaration: 
	('Class' ID LP class_body RP ); //ID: Serves as identifer

class_body: ID;

// Section 2.2: Attribute declaration
attribute: (immuttable | muttable) static? ':' data_type '=' data SEMI; //Integer

immuttable: 'Val';
muttable: 'Var';
static: '$';

data_type : 'Int'; // Not yet
data : ; // Not yet

// Section 2.3: Method declaration
method: static? ID LB params RB stmt; //stmt: Block of statement
constructor: 'Constructor' LB params RB stmt; //stmt: Block of statement
destructor: 'Destructor' LB RB stmt;

params : ('wtf')*; // Not yet
stmt: ; // Block of statement

// Section 3.1: Characters set
WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

// Section 3.2: Program comment
BLOCK_COMMENT : ('##' .*? '##') -> skip;

// Section 3.3: Identiiers: 
ALPHABET: [a-zA-Z_]+;

INTLIT: [0-9]+;

ID: ALPHABET ( ALPHABET [0-9] )*;

// Section 3.4: Keywords
BREAK: 'Break';
FOREACH: 'Foreach';
INT: 'Int';
NULL: 'Null';
CONSTRUCTOR: 'Constructor';
CONTINUE: 'Continue';
TRUE : 'True';
FLOAT: 'Float';
CLASS: 'Class';
DESTRUCTOR: 'Destructor';
IF: 'If';
FALSE: 'False';
BOOLEAN: 'Boolean';
VAL: 'Val';
NEW: 'New';
ELSEIF : 'Elseif';
ARRAY: 'Array';
STRING: 'String';
VAR: 'Var';
BY: 'By';
ELSE: 'Else';
IN: 'In';
RETURN : 'Return';

// Section 3.5: Operators
ADD: '+';
SUBTRACT : '-';
MULTIPLY : '/';
MODULO : '%';
NOT : '!';
AND : '&&';
OR : '||';
EQUAL : '==';
ASSIGN : '=';
NOT_EQUAL : '!=';
LESS_THAN : '<';
LEQ : '<=';
GREATER_THAN : '>';
GEQ : '>=';
EQUAL_WHAT : '==.';
DOT : '.';
SUPER_CLASS : '::';
// NEW : 'New'; --> Duplicate from the keyword

// Section 3.6: Seperators
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LP: '{';
RP: '}';
SEMI: ';';
// DOT: '.'; --> Duplicate from the operator
COMMA : ',';

// Section 3.7: Literals
LITERAL_INT_DEC: [1-9][0-9_]+ {self.text = self.text.replace('_','')}; // Need to work for non-duplicate underscores
LITERAL_INT_HEX: ('0x' | '0X')[1-9A-F_]+ {self.text = self.text.replace('_','')}; // Need to work for non-duplicate underscores
LITERAL_INT_OCT: ('0')(LITERAL_INT_DEC); // Just need to add a preceeding number zero by the normal decimal notation
LITERAL_INT_BIN: ('0b' | '0B')[01]+;
LITERAL_STRING: ["](ALPHABET | INTLIT)*["];
LITERAL_IDX_ARRAY: 'Array' LB RB;
LITERAL_MTD_ARRAY: 'Array' LB (LITERAL_IDX_ARRAY COMMA?)* RB;

DOUBLE_QUOTE : ('\'"');

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ALPHABET LB exp? RB;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .{raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};


