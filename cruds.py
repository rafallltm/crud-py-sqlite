import sqlite3

# Conectar ao banco de dados SQLite ou criar um novo se não existir
conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# Criar a tabela de tarefas se ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        concluida INTEGER
    )
''')

# Função para criar uma nova tarefa
def criar_tarefa(descricao):
    cursor.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, 0)", (descricao,))
    conn.commit()

# Função para ler todas as tarefas
def ler_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    return cursor.fetchall()

# Função para atualizar uma tarefa
def atualizar_tarefa(id, concluida):
    cursor.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (concluida, id))
    conn.commit()

# Função para excluir uma tarefa
def excluir_tarefa(id):
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()

# Menu principal
while True:
    print("\nAplicativo de Gerenciamento de Tarefas")
    print("1. Criar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        descricao = input("Digite a descrição da tarefa: ")
        criar_tarefa(descricao)
        print("Tarefa criada com sucesso!")

    elif escolha == "2":
        tarefas = ler_tarefas()
        print("\nLista de Tarefas:")
        for tarefa in tarefas:
            status = "Concluída" if tarefa[2] else "Pendente"
            print(f"{tarefa[0]}. {tarefa[1]} - {status}")

    elif escolha == "3":
        id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
        atualizar_tarefa(id, 1)
        print("Tarefa marcada como concluída!")

    elif escolha == "4":
        id = int(input("Digite o ID da tarefa a ser excluída: "))
        excluir_tarefa(id)
        print("Tarefa excluída com sucesso!")

    elif escolha == "5":
        print("Saindo do aplicativo.")
        break

    else:
        print("Opção inválida. Tente novamente.")
