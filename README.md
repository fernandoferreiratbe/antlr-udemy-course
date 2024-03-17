## Antlr - Another Tool For Language Recognition


## Setup
In order to reproduce, change or perform some test you should configure the virtual environment
Note: These steps were ran into macOS operating system.
```
python -m venv .anltr-venv
source .antlr-venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Generate Lexer and Parser and Visitor for Python3 language
```
antlr4 -Dlanguage=Python3 -no-listener -visitor <grammar_name>.g4
```

## Project Structure

- **Introduction package** contains the fundamentals concepts needs to implement bazilio language
- **baziliolanguage package** contains grammar, source code and resources to handle the bazilio language transpiler


## Documentation

Official Antlr site can be reach [here](https://www.antlr.org/)

Antlr Mega Tutorial can be reach [here](https://tomassetti.me/antlr-mega-tutorial/)

Udemy Course made by [Lucas Basilio](https://www.udemy.com/user/lucas-estevao-bazilio/) can be reach [here](https://www.udemy.com/course/antlr-programming-masterclass-with-python/)


## Additional Info

Say to Antlr4 where it should put the generated files. But pay attention, in order to use correctly you should be into grammar directory
```
antlr4 -Dlanguage=Python3 -no-listener -visitor Bazilio.g4 -o files/
```

Optionally to the command above, you should use
```
antlr4 -Dlanguage=Python3 -no-listener -visitor baziliolanguage/Bazilio.g4 -Xexact-output-dir -o baziliolanguage/.
```
With the command line above you can generate antlr4 files from everywhere and redirect the generated files to a specific directory.
