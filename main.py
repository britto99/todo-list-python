from database import criar_tabelas
from todo_app import menu

def main():
    criar_tabelas()
    print("Bem-vindo ao aplicativo de Lista de Tarefas!")
    menu()

if __name__ == "__main__":
    main()
