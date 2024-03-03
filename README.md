## Antlr - Another Tool For Language Recognition


## Setup
In order to reproduce, change or perform some test you should configure the virtual environment
Note: These steps were ran into macOS operating system.
```
python -m vevn .anltr-venv
source .antlr-venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Generate Lexer and Parser and Visitor for Python3 language
```
antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g4
```

## Project Structure

- **Introduction package** contains the fundamentals concepts needs to implement bazilio language
- **baziliolanguage package** contains grammar, source code and resources to handle the bazilio language transpiler


## Documentation

Official Antlr site can be reach [here](https://www.antlr.org/)

Antlr Mega Tutorial can be reach [here](https://tomassetti.me/antlr-mega-tutorial/)

Udemy Course made by [Lucas Basilio](https://www.udemy.com/user/lucas-estevao-bazilio/) can be reach [here](https://www.udemy.com/course/antlr-programming-masterclass-with-python/)

