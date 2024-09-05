import tkinter as tk
from tkinter import filedialog
import os
import yaml

def create_project_structure():
    yaml_structure = yaml_text.get("1.0", tk.END).strip()
    directory = directory_entry.get()

    if not yaml_structure or not directory:
        status_label.config(text="Por favor, insira a estrutura YAML e selecione um diretório.")
        return

    try:
        os.chdir(directory)
        structure = yaml.safe_load(yaml_structure)
        create_structure(structure)
        status_label.config(text="Estrutura do projeto criada com sucesso!")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}")

def create_structure(structure, parent_path=''):
    for key, value in structure.items():
        path = os.path.join(parent_path, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(value, path)
        elif value is None:
            open(path, 'a').close()

def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# Criar janela principal
root = tk.Tk()
root.title("Criador de Estrutura de Projeto")

# Área de texto para a estrutura YAML
yaml_label = tk.Label(root, text="Cole a estrutura YAML aqui:")
yaml_label.pack()
yaml_text = tk.Text(root, height=10, width=50)
yaml_text.pack()

# Entrada e botão para selecionar diretório
directory_frame = tk.Frame(root)
directory_frame.pack()
directory_entry = tk.Entry(directory_frame, width=40)
directory_entry.pack(side=tk.LEFT)
directory_button = tk.Button(directory_frame, text="Selecionar Pasta", command=select_directory)
directory_button.pack(side=tk.LEFT)

# Botão para criar a estrutura
create_button = tk.Button(root, text="Criar Estrutura do Projeto", command=create_project_structure)
create_button.pack()

# Label para status
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
