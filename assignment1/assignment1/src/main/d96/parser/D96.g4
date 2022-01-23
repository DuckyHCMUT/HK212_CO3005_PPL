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
	('Class' class_name (COLON class_name)? LP class_body RP ); //ID: Serves as identifer

class_body: (class_attr | class_method)*;

class_attr: var_decl;
class_method: normal_method | constructor | destructor;

normal_method: ID LB params_list? RB LP block_stmt? RP; 
constructor: CONSTRUCTOR LB params_list? RB LP block_stmt? RP; 
destructor: DESTRUCTOR LB RB LP block_stmt? RP;

params_list: params (SEMI params)*;

params : ID (COMMA ID)* COLON data_type;

data_type : INT | FLOAT | BOOLEAN | STRING | class_name;

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
	| method_invoc) 
	;

var_decl: (VAR | VAL) (pair_list | pair_list_arr) SEMI; //(decl_tail | array_decl_tail);

pair_list: ID pair all_expr?; // myVar (, myVar1(, myVar2 (, myVar3(: Int =) 100,) 200,) 300,) 400 

pair: COMMA ID pair (all_expr COMMA)? | COLON data_type ASSIGN?; 

pair_list_arr: ID pair_arr array_decl_tail; // myArr (, myArr1 (, myArr2 (, myArr3(:) Array[Int, 5],) Array[Int, 100],) Array[String, 4],) Array[Float, 2]

pair_arr: COMMA ID pair_arr array_decl_tail COMMA | COLON;

// array_decl_tail: ARRAY LS (data_type | ARRAY) COMMA LITERAL_INT_DEC RS; // Can be primitive or array type

array_decl_tail: ARRAY LS (data_type | ARRAY) COMMA 
	(LITERAL_INT) RS; // Can be primitive or array type

object_decl: NEW ID LB RB;

expr_tail: (all_expr COMMA)* all_expr; 

// Assign statement
// Some situations may appear as follow:
// a = expr;
// Self.a = expr;
// a.b.c = expr;

assign_stmt: (((class_name DOT)? (ID DOT)*) ID | element_expr) ASSIGN all_expr SEMI;


// If statement
if_stmt: IF LB all_expr RB LP block_stmt? RP (else_if_body)?;

else_if_body: ELSEIF LB all_expr RB LP block_stmt? RP else_if_body?;

// For-in statement
for_in_stmt: FOREACH LB for_in_body RB LP block_stmt RP;
for_in_body: ID IN for_in_expr DOTDOT for_in_expr (BY for_in_expr)? ;
for_in_expr: SUBTRACT? LITERAL_INT; // from -999999.... to 999999.... anything~

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN all_expr* SEMI;

class_name: (ID | SELF); // An arbitrary name or Self keyword

// A method invocation statement is an instance/static method invocation, that was described in subsection 5.6, with a semicolon at the end.
// method_invoc: ID (DOT | DOUBLE_SEMI) STATIC? ID LB expr_list? RB SEMI;  
method_invoc: (instance_method | static_method ) SEMI;
expr_list: (all_expr COMMA)* all_expr;

block_stmt: (stmt)+;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Section 3: Lexical Structure */
// Arrays
literal_idx_array: 'Array' LB (array_element COMMA?)* RB;
literal_mtd_array: 'Array' LB (literal_idx_array COMMA?)* RB;

array_element: (literal COMMA?)+;

/* Section 5: Expression */

all_expr: (op | member_access | object_create); 

op: op1 (STRING_CONCAT | EQUAL_STRING) op1 | op1; // +., ==., - Binary - Infix - None

op1: op2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ) op2 | op2; // ==, !=, <, >, <, =< >= - Binary - Infix - None

op2: op2 (AND | OR) op3 | op3; // &&, || - Binary - Infix - Left-assoc

op3: op3 (ADD | SUBTRACT) op4 | op4; // +, - - Binary - Infix - Left-assoc

op4: op4 (MULTIPLY | DIVIDE | MODULO) op5 | op5 ; // *, /, % - Binary - Infix - Left-assoc

op5: (NOT op5) | op6; // ! -  Unary - Prefix - Right-assoc

op6: (SUBTRACT op6) | op7; // (-) - Unary - Prefix - Right-assoc

op7: (op8 index_ops) | op8 ; // [] - Unary - Postfix - Left-assoc

op8: op8 (DOT | DOUBLE_COLON) op9 | op9; // . :: - Binary - Infix - Left-assoc

op9: (NEW op9) | operands; // New - Unary - Prefix - Right-assoc

operands: literal | ID | LB op RB | NULL | member_access; // Because member access can also return a value

// Section 5.1: Arithmetic operators
arithmetic_ops: SUBTRACT | ADD | MULTIPLY | DIVIDE | MODULO; // - + * / %

// Section 5.2: Boolean operators
boolean_ops: NOT | AND | OR | EQUAL_STRING; // ! && || ==.

// Section 5.3: String operators
string_ops: STRING_CONCAT; // +.

// Section 5.4: Relational operators
relational_ops: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ;

// Section 5.5: Index operators
element_expr: all_expr index_ops; // a + b(index_ops)
index_ops: LS all_expr RS index_ops?; // [3] or [a+2] or [a[b[c[3]]]

// Section 5.6: Member access
member_access: instance_attr | static_attr | instance_method | static_method;
// 1. Instance attribute
instance_attr: class_name DOT ID;

// 2. Static attribute
static_attr: ID DOUBLE_COLON ID;

// 3. Instance method invocation
instance_method: (class_name DOT)? instance_method_tail;
instance_method_tail: ID LB list_of_expr? RB;

// 4. Static method invocation
static_method: (ID DOUBLE_COLON)? ID LB list_of_expr? RB;

// Section 5.7: Object creation
object_create: NEW ID LB list_of_expr? RB;

list_of_expr: (op COMMA?)+;

// Section 3.7: Literals
literal: LITERAL_INT | LITERAL_FLOAT | LITERAL_STRING;

LITERAL_INT: 
	(LITERAL_INT_DEC | LITERAL_INT_HEX | LITERAL_INT_OCT | LITERAL_INT_BIN | LITERAL_INT_BIN)
	{self.text = self.text.replace('_','')};

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
// NEW : 'New'; --> Duplicate from the keyword

// Section 3.3: Identiiers: 
ID: STATIC? [_a-zA-Z][_a-zA-Z0-9]*;

// Section 3.2: Program comment
BLOCK_COMMENT : ('##' .*? '##') -> skip;

WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

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

// Errors and exceptions
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};



