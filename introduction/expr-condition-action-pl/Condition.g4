grammar Condition;

/*
 * Parser Ruler
 */

root: action+ EOF;

action: 'if' expr action ('else' action)? # Condition
    | 'print' expr                        # Print
    ;

expr: expr GT expr # GreaterThan
    | expr LT expr # LessThan
    | NUM          # Value
    ;

/*
 * Lexer Rules
 */

GT: '>';
LT: '<';
NUM: [0-9]+;

WS: [ \t\r\n]+ -> skip;