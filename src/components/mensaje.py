import flet as ft

class mensaje(ft.Container):
    def __init__(self, texto: str):
        super().__init__()
        self.texto = texto
        
    def build(self):
        return ft.SnackBar(
                content=ft.Text(self.texto),
                action="OK",
                action_color=ft.colors.INDIGO_800,
                duration=2000,
            )
    
    def mostrar(self, page):
        snackbar = self.build()
        page.snack_bar = snackbar
        page.snack_bar.open = True
        page.update()

