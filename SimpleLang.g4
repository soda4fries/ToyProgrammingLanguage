grammar SimpleLang;

program: expr* EOF;

expr
    : functionDecl
    | varDecl
    | assignment
    | ifExpr
    | block
    | functionCall
    | primary
    | '-' expr
    | 'not' expr
    | typeCast
    | expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | expr op=('>'|'<'|'>='|'<='|'=='|'!=') expr
    | expr op=('and'|'or') expr
    | ';'
    | '(' expr ')'
    ;

functionDecl
    : 'func' IDENTIFIER '(' paramList? ')' '->' Type block
    ;

paramList
    : parameter (',' parameter)*
    ;

parameter
    : IDENTIFIER ':' Type ('=' expr)?
    ;

Type
    : 'Int'
    | 'Float'
    | 'Bool'
    | 'String'
    | 'Void'
    ;

block
    : '{' expr* '}'
    ;

varDecl
    : 'let' IDENTIFIER ':' Type ('=' expr)?
    ;

assignment
    : IDENTIFIER '=' expr
    | IDENTIFIER assignOp expr
    ;

assignOp
    : '+=' | '-=' | '*=' | '/='
    ;

ifExpr
    : 'if' '(' expr ')' block ('else' block)?
    ;

typeCast
    : Type '(' expr ')'
    ;

functionCall
    : IDENTIFIER '(' (expr (',' expr)*)? ')'
    ;

primary
    : INT
    | FLOAT
    | BOOL
    | STRING
    | IDENTIFIER
    ;

FLOAT: '-'? [0-9]+ '.' [0-9]+;
INT: '-'? [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n] | '\\"')* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;