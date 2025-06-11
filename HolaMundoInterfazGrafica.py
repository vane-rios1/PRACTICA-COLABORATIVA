import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("500x500")

ventana.configure(bg="blue")

etiqueta = tk.Label(ventana, text="Hola mundo", font=("Arial", 50), bg="blue", fg="white")
etiqueta.pack(pady=20)

ventana.mainloop()
