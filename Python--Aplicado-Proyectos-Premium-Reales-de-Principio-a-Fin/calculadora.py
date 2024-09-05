import tkinter as tk

ventana = tk.Tk()
boton= tk.Button(ventana, text="Haz click aquí")
ventana.title("Calculadora")
ventana.configure(background="grey")

ventana.geometry("350x400")

mensaje= tk.Label(ventana, text="calculadora cientifica", bg="grey")
mensaje.pack()

ventana.mainloop()