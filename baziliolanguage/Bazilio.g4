grammar Bazilio;

root: procedureDefinition*;

procedureDefinition: PROCNAME parametersId START_BLOCK instructions END_BLOCK;

parametersId: (VAR)*;

instructions: instruction*;

instruction: (assign | input_ | output_)
            | (reprod | procedureCall | condition | while_)
            | (addElementToList | removeElementFromList);

assign: VAR ASSIGN expr;
input_: '<?>' VAR;
output_: '<w>' expr;

reprod: REPRDO expr;
procedureCall: PROCNAME parametersExpr;
condition: 'if' expr START_BLOCK instructions END_BLOCK ('else' START_BLOCK instructions END_BLOCK)?;
while_: 'while' expr START_BLOCK instructions END_BLOCK;

addElementToList: VAR ADDING expr;
removeElementFromList: CUTTING VAR LEFT_BRACKET expr RIGHT_BRACKET;
sizeFromList: SIZE VAR;
query: VAR LEFT_BRACKET expr RIGHT_BRACKET;

expr: expr MUL expr  # Multiplication
    | expr DIV expr  # Division
    | expr MOD expr  # Module
    | expr SUM expr  # Sum
    | expr SUB expr  # Subtraction
    | expr GT expr   # GreaterThan
    | expr LT expr   # LessThan
    | expr GET expr  # GreaterThanOrEqualsTo
    | expr LET expr  # LessThanOrEqualsTo
    | expr EQ expr   # EqualsTo
    | expr NEQ expr  # NotEqualsTo
    | sizeFromList   # ListSize
    | query          # QueryExpression
    | list           # ListExpression
    | LEFT_PARANTHESES expr RIGHT_PARANTHESES  # Expression
    | VAR            # Variable
    | STRING         # String
    | NUM            # Number
    | NOTE           # Note
    ;

parametersExpr: (expr)*;
list: '{' expr* '}';


CUTTING: '8<';
ADDING: '<<';
REPRDO: '(:)';
SIZE: '#';

PROCNAME: [A-Z][a-zA-Z0-9_]*;

NOTE: [A-G][0-9]?;

VAR: [a-zA-Z][a-zA-Z0-9_]*;
NUM: '-'?[0-9]+;
STRING: '"' ('\\' . | ~('\\'|'"'))* '"';
ASSIGN: '<-';

MUL: '*';
DIV: '/';
MOD: '%';
SUM: '+';
SUB: '-';
EQ: '=';
NEQ: '/=';
GT: '>';
LT: '<';
GET: '>=';
LET: '<=';

START_BLOCK: '|:';
END_BLOCK: ':|';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_PARANTHESES: '(';
RIGHT_PARANTHESES: ')';

COMMENT: '###' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;