import tkinter as tk
from tkinter import messagebox

#__________________

def sumar(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    suma = a + b
    
    resultado_var.set(f"Suma: {suma:g}")

#__________________

def resta(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    resta = a - b    
    resultado_var.set(f"Resta: {resta:g}")

#__________________

def division(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    if b == 0:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
        return
    division = a / b    
    resultado_var.set(f"División: {division:g}")

#__________________

def multiplicacion(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    multiplicacion = a * b    
    resultado_var.set(f"Multiplicación: {multiplicacion:g}")

#__________________

def potencia(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    potencia = a ** b    
    resultado_var.set(f"Potencia (A^B): {potencia:g}")

#__________________

def raiz_cuadrada(event=None):
    a_str = entry_a.get()
    try:
        a = float(a_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa un número válido en A.")
        return
    if a < 0:
        messagebox.showerror("Error", "No se puede calcular raíz cuadrada de un número negativo.")
        return
    raiz = a ** 0.5    
    resultado_var.set(f"Raíz cuadrada de A: {raiz:g}")
    

#__________________

def raiz_b(event=None):
    b_str = entry_b.get()
    try:
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa un número válido en B.")
        return
    if b < 0:
        messagebox.showerror("Error", "No se puede calcular raíz cuadrada de un número negativo.")
        return
    raiz = b ** 0.5    
    resultado_var.set(f"Raíz cuadrada de B: {raiz:g}")

#__________________

def modulo(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    if b == 0:
        messagebox.showerror("Error", "No se puede calcular módulo con divisor cero.")
        return
    modulo = a % b    
    resultado_var.set(f"Módulo (A % B): {modulo:g}")

#__________________

def promedio(event=None):
    a_str = entry_a.get()
    b_str = entry_b.get()
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa dos números válidos.")
        return
    promedio = (a + b) / 2    
    resultado_var.set(f"Promedio: {promedio:g}")

#================= INTERFAZ =================#

root = tk.Tk()
root.title("Calculadora Básica")
root.resizable(True, True)
root.configure(bg="pink")

# --- Configurar expansión de la nterfas grafica ---
for i in range(4):  # columnas
    root.columnconfigure(i, weight=1)
for j in range(5):  # filas
    root.rowconfigure(j, weight=1)

# Entradas
tk.Label(root, text="Número A:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, columnspan=3, padx=8, pady=8, sticky="nsew")
entry_a.focus()

tk.Label(root, text="Número B:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, columnspan=3, padx=8, pady=8, sticky="nsew")

#   Botones:
# Botones fila 1
tk.Button(root, text="Sumar", command=sumar).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Restar", command=resta).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Dividir", command=division).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Multiplicar", command=multiplicacion).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

# Botones fila 2
tk.Button(root, text="Potencia", command=potencia).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Raíz √A", command=raiz_cuadrada).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Módulo", command=modulo).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Promedio", command=promedio).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
tk.Button(root, text="Raíz √B", command=raiz_b).grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

# Resultado
resultado_var = tk.StringVar(value="Resultado: ")
tk.Label(root, textvariable=resultado_var, font=("Arial", 11, "bold")).grid(
    row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
)

#otro ¿?
root.bind("<Return>", sumar)

root.mainloop()
