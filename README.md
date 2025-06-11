# PRACTICA-COLABORATIVA
En esta práctica colaborativa realizamos la creación de códigos que imprima "Hola Mundo". 
Los programas que creamos fueron:
Algoritmo en PSeInt ----- Vanessa Ríos Pérez
Programacion Esctructurada en Python ------ Elías Coyotzi Sosa
Programacion Orientada a Objetos ------- Melanie Sosa Degabriel
Programacion en Tkinter -------- Dalila Yusaví Conde Flores 
Diagrama de clases ---------- Paulina Sánchez Ramírez


# ALGORITMO EN PSEINT
- Comienza el algoritmo con el nombre HolaMundo.
- Usa la instalación Escribir para mostrar un mensaje al usuario.
- El mensaje "Hola Mundo" aparece en pantalla cuando se ejecuta el programa.
- Termina el algoritmo con FinAlgoritmo.


# PROGRAMA ESTRUCTURADO A PYTHON
- Comienza definiendo la función
- Despues se coloca un print en donde se escribira "Hola mundo"
- Por ultimo cerrará con un main

 # PROGRAMA CON POO
 El programa define una clase llamada HolaMundo, que sirve para guardar un mensaje personalizado. Cuando se crea un objeto a partir de esta clase, se le puede dar un mensaje, como por ejemplo "Hola mundo". Luego, el programa utiliza un método de esa clase para mostrar ese mensaje en la pantalla. En resumen, el programa está diseñado para recibir un mensaje al inicio y luego imprimirlo cuando se lo pida. Es una forma básica de demostrar cómo funcionan las clases y los métodos en Python.

#  PROGRAMA CON INTERFAZ GRÁFICA (TKINTER)
- Comienza abriendo la extensió o librería tkinter para poder agregar la interfaz gráfica
- 



# Diagrama de clases 
El codigo tiene una sola clase llamada HolaMundo. Entonces el diagrama se enfoca en esta.
El diagrama tiene tres partes, separadas por líneas horizontales:
- Nombre de la clase
- Atributos (datos de la clase)
- Métodos (funciones de la clase)
- 
1. Nombre de la clase
En la parte superior se pone el nombre de la clase: HolaMundo.
Esto indica que todo lo que está en ese recuadro es parte de esa clase.

3. Atributos
Aquí se muestra el atributo mensaje.
La convención es que si un atributo tiene un signo - adelante (menos), indica que es privado o interno (en Python no se usa explícitamente así, pero es una convención).
mensaje: str indica que mensaje es de tipo cadena de texto (str).
La clase usa este atributo para guardar el texto que se quiere mostrar cuando se saluda.

5. Métodos
Los métodos son las funciones dentro de la clase.
El signo + indica que el método es público, es decir, accesible desde fuera de la clase.
__init__(mensaje: str) es el método constructor. Se llama cuando creas un objeto de la clase. Recibe un parámetro mensaje para inicializar el atributo de la clase.
saludar() es el método que imprime el mensaje almacenado.
/Cuando creamos un objeto como: saludo = HolaMundo("Hola mundo"), estamos usando el metodo __init__ para asignar "Hola mundo" al atributo mensaje.
/Luego, al llamar saludo.saludar(), ejecutamos el metodo que imprime el mesnsaje
