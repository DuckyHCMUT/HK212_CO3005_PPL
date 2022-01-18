// Student ID: 1953097
grammar D96;

@lexer::header {
from lexererr import *
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 2: Program structure */

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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 3: Lexical Structure */

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
CLASS: 'class';
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
MULTIPLY : '*';
DIVIDE: '/';
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
EQUAL_STRING : '==.';
STRING_CONCAT : '+.';
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
LITERAL: 
	LITERAL_INT_DEC | LITERAL_INT_HEX | LITERAL_INT_OCT | LITERAL_INT_BIN | LITERAL_INT_BIN | LITERAL_FLOAT | LITERAL_STRING;

LITERAL_INT_DEC: SIGN? [1-9][0-9_]+ {self.text = self.text.replace('_','')}; // Need to work for non-duplicate underscores
LITERAL_INT_HEX: ('0x' | '0X')[1-9A-F_]+ {self.text = self.text.replace('_','')}; // Need to work for non-duplicate underscores
LITERAL_INT_OCT: ('0')(LITERAL_INT_DEC); // Just need to add a preceeding number zero by the normal decimal notation
LITERAL_INT_BIN: ('0b' | '0B')[01]+;

LITERAL_FLOAT: 
		SIGN? 
		(
			FLOAT_INT FLOAT_DECIMAL FLOAT_EXP? // Case 1: Has the first 2 components --> 1.2E10 or 1.2 only
		|	(FLOAT_INT | FLOAT_DECIMAL) FLOAT_EXP // Case 2: One of the first 2 components omitted, but not exp --> .2E10, 2E10, .E10
		)		
	; 

FLOAT_INT: '0' | [1-9][0-9_]+;
FLOAT_DECIMAL: DOT [0-9]*;
FLOAT_EXP: ('e' | 'E') SIGN? [1-9][0-9];

SIGN: [+-];

// Strings literal, delimited by double quotation marks, containing STRING_CHAR (string characters)
LITERAL_STRING: 
	'"' STRING_CHAR* '"'
	{ 
		y = str(self.text)
		self.text = y[1:-1]
	};

DOUBLE_QUOTE : ('\'"'); //Double quote inside a string literal

// Arrays
LITERAL_IDX_ARRAY: 'Array' LB (ARRAY_ELEMENT COMMA?)* RB;
LITERAL_MTD_ARRAY: 'Array' LB (LITERAL_IDX_ARRAY COMMA?)* RB;

ARRAY_ELEMENT: (LITERAL COMMA?)+;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 4: Types and Values */

// Section 4.1: Primitive types
data_types: primitive_types | array_types | class_types;	
primitive_types: BOOLEAN | INT | FLOAT | STRING;

// Section 4.2: Array types
array_types: ARRAY LS primitive_types COMMA ARRAY_BOUND RS SEMI; // calling array: Array [Int, 1-9]
ARRAY_BOUND: [1-9][0-9]+;

// Section 4.3: Class types
class_types: NEW ID LB RB; // New ABC()

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 5: Expression */
expr: expr1 (STRING_CONCAT | EQUAL_STRING) expr1 | expr1; // +., ==., - Binary - Infix - None

expr1: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ) expr2 | expr2; // ==, !=, <, >, <, =< >= - Binary - Infix - None

expr2: expr2 (AND | OR) expr3 | expr3; // &&, || - Binary - Infix - Left-assoc

expr3: expr3 (ADD | SUBTRACT) expr4 | expr4; // +, - - Binary - Infix - Left-assoc

expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5 ; // *, /, % - Binary - Infix - Left-assoc

expr5: (NOT expr5) | expr6; // ! -  Unary - Prefix - Right-assoc

expr6: (SUBTRACT expr6) | expr7; // (-) - Unary - Prefix - Right-assoc

expr7: (expr8 index_ops) | expr8 ; // [] - Unary - Postfix - Left-assoc

expr8: expr8 (DOT | SUPER_CLASS) expr9 | expr9; // . :: - Binary - Infix - Left-assoc

expr9: (NEW expr9) | operands; // New - Unary - Prefix - Right-assoc

operands: LITERAL | ID | LB expr RB;

// Section 5.1: Arithmetic operators
arithmetic_ops: SUBTRACT | ADD | MULTIPLY | DIVIDE | MODULO; // - + * / %

// Section 5.2: Boolean operators
boolean_ops: NOT | AND | OR | EQUAL_STRING; // ! && || ==.

// Section 5.3: String operators
string_ops: STRING_CONCAT; // +.

// Section 5.4: Relational operators
relational_ops: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ;

// Section 5.5: Index operators
element_expr: expr index_ops; // a + b(index_ops)
index_ops: LS expr RS index_ops?; // [3] or [a+2] or [a[b[c[3]]]

// Section 5.6: Member access
// 1. Instance attribute
instance_attr: expr DOT ID;

// 2. Static attribute
static_attr: ID SUPER_CLASS ID;

// 3. Instance method invocation
instance_method: expr DOT ID LB list_of_expr RB;

// 4. Static method invocation
static_method: ID SUPER_CLASS ID LB list_of_expr RB;

// Section 5.7: Object creation
object_create: NEW ID LB list_of_expr RB;

list_of_expr: (expr COMMA?)+;

// Section 5.8: Self
self: 'Self';

// Section 5.9: Operator precedence and associativity


// Section 5.10: Type coercions


// Section 5.11: Evaluation orders


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ALPHABET LB exp? RB;

// Errors and exceptions
ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STRING_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible_char = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible_char:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};

ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

fragment STRING_CHAR: ~[\b\f\r\n\t"'\\] | ESC_SEQUENCE ;
fragment ESC_SEQUENCE: '\\' [bfrnt"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[bfrnt"'\\] | ~'\\' ;



