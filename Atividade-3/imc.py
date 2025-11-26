
import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    """
    Pega os dados dos campos de altura e peso, calcula o IMC
    e exibe o resultado e a classificação.
    """
    try:
        # Pega os valores dos campos de entrada (Entry)
        peso_str = entry_peso.get()
        altura_str = entry_altura.get()

        #Converte para números (float)
        peso = float(peso_str)
        altura_cm = float(altura_str)

        if altura_cm == 0:
            # Evita divisão por zero
            raise ZeroDivisionError

        altura_m = altura_cm / 100

        #Fórmula do IMC: peso / (altura * altura)
        imc = peso / (altura_m ** 2)

        #Determina a classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc < 34.9:
            classificacao = "Obesidade Grau I"
        elif imc < 39.9:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"

        #Formata o resultado
        resultado_final = f"{imc:.2f} ({classificacao})"

        #Atualiza o texto do label de resultado
        resultado_var.set(resultado_final)

    except ValueError:
        #Se o usuário digitar texto em vez de número
        messagebox.showerror("Erro de Entrada", "Por favor, digite valores numéricos válidos para peso e altura.")
    except ZeroDivisionError:
        messagebox.showerror("Erro de Cálculo", "A altura não pode ser zero.")


def limpar_dados():
    """
    Limpa todos os campos de entrada e o resultado.
    """
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_var.set("")  # Limpa o label de resultado


def sair():
    """
    Fecha a janela do aplicativo.
    """
    janela.destroy()


# --- 2.INTERFACE GRÁFICA (View) ---

#Cria a janela principal
janela = tk.Tk()
janela.title("Cálculo de IMC")
janela.geometry("450x300")  # Define um tamanho inicial

#Cria uma variável especial do Tkinter para o resultado
#Isso permite que o label mude de texto automaticamente
resultado_var = tk.StringVar()

# --- Criação dos Widgets (Componentes da tela) ---

# Frame principal para organizar os campos
frame_campos = tk.Frame(janela)
frame_campos.pack(pady=10, padx=10)

#Nome do Paciente
label_nome = tk.Label(frame_campos, text="Nome do Paciente:")
label_nome.grid(row=0, column=0, sticky="e", pady=5)
entry_nome = tk.Entry(frame_campos, width=40)
entry_nome.grid(row=0, column=1, pady=5)

#Endereço
label_endereco = tk.Label(frame_campos, text="Endereço Completo:")
label_endereco.grid(row=1, column=0, sticky="e", pady=5)
entry_endereco = tk.Entry(frame_campos, width=40)
entry_endereco.grid(row=1, column=1, pady=5)

#Altura
label_altura = tk.Label(frame_campos, text="Altura (cm):")
label_altura.grid(row=2, column=0, sticky="e", pady=5)
entry_altura = tk.Entry(frame_campos, width=40)
entry_altura.grid(row=2, column=1, pady=5)

#Peso
label_peso = tk.Label(frame_campos, text="Peso (Kg):")
label_peso.grid(row=3, column=0, sticky="e", pady=5)
entry_peso = tk.Entry(frame_campos, width=40)
entry_peso.grid(row=3, column=1, pady=5)

#Resultado
label_resultado_titulo = tk.Label(frame_campos, text="Resultado:")
label_resultado_titulo.grid(row=4, column=0, sticky="e", pady=10)
#Label onde o resultado REAL será exibido
label_resultado_valor = tk.Label(frame_campos, textvariable=resultado_var, font=("Arial", 12, "bold"))
label_resultado_valor.grid(row=4, column=1, sticky="w", pady=10)

#Frame para os botões (para organizar eles lado a lado)
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

#Botão Calcular
btn_calcular = tk.Button(frame_botoes, text="Calcular IMC", command=calcular_imc, width=12)
btn_calcular.pack(side=tk.LEFT, padx=10)

#Botão Limpar
btn_limpar = tk.Button(frame_botoes, text="Limpar Dados", command=limpar_dados, width=12)
btn_limpar.pack(side=tk.LEFT, padx=10)

#Botão Sair
btn_sair = tk.Button(frame_botoes, text="Sair", command=sair, width=12)
btn_sair.pack(side=tk.LEFT, padx=10)

# --- 3. Inicia o aplicativo ---
#Deixa a janela aberta esperando por interações do usuário
janela.mainloop()