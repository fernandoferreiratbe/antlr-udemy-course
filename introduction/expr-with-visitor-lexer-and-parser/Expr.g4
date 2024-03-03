grammar Expr;

/*
 * Parser Rules 
 */
root: expr EOF ;

expr: expr MUL expr  # Mul
    | expr DIV expr  # Div
    | expr PLUS expr # Sum
    | expr SUB expr  # Sub
    | NUM            # Value
    ;

/*
 * Lexer Rules
 */
NUM: [0-9]+ ;
MUL: '*' ;
DIV: '/' ;
PLUS: '+' ;
SUB: '-' ;
WS: [ \n]+ -> skip ;


/*
 * expr: Definition of the grammar for the sum and / or subtraction of natural numbers
 * skip: Tells the scanner that the WS token should not reach the parser.
 * root: To process the end of the file.
 */