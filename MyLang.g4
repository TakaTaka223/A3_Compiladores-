grammar MyLang;

// === Parser rules ===
program    : statement* EOF ;

statement
    : varDecl
    | assignment
    | ifStmt
    | whileStmt
    | ioStmt
    | block
    | ';'
    ;

// declaração de variável
varDecl    : 'var' ID ':' type ( '=' expr )? ';' ;

// atribuição
assignment : ID '=' expr ';' ;

// condicional
ifStmt     : 'se' '(' expr ')' 'entao' statement ('senao' statement)? ;

// loop
whileStmt  : 'enquanto' '(' expr ')' statement ;

// entrada e saída
ioStmt     : 'leia' '(' ID ')' ';'
           | 'escreva' '(' expr (',' expr)* ')' ';'
           ;

// bloco de código
block      : '{' statement* '}' ;

// tipos
type       : 'inteiro'
           | 'real'
           | 'booleano'
           ;

// expressões
expr
    : expr op=('*'|'/') expr                           # MulDivExpr
    | expr op=('+'|'-') expr                           # AddSubExpr
    | expr op=('<'|'>'|'<='|'>='|'=='|'!=') expr       # CompExpr
    | '-' expr                                         # UnaryMinus
    | '(' expr ')'                                     # ParenExpr
    | literal                                          # LiteralExpr
    | ID                                               # IdExpr
    ;

// literais
literal : INT_LITERAL
        | REAL_LITERAL
        | TRUE
        | FALSE
        | STRING_LITERAL
        ;

STRING_LITERAL : '"' (~["\r\n])* '"' ;

// === Lexer rules ===
TRUE     : 'verdadeiro' ;
FALSE    : 'falso' ;
ID       : [a-zA-Z_] [a-zA-Z0-9_]* ;
INT_LITERAL  : [0-9]+ ;
REAL_LITERAL : [0-9]+'.'[0-9]+ ;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
HASH_COMMENT : '#' ~[\r\n]* -> skip ;
