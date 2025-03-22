import flet as ft 
 
def main(page:ft.Page):
    ola = ft.Text('Olá mundo!',size=50)
    page.add(ola)
ft.app(target=main)
