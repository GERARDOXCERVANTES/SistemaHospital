import flet as ft

class fondo(ft.Image):
    def __init__(self):
        super().__init__(
            
            src="src/assets/fondo.jpg",
            expand=True,
            fit=ft.ImageFit.COVER,
            
        )
