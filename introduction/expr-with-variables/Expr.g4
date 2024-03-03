grammar Expr;

/*
* Parser Rules
*/
root: action+ EOF;

action: NAME ':=' expr
        | 'write' NAME
        ;
/* assoc=right indicates that expression starts from right to the left. */
expr: <assoc=right> expr '^' expr
    | expr ('*' | '/') expr
    | expr ('+' | '-') expr
    | NUM
    ;

/*
* Lexer Rules
*/
NUM: [0-9]+;
NAME: [a-z]+;

WS: [ \n]+ -> skip;
