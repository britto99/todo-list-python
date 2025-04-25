import sqlite3
from datetime import datetime


def criar_tabelas():
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            categoria_id INTEGER,
            status TEXT DEFAULT 'Pendente',
            data_criacao TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')
    conexao.commit()
    conexao.close()

def excluir_tarefa(tarefa_id):
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
    conexao.commit()
    conexao.close()

def adicionar_categoria(nome):
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (nome,))
    conexao.commit()
    conexao.close()

def adicionar_tarefa(titulo, descricao, categoria_id):
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO tarefas (titulo, descricao, categoria_id)
        VALUES (?, ?, ?)
    ''', (titulo, descricao, categoria_id))
    conexao.commit()
    conexao.close()

def listar_tarefas(categoria_id=None, status=None):
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()

    query = '''
        SELECT tarefas.id, tarefas.titulo, tarefas.descricao, categorias.nome, tarefas.status, tarefas.data_criacao
        FROM tarefas
        LEFT JOIN categorias ON tarefas.categoria_id = categorias.id
    '''
    
    params = []
    
    if categoria_id:
        query += ' WHERE tarefas.categoria_id = ?'
        params.append(categoria_id)
    
    if status:
        if categoria_id:
            query += ' AND tarefas.status = ?'
        else:
            query += ' WHERE tarefas.status = ?'
        params.append(status)
    
    query += ' ORDER BY tarefas.data_criacao DESC'

    cursor.execute(query, params)
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def editar_tarefa(tarefa_id, novo_titulo, nova_descricao, nova_categoria_id, novo_status):
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE tarefas
        SET titulo = ?, descricao = ?, categoria_id = ?, status = ?
        WHERE id = ?
    ''', (novo_titulo, nova_descricao, nova_categoria_id, novo_status, tarefa_id))
    conexao.commit()
    conexao.close()

def listar_categorias():
    conexao = sqlite3.connect('banco_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome FROM categorias')
    categorias = cursor.fetchall()
    conexao.close()
    return categorias
