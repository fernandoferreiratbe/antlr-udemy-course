grammar Expr;

/*
 * Parser Rules 
 */
root: expr EOF ;

expr: expr PLUS expr
    | expr SUB expr
    | NUM
    ;

/*
 * Lexer Rules
 */
NUM: [0-9]+ ;
PLUS: '+' ;
SUB: '-' ;
WS: [ \n]+ -> skip ;


/*
 * expr: Definition of the grammar for the sum and / or subtraction of natural numbers
 * skip: Tells the scanner that the WS token should not reach the parser.
 * root: To process the end of the file.
 */