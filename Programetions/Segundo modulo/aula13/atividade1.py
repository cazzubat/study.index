import flet as ft 
 
def main(page:ft.Page):
    # page.theme = "dark"   
    def handle_click(event):
        page.add(ft.Text("Cliquei no caiox"))
        # page.update()

    ola = ft.Text("Fala que é noix!",size=50,color="red",bgcolor="yellow")
    botao = ft.ElevatedButton(text="Clica no caiox",on_click=handle_click)

    page.add(ola,botao)

ft.app(target=main)
