// Student ID: 1953097
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Program's main structure
program: (class_decl)+ EOF;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 2: Program structure */

// Section 2.1: Class declaration
class_decl: 
	('Class' ID (COLON ID)? LP class_body RP ); //ID: Serves as identifer

class_body: (class_attr | class_method)*;

class_attr: (VAR | VAL) ID COLON data_type SEMI;
class_method: normal_method | constructor | destructor;

normal_method: STATIC? ID LB params_list? RB LP block_stmt? RP; 
constructor: 'Constructor' LB params_list? RB LP block_stmt? RP {print("text")}; 
destructor: 'Destructor' LB RB LP block_stmt? RP;

params_list: params (SEMI params)*;

params : ID (COMMA ID)* COLON data_type;

data_type : INT | FLOAT | BOOLEAN | STRING;

// Section 4.3: Class types
class_types: ID; // ABC

// Section 6: Statements
// Section 6.1: Variable and constant declaration statement
stmt: 
	(var_decl
	| assign_stmt
	| if_stmt
	| for_in_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invoc
	| (LP block_stmt RP))
	;

var_decl: (VAR | VAL) (decl_tail | array_decl_tail);
decl_tail: 
	(ID COMMA)* ID COLON (data_type) ASSIGN (expr_tail)? SEMI;
array_decl_tail: 
	(ID COMMA)* ID COLON (array_type) SEMI;
object_decl: NEW ID LB RB;

expr_tail: (expr COMMA)* expr; 

array_type: (array_type_tail COMMA)* array_type_tail;

array_type_tail:
	(ARRAY LS data_type COMMA LITERAL_INT_DEC RS); //Array[Int, 5];

assign_stmt: assign_lhs ASSIGN expr SEMI;
assign_lhs: element_expr | ID;

if_stmt: if_body SEMI;
if_body: IF expr else_if_body ELSE LP block_stmt? RP;
else_if_body: (ELSEIF expr LP block_stmt? RP)*;

for_in_stmt: FOREACH for_in_body SEMI;
for_in_body: LB ID IN for_in_expr DOTDOT for_in_expr (BY for_in_expr)? RB;
for_in_expr: LITERAL_INT_DEC; // from -999999.... to 999999.... anything~

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN (expr)? SEMI;

// A method invocation statement is an instance/static method invocation, that was described in subsection 5.6, with a semicolon at the end.
method_invoc: ID (DOT | DOUBLE_SEMI) STATIC? ID LB expr_list? RB SEMI;  
expr_list: (expr COMMA)* expr;

block_stmt: (stmt)+;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 3: Lexical Structure */
// Arrays
literal_idx_array: 'Array' LB (array_element COMMA?)* RB;
literal_mtd_array: 'Array' LB (literal_idx_array COMMA?)* RB;

array_element: (LITERAL COMMA?)+;

/* Section 5: Expression */
expr: expr1 (STRING_CONCAT | EQUAL_STRING) expr1 | expr1; // +., ==., - Binary - Infix - None

expr1: expr2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ) expr2 | expr2; // ==, !=, <, >, <, =< >= - Binary - Infix - None

expr2: expr2 (AND | OR) expr3 | expr3; // &&, || - Binary - Infix - Left-assoc

expr3: expr3 (ADD | SUBTRACT) expr4 | expr4; // +, - - Binary - Infix - Left-assoc

expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5 ; // *, /, % - Binary - Infix - Left-assoc

expr5: (NOT expr5) | expr6; // ! -  Unary - Prefix - Right-assoc

expr6: (SUBTRACT expr6) | expr7; // (-) - Unary - Prefix - Right-assoc

expr7: (expr8 index_ops) | expr8 ; // [] - Unary - Postfix - Left-assoc

expr8: expr8 (DOT | DOUBLE_SEMI) expr9 | expr9; // . :: - Binary - Infix - Left-assoc

expr9: (NEW expr9) | operands; // New - Unary - Prefix - Right-assoc

operands: LITERAL | ID | LB expr RB ;

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
static_attr: ID DOUBLE_SEMI ID;

// 3. Instance method invocation
instance_method: expr DOT ID LB list_of_expr RB;

// 4. Static method invocation
static_method: ID DOUBLE_SEMI ID LB list_of_expr RB;

// Section 5.7: Object creation
object_create: NEW ID LB list_of_expr RB;

list_of_expr: (expr COMMA?)+;

// Section 3.7: Literals
LITERAL: 
	((LITERAL_INT_DEC | LITERAL_INT_HEX | LITERAL_INT_OCT | LITERAL_INT_BIN | LITERAL_INT_BIN | LITERAL_FLOAT)
	{self.text = self.text.replace('_','')})
	| 
	(LITERAL_STRING)
	;

LITERAL_INT_DEC: 
	(
		'0' 
		|
		([1-9] ('_'? [0-9])*)
	){self.text = self.text.replace('_','')}; 

LITERAL_INT_HEX: 
	('0x' | '0X')
	(
		'0' 
		| 
		[1-9A-F] ('_'? [0-9A-F])*
	) 
	{self.text = self.text.replace('_','')}; // Need to work for non-duplicate underscores
LITERAL_INT_OCT: 
	(
		'0'
	)
		('0' // Number zero in octal (00) 
		| 
			([1-7] ('_'? [0-7])*
		)
	)
	{self.text = self.text.replace('_','')}; // Just need to add a preceeding number zero by the normal decimal notation
LITERAL_INT_BIN: ('0b' | '0B')('0' | ('1' [01]*));

LITERAL_FLOAT: 
		(
			(FLOAT_INT FLOAT_DECIMAL FLOAT_EXP?) // Case 1: Has the first 2 components --> 1.2E10 or 1.2 only
		|
		// Case 2: Decimal part omitted --> 2E-10, 2E10
		// Case 3: Integer part omitted --> .E3, .E-5 
			(FLOAT_INT FLOAT_EXP)
		|
			(FLOAT_DECIMAL FLOAT_EXP) 
		)
		{self.text = self.text.replace('_','')};
		// {print("here")}; 

fragment FLOAT_INT: 
	'0' 
	|
	(
		[1-9] ('_'? [0-9])*
	);
fragment FLOAT_DECIMAL: DOT [0-9]*;
fragment FLOAT_EXP: [eE] [+-]? [1-9] [0-9]*;

// Strings literal, delimited by double quotation marks, containing STRING_CHAR (string characters)
LITERAL_STRING: 
	'"' STRING_CHAR* '"'
	{ 
		y = str(self.text)
		self.text = y[1:-1]
	};

DOUBLE_QUOTE : ('\'"'); //Double quote inside a string literal

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Section 3.4: Keywords
VAL: 'Val';
VAR: 'Var';
STATIC: '$';
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
// VAL: 'Val';
NEW: 'New';
ELSEIF : 'Elseif';
ARRAY: 'Array';
STRING: 'String';
// VAR: 'Var';
BY: 'By';
ELSE: 'Else';
IN: 'In';
RETURN : 'Return';
// SELF: 'Self';

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
DOTDOT: '..';

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
DOUBLE_SEMI : '::';
COLON: ':';
// NEW : 'New'; --> Duplicate from the keyword

// Section 3.3: Identiiers: 
ID: STATIC? [_a-zA-Z][_a-zA-Z0-9]*;

fragment INTLIT: [0-9][1-9]*;

WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

// Section 3.2: Program comment
BLOCK_COMMENT : ('##' .*? '##') -> skip;

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



