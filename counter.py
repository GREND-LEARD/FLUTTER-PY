import flet as ft

def main (page: ft.Page):
    
    page.title = "Mi contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_numero = ft.TextField(value=f"1", text_align=ft.TextAlign.CENTER, width=100)
    
    # si queremos interactuarl con ellos pues como variable
    def menos (e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()
    
    def mas(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()
    
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=menos),
                txt_numero,
                ft.IconButton(ft.icons.ADD, on_click=mas),
                ft.ElevatedButton(text=" Hola yo"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )      
    )
    
    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()

ft.app(main)
# flet run counter.py -d  app de escritorio 
#  flet run counter.py -W pagina web

