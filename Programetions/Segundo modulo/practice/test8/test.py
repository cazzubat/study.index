import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    
    name_input = ft.TextField(label="Nome", expand=True)
    email_input = ft.TextField(label="Email", expand=True)
    message_input = ft.TextField(label="Mensagem", multiline=True, expand=True)
    confirmation_text = ft.Text(visible=False)
    
    def submit_form(e):
        if name_input.value and email_input.value and message_input.value:
            confirmation_text.value = "Formulário enviado com sucesso!"
            confirmation_text.visible = True
            name_input.value = ""
            email_input.value = ""
            message_input.value = ""
            page.update()
    
    submit_button = ft.ElevatedButton("Enviar", on_click=submit_form)
    
    page.add(
        ft.Column([
            name_input,
            email_input,
            message_input,
            submit_button,
            confirmation_text
        ])
    )

ft.app(target=main)