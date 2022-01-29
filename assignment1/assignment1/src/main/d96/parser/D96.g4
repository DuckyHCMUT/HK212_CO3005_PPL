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
/* Program structure */

class_decl: 
	('Class' class_name (COLON class_name)? LP class_body RP ); //ID: Serves as identifer

class_body: (class_attr | class_method)*;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// For class attributes

class_attr: (VAR | VAL) 
			(attr_no_value 
			| attr_with_value 
			| attr_array_no_value 
			| attr_array_with_value) 
			SEMI;

attr_no_value: any_id (COMMA any_id)* COLON data_type;

attr_with_value: any_id attr_pair all_expr; 
attr_pair: COMMA any_id attr_pair all_expr COMMA | COLON data_type ASSIGN; 

attr_array_no_value: any_id (COMMA any_id)* COLON attr_array_decl_tail;

attr_array_with_value: any_id attr_array_pair array_rhs; 
attr_array_pair: COMMA any_id attr_array_pair array_rhs COMMA | COLON attr_array_decl_tail ASSIGN; 
attr_array_decl_tail: ARRAY LS (data_type | attr_array_decl_tail) COMMA (LITERAL_INT) RS;

any_id: ID | DOLLAR_ID;

// Right-hand side of an array --> Check lower lines
// array_rhs: (literal_array | object_create all_expr?);
 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// For class methods

class_method: normal_method | constructor | destructor;

normal_method: any_id LB params_list? RB LP block_stmt? RP; 

constructor: CONSTRUCTOR LB params_list? RB LP block_stmt? RP; 

destructor: DESTRUCTOR LB RB LP block_stmt? RP;
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Statement lists
stmt: 
	var_decl
	| assign_stmt 
	| if_stmt
	| for_in_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invoc_literal DOT funcall SEMI
	| (SELF | ID) DOUBLE_COLON static_method SEMI
	| LP block_stmt? RP 
	;

// Variable declaration
var_decl: 	(VAR | VAL) 
			( var_no_value 
			| var_with_value 
			| var_array_no_value
			| var_array_with_value) 
			SEMI; 

var_no_value: ID (COMMA ID)* COLON data_type;

var_with_value: ID var_pair all_expr; 
var_pair: COMMA ID var_pair all_expr COMMA | COLON data_type ASSIGN; 

var_array_no_value: ID (COMMA ID)* COLON var_array_decl_tail;

var_array_with_value: ID var_array_pair array_rhs; 
var_array_pair: COMMA ID var_array_pair array_rhs COMMA | COLON var_array_decl_tail ASSIGN; 
var_array_decl_tail: ARRAY LS (data_type | var_array_decl_tail) COMMA (LITERAL_INT) RS;

array_rhs: (literal_array | object_create all_expr?);

// Assign statement, not clean
assign_stmt: assign_lhs ASSIGN all_expr SEMI;
assign_lhs: scalar_variable | scalar_variable element_expr;

params_list: params (SEMI params)*;

params : ID ((COMMA ID)* COLON (data_type | var_array_decl_tail)); // need array

data_type : INT | FLOAT | BOOLEAN | STRING | class_name;

// If statement
if_stmt: IF LB all_expr RB LP block_stmt? RP (else_if_body)? else_body?;
else_if_body: ELSEIF LB all_expr RB LP block_stmt? RP else_if_body?;
else_body: ELSE LP block_stmt? RP;

// Foreach-In statement
for_in_stmt: FOREACH LB for_in_body RB LP block_stmt? RP;
for_in_body: scalar_variable IN for_in_expr DOTDOT for_in_expr (BY for_in_expr)? ; 
for_in_expr: all_expr;

scalar_variable: scalar_variable DOT (ID | funcall)
				| static_member_access
				| SELF 
				| ID 
				;

// Break statement
break_stmt: BREAK SEMI;

// Continue statement
continue_stmt: CONTINUE SEMI;

// Return statement
return_stmt: RETURN all_expr* SEMI;

class_name: (ID | SELF); // An arbitrary name or Self keyword

// Method invocation
// A method invocation statement is an instance/static method invocation, that was described in subsection 5.6, with a semicolon at the end.
method_invoc_literal: method_invoc_literal DOT (ID | funcall) 
					| NEW funcall // New X().New
					| method_invoc_literal element_expr
					| static_member_access
					| SELF
					| ID
					;

method_invoc: method_invoc_literal | SEMI;

expr_list: (all_expr COMMA)* all_expr;

funcall: ID LB list_of_expr? RB;

// Block statement recursively called
block_stmt: (stmt)+;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Expression */

all_expr: (op | object_create); 

op: op1 (STRING_CONCAT | EQUAL_STRING) op1 | op1; // +., ==., - Binary - Infix - None

op1: op2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ) op2 | op2; // ==, !=, <, >, <, =< >= - Binary - Infix - None

op2: op2 (AND | OR) op3 | op3; // &&, || - Binary - Infix - Left-assoc

op3: op3 (ADD | SUBTRACT) op4 | op4; // +, - - Binary - Infix - Left-assoc

