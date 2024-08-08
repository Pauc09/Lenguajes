# Lenguajes
Estudiantes de ciencias de la computación
Ana Amador 
Paula Caballero
Daniela López
Alan Osorio

Este proyecto implementa un simulador de un Autómata Finito Determinista (DFA) en C.
Este simulador permite configurar el DFA a través de un archivo de configuración y probar diferentes cadenas de entrada para verificar si son aceptadas o rechazadas por el autómata.
*Descripción del Proyecto*
El simulador de DFA lee un archivo de configuración que define los componentes del autómata: el conjunto de estados, el alfabeto de entrada, el estado inicial, el conjunto de estados de aceptación y las transiciones entre estados.
Luego, procesa las cadenas de entrada carácter por carácter, siguiendo las transiciones definidas, y determina si cada cadena es aceptada o rechazada.
El archivo "config.txt" cumple con los siguientes parametros: 
q0,q1,q2
a,b
q0
q2
q0,a,q1
q1,b,q2
q2,a,q0
