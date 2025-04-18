import flet as ft

class TextoIcono(ft.Row):
    def __init__(self, texto, icono, IconC):
        super().__init__(
            spacing=10,  
            controls=[
                ft.Icon(name=icono, size=24, color=IconC), 
                ft.Text(texto, size=16, weight="bold",text_align= ft.TextAlign.CENTER,)
            ]
        )
