# Lenguajes
Estudiantes de ciencias de la computación

Ana Amador 

Paula Caballero

Daniela López

Alan Osorio

Este proyecto implementa un Autómata Finito Determinista (DFA) en lenguaje C, que puede ser configurado y probado en un entorno Linux. A continuación, se detallan los pasos para clonar el repositorio, compilar el código fuente, configurar el DFA y ejecutar el programa.

# Requisitos
•	Sistema operativo Linux.
•	Compilador de C (GCC).
•	Acceso a la terminal de Linux.

1)	# CLONAR EL REPOSITORIO
a.	## Primero, debes clonar el repositorio que contiene el proyecto. Abre la terminal y ejecuta el siguiente comando: git clone <URL_DEL_REPOSITORIO>
i.	### Nota: Reemplaza <URL_DEL_REPOSITORIO> con la URL real del repositorio que quieres clonar.

2)	# Navegar al directorio del proyecto
a.	## Una vez clonado el repositorio, navega al directorio del proyecto: 
cd <NOMBRE_DEL_DIRECTORIO>
i.	### Nota: Reemplaza <NOMBRE_DEL_DIRECTORIO> con el nombre del directorio que contiene los archivos del proyecto.

3)	# Verificar los archivos
a.	## Asegúrate de que los archivos necesarios están presentes en el directorio. Deberías ver los siguientes tres archivos:
i.	###  DFA4.c: El archivo de código fuente en C.
ii.	 ### CONFIG.txt: El archivo de configuración que define los estados, el alfabeto y las transiciones del DFA.
iii.	### README.md: Este archivo con las instrucciones.
b.	## Para verificar esto, usa el siguiente comando:
i.	### Ls

4)	# Compilar el código fuente
a.	## Para compilar el archivo DFA4.c, necesitas utilizar el compilador GCC. Ejecuta el siguiente comando en la terminal:
i.	### Gcc DFA4.c -o dfa.out 
1.	### Esto generará un archivo ejecutable llamado en este caso `dfa.out`
   
5)	# Ejecutar el programa
a.	## Ahora que has compilado el código, puedes ejecutar el programa utilizando el archivo ejecutable `dfa.out`. Ejecuta el siguiente comando:
i.	## ./dfa.out

6)	# Configurar y probar el DFA
a.	## Cuando ejecutes el programa, se te pedirá que ingreses el nombre del archivo de configuración. El archivo de configuración predeterminado es config.txt, que ya está en el directorio del proyecto. Ingresa config.txt cuando se te solicite:
i.	### Ingrese el nombre del archivo de configuración: config.txt
b.	## Luego, se te pedirá que ingreses una cadena para probar. Ingresa la cadena que deseas evaluar según las reglas del DFA definidas en config.txt.

7)	# Probar múltiples cadenas
a.	## Después de ingresar una cadena, el programa te indicará si la cadena es aceptada o rechazada. Luego, te preguntará si deseas probar otra cadena. Puedes continuar ingresando cadenas o escribir `no` para finalizar.
i.	### ¿Desea probar otra cadena? (si/no): si
