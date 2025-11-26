import tkinter as tk
from tkinter import messagebox
import sqlite3 # 1. Importar a biblioteca do banco de dados

#FUNÇÕES DE BANCO DE DADOS

def conectar_banco():
    """Conecta ao banco de dados (ou cria se não existir)"""
    conn = sqlite3.connect('imc_pacientes.db')
    return conn

def criar_tabela():
    """Cria a tabela no banco de dados se ela ainda não existir"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            altura REAL,
            peso REAL,
            imc REAL,
            classificacao TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_dados(nome, endereco, altura, peso, imc, classificacao):
    """Salva o registro do paciente no banco de dados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pacientes (nome, endereco, altura, peso, imc, classificacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, endereco, altura, peso, imc, classificacao))
    conn.commit()
    conn.close()
    print("Dados salvos com sucesso!")

def ver_historico():
    """Busca os dados no banco e exibe em uma janela"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, imc, classificacao FROM pacientes")
    registros = cursor.fetchall()
    conn.close()

    if not registros:
        messagebox.showinfo("Histórico", "Nenhum registro encontrado.")
        return

    #Formata o texto para exibir
    texto_historico = "Histórico de Consultas:\n----------------------\n"
    for registro in registros:
        texto_historico += f"Nome: {registro[0]} | IMC: {registro[1]:.2f} | {registro[2]}\n"
    
    #Exibe numa caixa de mensagem (poderia ser uma nova janela também)
    messagebox.showinfo("Histórico de IMC", texto_historico)


#LÓGICA DO PROGRAMA 

def calcular_imc():
    """
    Pega os dados, calcula o IMC, exibe e SALVA NO BANCO.
    """
    try:
        #Pega os valores dos campos
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        peso_str = entry_peso.get()
        altura_str = entry_altura.get()

        #Validação simples para obrigar nome
        if not nome:
            messagebox.showwarning("Aviso", "Por favor, preencha o Nome do Paciente.")
            return

        #Converte para números
        peso = float(peso_str)
        altura_cm = float(altura_str)

        if altura_cm == 0:
            raise ZeroDivisionError

        altura_m = altura_cm / 100

        #Cálculo
        imc = peso / (altura_m ** 2)

        #Classificação
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

        #Formata resultado visual
        resultado_final = f"{imc:.2f} ({classificacao})"
        resultado_var.set(resultado_final)

        #NOVO: SALVAR NO BANCO DE DADOS
        salvar_dados(nome, endereco, altura_cm, peso, imc, classificacao)
        messagebox.showinfo("Sucesso", "Cálculo realizado e salvo no banco de dados!")

    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite valores numéricos válidos para peso e altura.")
    except ZeroDivisionError:
        messagebox.showerror("Erro de Cálculo", "A altura não pode ser zero.")


def limpar_dados():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_var.set("")


def sair():
    janela.destroy()


#INICIALIZAÇÃO

#Cria a tabela ao iniciar o programa
criar_tabela()

#INTERFACE GRÁFICA (Igual à anterior, com um botão extra)

janela = tk.Tk()
janela.title("Cálculo de IMC com Banco de Dados")
janela.geometry("500x350") #Aumentei um pouco a altura

resultado_var = tk.StringVar()

frame_campos = tk.Frame(janela)
frame_campos.pack(pady=10, padx=10)

#Campos (Nome, Endereço, Altura, Peso)
tk.Label(frame_campos, text="Nome do Paciente:").grid(row=0, column=0, sticky="e", pady=5)
entry_nome = tk.Entry(frame_campos, width=40)
entry_nome.grid(row=0, column=1, pady=5)

tk.Label(frame_campos, text="Endereço Completo:").grid(row=1, column=0, sticky="e", pady=5)
entry_endereco = tk.Entry(frame_campos, width=40)
entry_endereco.grid(row=1, column=1, pady=5)

tk.Label(frame_campos, text="Altura (cm):").grid(row=2, column=0, sticky="e", pady=5)
entry_altura = tk.Entry(frame_campos, width=40)
entry_altura.grid(row=2, column=1, pady=5)

tk.Label(frame_campos, text="Peso (Kg):").grid(row=3, column=0, sticky="e", pady=5)
entry_peso = tk.Entry(frame_campos, width=40)
entry_peso.grid(row=3, column=1, pady=5)

tk.Label(frame_campos, text="Resultado:").grid(row=4, column=0, sticky="e", pady=10)
tk.Label(frame_campos, textvariable=resultado_var, font=("Arial", 12, "bold")).grid(row=4, column=1, sticky="w", pady=10)

#Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

tk.Button(frame_botoes, text="Calcular e Salvar", command=calcular_imc, width=15, bg="#dddddd").pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Ver Histórico", command=ver_historico, width=15).pack(side=tk.LEFT, padx=5) #Botão Novo
tk.Button(frame_botoes, text="Limpar", command=limpar_dados, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Sair", command=sair, width=10).pack(side=tk.LEFT, padx=5)

janela.mainloop()