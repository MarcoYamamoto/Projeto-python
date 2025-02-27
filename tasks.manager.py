import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        
    def load_tasks(self):
        """Carrega as tarefas do arquivo JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tasks = data.get('tasks', [])
        else:
            print("Arquivo de tarefas não encontrado, criando um novo arquivo.")
        
    def save_tasks(self):
        """Salva as tarefas no arquivo JSON."""
        with open(self.filename, 'w') as file:
            json.dump({"tasks": self.tasks}, file, indent=4)
        
    def add_task(self, title, description, due_date):
        """Adiciona uma nova tarefa."""
        task_id = len(self.tasks) + 1
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "completed": False,
            "due_date": due_date
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Tarefa '{title}' adicionada com sucesso!")
    
    def edit_task(self, task_id, title=None, description=None, due_date=None):
        """Edita uma tarefa existente."""
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if due_date:
                task["due_date"] = due_date
            self.save_tasks()
            print(f"Tarefa '{task_id}' editada com sucesso!")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")
    
    def remove_task(self, task_id):
        """Remove uma tarefa pelo ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Tarefa '{task_id}' removida com sucesso!")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")
    
    def get_task_by_id(self, task_id):
        """Retorna uma tarefa pelo ID."""
        return next((task for task in self.tasks if task["id"] == task_id), None)
    
    def display_tasks(self, show_completed=False):
        """Exibe todas as tarefas ou apenas as pendentes."""
        print("\n=== Tarefas ===")
        filtered_tasks = [task for task in self.tasks if task["completed"] == show_completed]
        
        if not filtered_tasks:
            print("Nenhuma tarefa encontrada.")
        else:
            for task in filtered_tasks:
                status = "Concluída" if task["completed"] else "Pendente"
                print(f"ID: {task['id']} | {task['title']} | Status: {status} | Data: {task['due_date']}")
    
    def mark_task_completed(self, task_id):
        """Marca uma tarefa como concluída."""
        task = self.get_task_by_id(task_id)
        if task:
            task["completed"] = True
            self.save_tasks()
            print(f"Tarefa '{task_id}' marcada como concluída!")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")

def main():
    manager = TaskManager()
    
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1. Adicionar Tarefa")
        print("2. Editar Tarefa")
        print("3. Remover Tarefa")
        print("4. Exibir Tarefas Pendentes")
        print("5. Exibir Tarefas Concluídas")
        print("6. Marcar Tarefa como Concluída")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            title = input("Título da Tarefa: ")
            description = input("Descrição: ")
            due_date = input("Data de Conclusão (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)
        
        elif choice == "2":
            task_id = int(input("ID da tarefa a editar: "))
            title = input("Novo título (deixe vazio para não alterar): ")
            description = input("Nova descrição (deixe vazio para não alterar): ")
            due_date = input("Nova data de conclusão (deixe vazio para não alterar): ")
            manager.edit_task(task_id, title, description, due_date)
        
        elif choice == "3":
            task_id = int(input("ID da tarefa a remover: "))
            manager.remove_task(task_id)
        
        elif choice == "4":
            manager.display_tasks(show_completed=False)
        
        elif choice == "5":
            manager.display_tasks(show_completed=True)
        
        elif choice == "6":
            task_id = int(input("ID da tarefa a marcar como concluída: "))
            manager.mark_task_completed(task_id)
        
        elif choice == "0":
            print("Saindo... Até mais!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
