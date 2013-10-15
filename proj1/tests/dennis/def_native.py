# Body of a function may be replaced in its entirety by the single statement
# "native string-literal," in either form below. This means that the function
# is implemented by a "native" function (C or C++ in our case) as part of the
# run-time system.

def hello():
    native "stringliteral"

def hello(): native "stringliteral"