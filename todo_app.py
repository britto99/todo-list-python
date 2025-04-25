import tkinter as tk
from tkinter import messagebox, ttk
from database import criar_tabelas, adicionar_categoria, adicionar_tarefa, listar_tarefas, excluir_tarefa, editar_tarefa, listar_categorias

def listar_tarefas_gui():
    tarefas = listar_tarefas()
    for widget in frame_tarefas.winfo_children():
        widget.destroy()
    for t in tarefas:
        tarefa_label = tk.Label(frame_tarefas, text=f"ID: {t[0]} | Título: {t[1]} | Status: {t[4]} | Categoria: {t[3]} | Criado em: {t[5]}", bg="#f9f9f9", anchor="w", justify="left")
        tarefa_label.pack(fill="x", padx=10, pady=2)

def atualizar_categorias():
    categorias = listar_categorias()
    ids = [str(cat[0]) for cat in categorias]
    combo_categoria['values'] = ids
    combo_nova_categoria['values'] = ids

def adicionar_categoria_gui():
    nome = entry_categoria.get()
    if nome:
        adicionar_categoria(nome)
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
        entry_categoria.delete(0, tk.END)
        atualizar_categorias()
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome da categoria.")

def adicionar_tarefa_gui():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    categoria_id = combo_categoria.get()
    if titulo and descricao and categoria_id:
        adicionar_tarefa(titulo, descricao, int(categoria_id))
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        entry_titulo.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        listar_tarefas_gui()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

def excluir_tarefa_gui():
    try:
        tarefa_id = int(entry_tarefa_id.get())
        excluir_tarefa(tarefa_id)
        messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
        entry_tarefa_id.delete(0, tk.END)
        listar_tarefas_gui()
    except ValueError:
        messagebox.showerror("Erro", "ID inválido.")

def editar_tarefa_gui():
    try:
        tarefa_id = int(entry_tarefa_id.get())
        novo_titulo = entry_novo_titulo.get()
        nova_descricao = entry_nova_descricao.get()
        nova_categoria_id = combo_nova_categoria.get()
        novo_status = combo_status.get()
        if novo_titulo and nova_descricao and nova_categoria_id and novo_status:
            editar_tarefa(tarefa_id, novo_titulo, nova_descricao, int(nova_categoria_id), novo_status)
            messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
            listar_tarefas_gui()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")
    except ValueError:
        messagebox.showerror("Erro", "ID inválido.")

root = tk.Tk()
root.title("📋 Lista de Tarefas")
root.geometry("800x700")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")

titulo_label = tk.Label(root, text="Aplicativo de Lista de Tarefas", font=("Segoe UI", 18, "bold"), bg="#f0f0f0", fg="#333")
titulo_label.pack(pady=10)

frame_categoria = tk.LabelFrame(root, text="➕ Adicionar Categoria", font=("Segoe UI", 10, "bold"), bg="#ffffff")
frame_categoria.pack(fill="x", padx=15, pady=10)

tk.Label(frame_categoria, text="Nome:", bg="#ffffff").pack(side="left", padx=5)
entry_categoria = tk.Entry(frame_categoria)
entry_categoria.pack(side="left", padx=5)
tk.Button(frame_categoria, text="Adicionar", bg="#4CAF50", fg="white", command=adicionar_categoria_gui).pack(side="left", padx=5)

frame_tarefa = tk.LabelFrame(root, text="📝 Nova Tarefa", font=("Segoe UI", 10, "bold"), bg="#ffffff")
frame_tarefa.pack(fill="x", padx=15, pady=10)

tk.Label(frame_tarefa, text="Título:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=2, sticky="e")
entry_titulo = tk.Entry(frame_tarefa, width=40)
entry_titulo.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_tarefa, text="Descrição:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=2, sticky="e")
entry_descricao = tk.Entry(frame_tarefa, width=40)
entry_descricao.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_tarefa, text="Categoria ID:", bg="#ffffff").grid(row=2, column=0, padx=5, pady=2, sticky="e")
combo_categoria = ttk.Combobox(frame_tarefa)
combo_categoria.grid(row=2, column=1, padx=5, pady=2)

tk.Button(frame_tarefa, text="Adicionar Tarefa", bg="#2196F3", fg="white", command=adicionar_tarefa_gui).grid(row=3, column=0, columnspan=2, pady=10)

frame_excluir = tk.LabelFrame(root, text="🛠️ Gerenciar Tarefa", font=("Segoe UI", 10, "bold"), bg="#ffffff")
frame_excluir.pack(fill="x", padx=15, pady=10)

tk.Label(frame_excluir, text="ID da Tarefa:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=2, sticky="e")
entry_tarefa_id = tk.Entry(frame_excluir)
entry_tarefa_id.grid(row=0, column=1, padx=5, pady=2)
tk.Button(frame_excluir, text="Excluir", bg="#f44336", fg="white", command=excluir_tarefa_gui).grid(row=0, column=2, padx=5, pady=2)

tk.Label(frame_excluir, text="Novo Título:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=2, sticky="e")
entry_novo_titulo = tk.Entry(frame_excluir)
entry_novo_titulo.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_excluir, text="Nova Descrição:", bg="#ffffff").grid(row=2, column=0, padx=5, pady=2, sticky="e")
entry_nova_descricao = tk.Entry(frame_excluir)
entry_nova_descricao.grid(row=2, column=1, padx=5, pady=2)

tk.Label(frame_excluir, text="Nova Categoria:", bg="#ffffff").grid(row=3, column=0, padx=5, pady=2, sticky="e")
combo_nova_categoria = ttk.Combobox(frame_excluir)
combo_nova_categoria.grid(row=3, column=1, padx=5, pady=2)

tk.Label(frame_excluir, text="Novo Status:", bg="#ffffff").grid(row=4, column=0, padx=5, pady=2, sticky="e")
combo_status = ttk.Combobox(frame_excluir, values=["Pendente", "Concluído"])
combo_status.grid(row=4, column=1, padx=5, pady=2)

tk.Button(frame_excluir, text="Editar", bg="#FF9800", fg="white", command=editar_tarefa_gui).grid(row=5, column=0, columnspan=3, pady=10)

frame_tarefas = tk.LabelFrame(root, text="📄 Lista de Tarefas", font=("Segoe UI", 10, "bold"), bg="#ffffff")
frame_tarefas.pack(fill="both", expand=True, padx=15, pady=15)

criar_tabelas()
atualizar_categorias()
listar_tarefas_gui()

root.mainloop()
