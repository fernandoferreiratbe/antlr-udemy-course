grammar Condition;

root: action+ EOF;

action: 'if' expr action ('else' action)? # Condition
    | 'print' expr                        # Print
    ;

expr: expr GT expr # GreaterThan
    | expr LT expr # LessThan
    | NUM          # Value
    ;

GT: '>';
LT: '<';
NUM: [0-9]+;

WS:[ \n]+ -> skip;