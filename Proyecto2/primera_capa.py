def reportar_error_lexico(linea, columna, errores):
    errores.append(f">>> Error léxico (línea {linea}, posición {columna})")

def tokenize(code, errores):
    keywords = ['False', 'await', 'else', 'import', 'pass', 'None', 'break', 'except', 'in', 
                'raise', 'True', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for', 
                'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 
                'global', 'not', 'with', 'async', 'elif', 'if', 'or', 'yield', 'object', 'bool', 
                'self', 'print', 'range', 'match', 'case', '_', 'type', 'str']
    
    operators = {'+': 'tk_suma', '-': 'tk_resta', '*': 'tk_mult', '/': 'tk_div', '%': 'tk_mod',
                 '=': 'tk_asig', '==': 'tk_igual', '!=': 'tk_dif', '<': 'tk_menor', '>': 'tk_mayor',
                 '<=': 'tk_menor_igual', '>=': 'tk_mayor_igual', '&': 'tk_and', '|': 'tk_or',
                 '^': 'tk_xor', '~': 'tk_not', '<<': 'tk_shl', '>>': 'tk_shr', '->': 'tk_ejecuta'}
    
    delimiters = {'(': 'tk_par_izq', ')': 'tk_par_der', '{': 'tk_llave_izq', '}': 'tk_llave_der',
                  '[': 'tk_cor_izq', ']': 'tk_cor_der', ',': 'tk_coma', ':': 'tk_dos_puntos',
                  '.': 'tk_punto', ';': 'tk_punto_coma', '@': 'tk_arroba'}

    def is_keyword(word):
        return word in keywords
    
    def is_identifier(word):
        return word.isidentifier()
    
    def is_number(word):
        try:
            float(word)
            return True
        except ValueError:
            return False
    
    tokens = []
    line_num = 1
    column = 1
    current_word = ""
    in_string = None
    start_of_string = -1
    start_line = -1
    start_column = -1
    i = 0
    code_length = len(code)
    in_docstring = False

    error_detected = False

    while i < code_length and not error_detected:
        char = code[i]
        
        if not in_docstring and code[i:i+3] == '"""':
            in_docstring = True
            i += 3
            continue
        elif in_docstring and code[i:i+3] == '"""':
            in_docstring = False
            i += 3
            continue

        if in_docstring:
            i += 1
            continue

        if char == '\n':
            line_num += 1
            column = 1
            i += 1
            continue
        elif char.isspace():
            column += 1
            i += 1
            continue
        elif char in delimiters:
            tokens.append((delimiters[char], line_num, column))
            column += 1
            i += 1
            continue
        elif code[i:i+2] in operators:
            tokens.append((operators[code[i:i+2]], line_num, column))
            column += 2
            i += 2
            continue
        elif char in operators:
            tokens.append((operators[char], line_num, column))
            column += 1
            i += 1
            continue
        elif char == '"' or char == "'":
            if in_string is None:
                in_string = char
                start_of_string = i
                start_line = line_num
                start_column = column
            elif in_string == char:
                in_string = None
                tokens.append(('tk_cadena', line_num, column))
            column += 1
            i += 1
            continue
        
        if in_string is not None:
            column += 1
            i += 1
            continue
        
        current_word += char
        if is_keyword(current_word):
            tokens.append((current_word, line_num, column))
            current_word = ""
            column += 1
            i += 1
        elif is_identifier(current_word):
            if i+1 < code_length and not code[i+1].isalnum() and code[i+1] not in ('_',):
                tokens.append(('id', line_num, column))
                current_word = ""
            column += 1
            i += 1
        elif is_number(current_word):
            if i+1 < code_length and not code[i+1].isdigit() and code[i+1] != '.':
                tokens.append(('tk_entero', line_num, column))
                current_word = ""
            column += 1
            i += 1
        else:
            reportar_error_lexico(line_num, column, errores)
            error_detected = True
            break

    return tokens, errores
