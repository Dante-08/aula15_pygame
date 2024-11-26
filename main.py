import tkinter as tk

def soma():
    n1 = float(input1.get())
    n2 = float(input2.get())
    soma = n1 + n2
    Result.config(text=f'Resultado: {soma}')

def sub():
    n1 = float(input1.get())
    n2 = float(input2.get())
    sub = n1 - n2
    Result.config(text=f'Resultado: {sub}')

def div():
    n1 = float(input1.get())
    n2 = float(input2.get())
    div = n1 / n2
    Result.config(text=f'Resultado: {div:.2f}')

def mult():
    n1 = float(input1.get())
    n2 = float(input2.get())
    mult = n1 * n2
    Result.config(text=f'Resultado: {mult}')


root = tk.Tk()
root.title('Calculadora')
root.geometry('250x350')

# label

texto = tk.Label(root, text= 'CALCULADORA')
texto.grid(row=1, column=2)

# input
input1 = tk.Entry(root)
input1.grid(row=2,column= 2, pady=20, padx=60),

input2 = tk.Entry(root)
input2.grid(row=3,column= 2, padx=60)


# label

Result = tk.Label(root, text= '-')
Result.grid(row=9, column=2, padx=60)

# botão soma

btn = tk.Button(root, text= '+', command = soma)
btn.grid(row= 5, column=2, pady=5)

# botão sub

btn = tk.Button(root, text= '-', command = sub)
btn.grid(row= 6, column=2, pady=5)

# botão div

btn = tk.Button(root, text= '/', command = div)
btn.grid(row= 7, column=2, pady=5)

# botão multiplicação

btn = tk.Button(root, text= 'X', command = mult)
btn.grid(row= 8, column=2, pady=5)


root.mainloop()