import tkinter as tk
from tkinter import Button, Frame, Label, Entry

def calcula_imc():
    imc = float(peso.get()) / float(altura.get()) ** 2
    if imc < 18.5:
        resultado['text'] = f"Seu IMC é: {imc:.2f} (Abaixo do peso)"
    elif 18.5 <= imc < 24.9:
        resultado['text'] = f"Seu IMC é: {imc:.2f} (Peso normal)"
    elif 25 <= imc < 29.9:
        resultado['text'] = f"Seu IMC é: {imc:.2f} (Sobrepeso)"
    elif 30 <= imc < 34.9:
        resultado['text'] = f"Seu IMC é: {imc:.2f} (Obesidade grau I)"
    elif 35 <= imc < 39.9:
        resultado['text'] = f"Seu IMC é: {imc:.2f} (Obesidade grau II)"
    print(f"Seu IMC é: {imc:.2f}")

janela = tk.Tk() # Cria a janela principal
janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f"+{x}+{y}")

frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1) # Cria um frame com padding
Label(frame, text="Para saber o seu IMC digite os valores abaixo", pady=40).grid(column=1, row=1, columnspan=2) # Adiciona um rótulo à janela, usando o grid para posicionamento

Label(frame, text="Qual é o seu peso(kg)?").grid(column=1, row=2) # Adiciona um rótulo para o peso
peso = Entry(frame)
peso.grid(column=2, row=2) # Adiciona um campo de entrada para o peso

Label(frame, text="Qual é a sua altura(m)?").grid(column=1, row=3) # Adiciona um rótulo para a altura
altura = Entry(frame)
altura.grid(column=2, row=3) # Adiciona um campo de entrada para a altura,

Button(frame, text="Calcular IMC", command=calcula_imc).grid(column=2, row=4) # Adiciona um botão para calcular o IMC

resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2) # Adiciona um rótulo para mostrar o resultado


janela.title("Calculadora de IMC")
janela.mainloop() # Inicia o loop principal da interface gráfica


