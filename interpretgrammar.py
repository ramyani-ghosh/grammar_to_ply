grammar_file = 'test_grammar.txt'


f = open(grammar_file, "r")

l = f.readlines()
lines=[]
for line in l:
    lines.append(line.rstrip('\n'))

#dictionary of lvalue and rvalues in grammar
dict= {}
for line in lines:
    lr = line.split(":=")
    rule_right = lr[1].strip()
    rule_right = rule_right.replace("|","\n\t|")
    dict[lr[0].strip()] = rule_right

#print(dict)

#reserved keywords:
reserved={}
reserved_words = dict['reserved'].split(" ")
for word in reserved_words:
    word=word.strip()
    if( word != "" ):
        reserved[word]=word.upper()
print(reserved)
#token values:
tokens = list(reserved.values())
for token in dict['tokens'].split(" "):
    t=token.split('=')
    tokens_temp = {}
    tokens_temp[t[0]]=t[1]
    tokens.append(t[0].split("_")[1])
    locals().update(tokens_temp)

print("TOKENS GENERATED: ", tokens,"\n\n")
#start production
start_dict={}
start_dict['start'] = dict['start']
locals().update(start_dict)

# Ignored characters
t_ignore = " "#"\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def p_empty(p):
     'empty :'
     pass
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


function =""
for line in dict:
    if line.startswith('t_'):
        left_production = line[2:]
        function = "\ndef "+line+"(t):\n\tr\'" +dict[line]+ "\'\n\tt.type=reserved.get(t.value,\'"+ left_production +"\')\n\treturn t"
        print(function)
exec(function)
# def t_NAME(t):
#      r'[a-zA-Z_][a-zA-Z_0-9]*'
#      t.type = reserved.get(t.value,'NAME')    # Check for reserved words
#      return t
#
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

action_funcs = ""
#defining the actions:
for line in dict:
    if line not in ['start','reserved','tokens']:
        function = "\ndef p_"+line+"(t):\n\t\'\'\'"+line+ " : " +dict[line] + "\'\'\' "
        action_funcs = action_funcs + function + "\n"
print("ACTION FUNCTIONS GENERATED: ", action_funcs,"\n\n")
def p_error(t):
    print("Syntax error at '%s'" % t.value)


codesegment=''' foo(a-b-para):
\tsome_statement
\treturn a'''

print("\n\n  PARSING CODE SEGMENT:\n", "_"*40, "\n",codesegment,"\n","_"*40,"\n\n")
execute_code = action_funcs +'''\n\nimport ply.yacc as yacc
parser = yacc.yacc()
yacc.parse(codesegment)\n\n'''
#print(execute_code)
exec(execute_code)


# reserved = {
#     'def' : 'DEF'
#  }
# tokens = [ 'COLON', 'COMMA','TAB',  'NAME', 'LPAREN','RPAREN' ] + list(reserved.values())
#
# # Tokens
# t_COMMA   = r'\,'
# t_COLON   = r'\:'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_TAB     = r'\t'
# #t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
#
# def t_NAME(t):
#      r'[a-zA-Z_][a-zA-Z_0-9]*'
#      t.type = reserved.get(t.value,'NAME')    # Check for reserved words
#      return t
#
