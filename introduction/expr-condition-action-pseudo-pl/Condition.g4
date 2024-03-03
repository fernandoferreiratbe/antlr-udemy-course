grammar Condition;

root: action+ EOF;

action: 'iff' expr action ('otherwise' action)?  # Condition
        | 'write' expr                           # Write
        | 'next' expr                            # Next
        ;

expr: expr GT expr  # GreaterThan
    | expr LT expr  # LessThan
    | expr EQ expr  # Equals
    | expr NEQ expr # NotEquals
    | expr ADD expr # Sum
    | NUM           # NumValue
    ;

GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';
ADD: '+';
NUM: [0-9]+;

WS: [ \t\r\n] -> skip;