def reportar_error_lexico(linea, columna, errores):
    """Registra un error léxico en una lista de errores."""
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
    in_string = None  # None, 'single', or 'double'
    start_of_string = -1  # Para llevar un registro de la posición de inicio de la cadena
    start_line = -1  # Para almacenar la línea donde comienza la comilla inicial
    start_column = -1  # Para almacenar la columna donde comienza la comilla inicial
    i = 0
    code_length = len(code)
    in_docstring = False  # Indica si estamos dentro de un docstring


    error_detected = False

    while i < code_length and not error_detected:
        char = code[i]
        
        # Detectar el inicio o fin de un docstring
        if not in_docstring and code[i:i+3] == '"""':
            in_docstring = True
            i += 3
            continue
        elif in_docstring and code[i:i+3] == '"""':
            in_docstring = False
            i += 3
            continue

        # Si estamos dentro de un docstring, ignorar el contenido
        if in_docstring:
            i += 1
            continue

        if char == '\n':
            if current_word:
                if is_keyword(current_word):
                    tokens.append(f'<{current_word},{line_num},{column - len(current_word)}>') 
                elif is_number(current_word):
                    tokens.append(f'<tk_entero,{current_word},{line_num},{column - len(current_word)}>') 
                elif is_identifier(current_word):
                    tokens.append(f'<id,{current_word},{line_num},{column - len(current_word)}>') 
                else:
                    reportar_error_lexico(line_num, column, errores)
                    error_detected = True
                current_word = ""
            line_num += 1
            column = 1
            in_string = None  # Restablecer en cada nueva línea
        elif char == '#':
            # Ignorar el resto de la línea como comentario
            while i < code_length and code[i] != '\n':
                i += 1
            continue  # Saltar al siguiente carácter de la línea
        elif char in ' \t':
            if current_word:
                if is_keyword(current_word):
                    tokens.append(f'<{current_word},{line_num},{column - len(current_word)}>') 
                elif is_number(current_word):
                    tokens.append(f'<tk_entero,{current_word},{line_num},{column - len(current_word)}>') 
                elif is_identifier(current_word):
                    tokens.append(f'<id,{current_word},{line_num},{column - len(current_word)}>') 
                else:
                    reportar_error_lexico(line_num, column, errores)
                    error_detected = True
                current_word = ""
            column += 1
        elif char in operators or char in delimiters:
            if current_word:
                if is_keyword(current_word):
                    tokens.append(f'<{current_word},{line_num},{column - len(current_word)}>') 
                elif is_number(current_word):
                    tokens.append(f'<tk_entero,{current_word},{line_num},{column - len(current_word)}>') 
                elif is_identifier(current_word):
                    tokens.append(f'<id,{current_word},{line_num},{column - len(current_word)}>') 
                else:
                    reportar_error_lexico(line_num, column, errores)
                    error_detected = True
                current_word = ""

            # Comprobar operadores compuestos
            if i + 1 < code_length and code[i:i+2] in operators:
                token_type = operators[code[i:i+2]]
                tokens.append(f'<{token_type},{line_num},{column}>') 
                column += 2
                i += 1
            elif char in operators:
                tokens.append(f'<{operators[char]},{line_num},{column}>') 
                column += 1
            elif char in delimiters:
                tokens.append(f'<{delimiters[char]},{line_num},{column}>') 
                column += 1

        elif char == '"':
            if in_string:
                # Si estamos en una cadena de texto, encontrar el cierre
                if in_string == 'double':
                    # Capturar el contenido dentro de las comillas
                    lexeme = code[start_of_string+1:i]  # Excluir las comillas en el token
                    tokens.append(f'<tk_cadena,”{lexeme}”,{start_line},{start_column}>') 
                    in_string = None
                    column += (i - start_of_string)  # Ajustar la columna, sin contar doble las comillas
                    i += 1  # Mover el índice después de la comilla de cierre
                    continue  # Saltar al próximo ciclo para evitar procesar de nuevo el carácter
            else:
                # Empezar una cadena de texto entre comillas dobles
                in_string = 'double'
                start_of_string = i  # Guardar la posición de inicio de la cadena
                start_line = line_num  # Guardar la línea de la comilla inicial
                start_column = column  # Guardar la columna de la comilla inicial
            column += 1

        elif char == "'":
            if in_string:
                # Si estamos en una cadena de texto, encontrar el cierre
                if in_string == 'single':
                    # Capturar el contenido dentro de las comillas
                    lexeme = code[start_of_string+1:i]  # Excluir las comillas en el token
                    tokens.append(f'<tk_cadena,”{lexeme}”,{start_line},{start_column}>') 
                    in_string = None
                    column += (i - start_of_string)  # Ajustar la columna, sin contar doble las comillas
                    i += 1  # Mover el índice después de la comilla de cierre
                    continue  # Saltar al próximo ciclo para evitar procesar de nuevo el carácter
            else:
                # Empezar una cadena de texto entre comillas simples
                in_string = 'single'
                start_of_string = i  # Guardar la posición de inicio de la cadena
                start_line = line_num  # Guardar la línea de la comilla inicial
                start_column = column  # Guardar la columna de la comilla inicial
            column += 1

        else:
            if not in_string:
                current_word += char
                column += 1

        i += 1

    # Procesar última palabra si existe
    if current_word and not error_detected:
        if is_keyword(current_word):
            tokens.append(f'<{current_word},{line_num},{column - len(current_word)}>') 
        elif is_number(current_word):
            tokens.append(f'<tk_entero,{current_word},{line_num},{column - len(current_word)}>') 
        elif is_identifier(current_word):
            tokens.append(f'<id,{current_word},{line_num},{column - len(current_word)}>') 
        else:
            reportar_error_lexico(line_num, column, errores)

    return tokens