op4: op4 (MULTIPLY | DIVIDE | MODULO) op5 | op5 ; // *, /, % - Binary - Infix - Left-assoc

op5: (NOT op5) | op6; // ! -  Unary - Prefix - Right-assoc

op6: (SUBTRACT op6) | op7; // (-) - Unary - Prefix - Right-assoc

op7: op7 LS op7 RS | op8 ; // [] - Unary - Postfix - Left-assoc

op8: op8 DOT (ID | funcall) | op9; // . - Binary - Infix - Left-assoc

op9: (SELF | ID) DOUBLE_COLON (static_method | DOLLAR_ID) | op10; 

op10: (NEW operands LB list_of_expr? RB) | operands; // New - Unary - Prefix - Right-assoc

operands: literal | SELF | ID | LB op RB | NULL | literal_array; // Because member access can also return a value

// Section 5.5: Index operators
element_expr: index_ops; // a + b(index_ops)
index_ops: index_ops LS all_expr RS | LS all_expr RS; // [3] or [a+2] or a[1][2] or a[a[1]]

// Section 5.6: Member access
// static_member_access: static_attr | static_method;
static_member_access:
	(NEW funcall | SELF | ID) DOUBLE_COLON (
		DOLLAR_ID
		| static_method
	);

// 1. Instance attribute
instance_attr: DOT ID;

// 2. Static attribute
static_attr: DOUBLE_COLON DOLLAR_ID; // ::$a

// 3. Instance method invocation
instance_method: DOT ID LB list_of_expr? RB;

// 4. Static method invocation
static_method: DOLLAR_ID LB list_of_expr? RB;

// Section 5.7: Object creation
object_create: NEW ID LB list_of_expr? RB;

list_of_expr: op (COMMA op)*;

// Section 3.7: Literals
literal: LITERAL_INT | LITERAL_FLOAT | LITERAL_STRING | LITERAL_BOOLEAN | LITERAL_ZERO;

// Arrays
literal_array: literal_idx_array | literal_mtd_array;
literal_idx_array: 'Array' LB array_element RB;
literal_mtd_array: 'Array' LB (literal_idx_array COMMA?)* RB;

array_element: all_expr (COMMA all_expr)*;

LITERAL_BOOLEAN: TRUE | FALSE; 

LITERAL_INT: 
	(LITERAL_INT_DEC | LITERAL_INT_HEX | LITERAL_INT_OCT | LITERAL_INT_BIN)
	{self.text = self.text.replace('_','')};

LITERAL_ZERO: 
			  '0'                 // Decimal
			| '00'                // Octal
			| '0x0' | '0X0'       // Hexadecimal
			| '0b0' | '0B0'       // Binary
			;

LITERAL_INT_DEC: ([1-9] ('_'? [0-9])*); 

LITERAL_INT_HEX: ('0x' | '0X')([1-9A-F] ('_'? [0-9A-F])*) ;

LITERAL_INT_OCT: '0' [1-7] ('_'? [0-7])*; 
	
LITERAL_INT_BIN: ('0b' | '0B') ('1' ('_'? [01])*);

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

fragment FLOAT_INT: 
	'0' 
	|
	(
		[1-9] ('_'? [0-9])*
	);
fragment FLOAT_DECIMAL: DOT [0-9]*;
fragment FLOAT_EXP: [eE] [+-]? ([0-9]+);

// Strings literal, delimited by double quotation marks, containing STRING_CHAR (string characters)
LITERAL_STRING: 
	'"' (STRING_CHAR | DOUBLE_QUOTE | ESC_SEQUENCE)* '"'
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
NEW: 'New';
ELSEIF : 'Elseif';
ARRAY: 'Array';
STRING: 'String';
BY: 'By';
ELSE: 'Else';
IN: 'In';
RETURN : 'Return';
SELF: 'Self';

// Section 3.6: Seperators
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LP: '{';
RP: '}';
SEMI: ';';
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
DOUBLE_COLON : '::';
COLON: ':';

// Section 3.3: Identiiers
ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: STATIC [_a-zA-Z0-9]+;

// Section 3.2: Program comment
BLOCK_COMMENT : ('##' .*? '##') -> skip;

WS: [ \t\n\r\b\f]+ -> skip; // skip spaces, tabs, newlines

// Errors and exceptions
fragment STRING_CHAR: ~[\\"\n];

UNCLOSE_STRING: '"' (STRING_CHAR | ESC_SEQUENCE)* (EOF | '\n')
{
	content = str(self.text)
	esc = ['\n']
	if content[-1] in esc:
		raise UncloseString(content[1:-1])
	else:
		raise UncloseString(content[1:])
};

ILLEGAL_ESCAPE: '"' (STRING_CHAR | ESC_SEQUENCE)* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

// fragment ESC_SEQUENCE: '\\' [bfrnt'"\\] ;

fragment ESC_SEQUENCE: '\\b'
						| '\\f'
						| '\\r'
						| '\\n'
						| '\\t'
						| '\\\''
						| '\\\\'
						| '\'"';

fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\];

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};

