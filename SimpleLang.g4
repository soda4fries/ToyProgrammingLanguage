grammar SimpleLang;

program: (functionDecl | statement)* EOF;

functionDecl
    : 'func' IDENTIFIER '(' paramList? ')' '->' type block
    ;

paramList
    : parameter (',' parameter)*
    ;

parameter
    : IDENTIFIER ':' type ('=' expr)?
    ;

type: 'int' | 'bool' | 'string' | 'float' | arrayType | listType;

arrayType: 'array' '<' type '>' ;
listType: 'list' '<' type '>' ;

block: '{' statement* '}' ;

statement
    : varDecl 
    | assignment 
    | functionCall ';'
    | returnStmt 
    | ifStatement
    | commentStmt
    | arrayOp 
    | listOp 
    | matrixOp 
    | whileStatement
    | block
    | matchStatement
    ;

varDecl: 'let' IDENTIFIER ':' type ('=' expr)? ';' ;

assignment: IDENTIFIER ('['expr']')? '=' expr ';' ;

arrayOp: IDENTIFIER '.' (
    'sort' '(' ('desc')? ')' |
    'mean' '(' ')' |
    'median' '(' ')' |
    'variance' '(' ')' |
    'stddev' '(' ')' |
    'play' '(' ')' |
    'linreg' '(' expr ')' |
    'rotate' '(' expr ')' |
    'shift' '(' expr ')' |
    'filter' '(' lambdaExpr ')' |
    'map' '(' lambdaExpr ')'

) ';' ;

lambdaExpr: IDENTIFIER '=>' expr ;

listOp: IDENTIFIER '.' ('append' '(' expr ')' | 'remove' '(' expr ')' | 'sort' '(' ')') ';' ;

matrixOp
    : IDENTIFIER '.' ('add' '(' expr ')' | 'multiply' '(' expr ')' | 'invert' '(' ')' | 'transpose' '(' ')') ';'
    ;

matchStatement
    : 'match' expr '{' matchCase+ '}'
    ;

matchCase
    : 'case' pattern '=>' statement
    ;

pattern
    : INT
    | FLOAT
    | BOOL
    | STRING
    | IDENTIFIER
    | '_'
    | '[' pattern (',' pattern)* ']'
    | '{' IDENTIFIER ':' pattern (',' IDENTIFIER ':' pattern)* '}'
    ;

ifStatement
    : 'if' '(' expr ')' block ('else' block)?
    ;

whileStatement
    : 'while' '(' expr ')' block
    ;

returnStmt: 'return' expr? ';' ;

commentStmt
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;

MOD: '%';

expr
    : functionCall
    | primary
    | '-' expr
    | expr '[' expr ']'
    | expr op=('*'|'/'|MOD) expr
    | expr op=('+'|'-') expr
    | expr op=('>'|'<'|'>='|'<='|'=='|'!=') expr
    | expr op=('and'|'or') expr
    | '[' (expr (',' expr)*)? ']'
    | '(' expr ')'
    ;

functionCall: IDENTIFIER '(' (expr (',' expr)*)? ')' ;

primary
    : INT
    | FLOAT
    | BOOL
    | STRING
    | IDENTIFIER
    ;

SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;

INT: '-'? [0-9]+;
FLOAT: '-'? [0-9]+ '.' [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n] | '\\"')* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;