import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    
    task_input = ft.TextField(label="Nova Tarefa", expand=True)
    task_list = ft.Column()
    
    def add_task(e):
        if task_input.value.strip():
            task_list.controls.append(ft.Text(task_input.value))
            task_input.value = ""
            page.update()
    
    add_button = ft.ElevatedButton("Adicionar", on_click=add_task)
    
    page.add(ft.Row([task_input, add_button]), task_list)

ft.app(target=main)