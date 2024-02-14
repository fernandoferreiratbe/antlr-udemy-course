grammar Looping;

root: instructions EOF;

instructions: instruction*;

instruction: (assign | output | while_);

output: 'send' expression;

assign: VAR ASSIGN expression;

while_: 'while' expression instructions;

expression: expression ADD expression  # Sum
        | expression SUB expression    # Sub
        | expression LT expression     # LessThan
        | expression GT expression     # GreaterThan
        | expression EQ expression     # Equals
        | expression NEQ expression    # NotEquals
        | VAR                          # Variable
        | NUM                          # NumValue
        ;

ADD: '+';
SUB: '-';
LT: '<';
GT: '>';
EQ: '==';
NEQ: '!=';

NUM: [0-9]+;
VAR: [a-zA-Z][a-zA-Z0-9]*;
ASSIGN: '<-';

WS: [ \t\r\n]+ -> skip;