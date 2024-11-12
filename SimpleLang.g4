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

type: 'int' | 'bool' | 'string';

block: '{' statement* '}';

statement
    : varDecl ';'
    | assignment ';'
    | functionCall ';'
    | returnStmt ';'
    | ifStatement
    | commentStmt
    ;

varDecl
    : 'let' IDENTIFIER ':' type ('=' expr)?
    ;

assignment
    : IDENTIFIER '=' expr
    ;

ifStatement
    : 'if' '(' expr ')' block ('else' block)?
    ;

returnStmt
    : 'return' expr?
    ;

commentStmt
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;

expr
    : functionCall
    | primary
    | '-' expr
    | expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | expr op=('>'|'<'|'>='|'<='|'=='|'!=') expr
    | expr op=('and'|'or') expr
    | '(' expr ')'
    ;

functionCall
    : IDENTIFIER '(' (expr (',' expr)*)? ')'
    ;

primary
    : INT
    | BOOL
    | STRING
    | IDENTIFIER
    ;

SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;

INT: '-'? [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n] | '\\"')* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;