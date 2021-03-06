/* -*- mode: C++; c-file-style: "stroustrup"; indent-tabs-mode: nil; -*- */

/* tokens.cc: Definitions related to AST_Token and its subclasses. */

/* Authors: 
 * Toan Vuong
 * Eugene Huang
 * Dennis Rong
*/

#include <iostream>
#include <cstdlib>
#include "apyc.h"
#include "ast.h"
#include "apyc-parser.hh"

using namespace std;

/** Default print for tokens. */
void
AST_Token::print (ostream& out, int indent)
{
    out << "(<Token>)";
}

/** Default implementation. */
string
AST_Token::string_text () const
{
    throw logic_error ("unimplemented operation: string_text");
}

/** Default implementation. */
void
AST_Token::append_text(const string& s)
{
    throw logic_error ("unimplemented operation: append_text");
}

/** Represents a type_var */
class TypeVar_Token : public AST_Token {
private:
    void print (ostream& out, int indent) {
        out << "(type_var " << lineNumber() << " " << as_string() << ")";
    }

    TOKEN_CONSTRUCTORS(TypeVar_Token, AST_Token);
};

/** Represents an id. */
class Id_Token : public AST_Token {
private:
    void print (ostream& out, int indent) {
        out << "(id " << lineNumber() << " " << as_string() << ")";
    }

    TOKEN_CONSTRUCTORS(Id_Token, AST_Token);
};

/** Represents an integer literal. */
class Int_Token : public AST_Token {
private:

    void print (ostream& out, int indent) {
        out << "(int_literal " << lineNumber () << " " << value << ")";
    }

    /** Initialize value from the text of the lexeme, checking that
     *  the literal is in range.  [The post_make method may be
     *  overridden to provide additional processing during the
     *  construction of a node or token.] */
    Int_Token* post_make () {
        value = strtol(as_chars(),NULL,0);
        if (value > 1073741824)
        {
            error(as_chars(), "Integer greater than 2^30");
        }
        return this;
    }

    long value;

    TOKEN_CONSTRUCTORS(Int_Token, AST_Token);

};

/** Represents a string. */
class String_Token : public AST_Token {
private:
    
    /** Set literal_text from the text of this lexeme, converting
     *  escape sequences as necessary. */
    String_Token* post_make () {
        if (syntax () == RAWSTRING) {
            literal_text = string (as_chars (), text_size ());
        } else {
            // get rid of starting and ending quotes
            const char* s = as_chars();
            size_t i;
            i = 0;
            int v;
            literal_text.clear ();
            while (i < text_size()) {
                i += 1;
                if (s[i-1] == '\\') {
                    i += 1;
                    switch (s[i-1]) {
                    default: literal_text += '\\'; v = s[i-1]; break;
                    case '\n': continue;
                    case 'a': v = '\007'; break;
                    case 'b': v = '\b'; break;
                    case 'f': v = '\f'; break;
                    case 'n': v = '\n'; break;
                    case 'r': v = '\r'; break;
                    case 't': v = '\t'; break;
                    case 'v': v = '\v'; break;
                    case '\'': v = '\''; break;
                    case '"': case '\\': v = s[i-1]; break;
                    case '0': case '1': case '2': case '3': case '4':
                    case '5': case '6': case '7': 
                    { 
                        v = s[i-1] - '0';
                        for (int j = 0; j < 2; j += 1) {
                            if ('0' > s[i] || s[i] > '7')
                                break;
                            v = v*8 + (s[i] - '0');
                            i += 1;
                        }
                        break;
                    }
                    case 'x': {
                        if (i+2 > text_size() || 
                            !isxdigit (s[i]) || !isxdigit (s[i+1])) {
                            error (s, "bad hexadecimal escape sequence");
                            break;
                        }
                        sscanf (s+i, "%2x", &v);
                        i += 2;
                        break;
                    }
                    }
                } else
                    v = s[i-1];
                literal_text += (char) v;        
            }
        }
        return this;
    }

    void print (ostream& out, int indent) {
        out << "(string_literal " << lineNumber () << " \"";
        if (literal_text[0] == 'r' || literal_text[0] == 'R')
        {
            for (size_t i = 2; i < literal_text.size() - 1; i += 1)
            {
                char c = literal_text[i];
                out << c;
            }
        }
        else
        {
            size_t orig_size;
            orig_size = text_size();
            size_t size;
            size = 0;
            size_t start;
            start = 0;

            char quote = literal_text[0];
            if (orig_size >= 6 && quote == literal_text[1] && quote == literal_text[2] && quote == literal_text[orig_size-1] && quote == literal_text[orig_size-2] && quote == literal_text[orig_size-3])
            {
              start = 3;
              size = orig_size - 3;
            }
            else
            {
              start = 1;
              size = orig_size - 1;
            }


            for (size_t i = start; i < size; i += 1) {
                char c = literal_text[i];
                if (c < 32 || c == '\\' || c == '"') {
                    out << "\\" << oct << setw (3) << setfill('0') << (int) c
                        << setfill (' ') << dec;
                } else
                    out << c;
            }
        }
        out << "\")";
    }

    string string_text () const {
        return literal_text;
    }

    void append_text(const string& s) {
        literal_text += s;
    }

    TOKEN_CONSTRUCTORS(String_Token, AST_Token);
    static const String_Token raw_factory;

    string literal_text;
};

/** A dummy token whose creation registers String_Token as the class
 *  to use for RAWSTRING tokens produced by the lexer.  (The
 *  TOKEN_FACTORY macro above registers String_Token as the class for
 *  non-raw the STRING tokens as well.)
 *  */ 
const String_Token String_Token::raw_factory (RAWSTRING);


/*
 * Token Factories
*/
TOKEN_FACTORY(String_Token, STRING);
TOKEN_FACTORY(Id_Token, ID);
TOKEN_FACTORY(Int_Token, INT_LITERAL);
TOKEN_FACTORY(TypeVar_Token, TYPE_VAR);

    

