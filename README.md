# PRACTICA-COLABORATIVA
En esta práctica colaborativa realizamos la creación de códigos que imprima "Hola Mundo". 
Los programas que creamos fueron:
- Algoritmo en PSeInt ----- Vanessa Ríos Pérez
- Programacion Esctructurada en Python ------ Elías Coyotzi Sosa
- Programacion Orientada a Objetos ------- Melanie Sosa Degabriel
- Programacion en Tkinter -------- Dalila Yusaví Conde Flores 
- Diagrama de clases ---------- Paulina Sánchez Ramírez


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
- import tkinter as tk : Esta línea importa la librería  tkinter , que se usa para crear interfaces gráficas de usuario (GUI) en Python. Se le da el alias  tk  para facilitar su uso en el resto del código.
​
- ventana = tk.Tk() : Se crea la ventana principal de la aplicación.   tk.Tk()  crea un objeto ventana. Este objeto se asigna a la variable  ventana .
​
-  ventana.title("Hola Mundo") : Se establece el título de la ventana como "Hola Mundo".
​
-  ventana.geometry("500x500") : Se define el tamaño de la ventana a 500 píxeles de ancho por 500 píxeles de alto.
​
-  ventana.configure(bg="blue") : Se configura el color de fondo de la ventana a azul ( "blue" ).
​
-  etiqueta = tk.Label(ventana, text="Hola mundo", font=("Arial", 50), bg="blue", fg="white") : Se crea una etiqueta ( Label ) que mostrará el texto "Hola mundo"
​
-  ventana : La ventana donde se colocará la etiqueta.
​
-  text="Hola mundo" : El texto que mostrará la etiqueta.
​
-  font=("Arial", 50) : La fuente y el tamaño del texto (Arial, tamaño 50).
​
-  bg="blue" : El color de fondo de la etiqueta (azul, para que coincida con el fondo de la ventana).
​
-  fg="white" : El color del texto (blanco, para que contraste con el fondo azul).
​
-  etiqueta.pack(pady=20) : Se coloca la etiqueta en la ventana usando el gestor de geometría  pack .  pady=20  añade un relleno de 20 píxeles de espacio vertical arriba y abajo de la etiqueta.
​
-  ventana.mainloop() : Esta línea inicia el bucle principal de la aplicación  tkinter .  Mantiene la ventana abierta y responde a los eventos del usuario (como clics de ratón o pulsaciones de teclado) hasta que el usuario la cierre.



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
