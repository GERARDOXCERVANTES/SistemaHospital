import flet as ft

class iconLogin(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            width=60,
            height=60,
            border_radius=100,                    # Radio de la esquina
            clip_behavior=ft.ClipBehavior.HARD_EDGE,  # Recorta según el radio
            content=ft.Image(
                src="src/assets/logo.jpg",
                fit=ft.ImageFit.COVER              # Aseguras que ocupe todo el contenedor
            ),
             shadow=ft.BoxShadow(
                spread_radius=5,  # Difusión
                blur_radius=15,  # Desenfoque
                color=ft.colors.BLACK26,  # Color de la sombra
                offset=ft.Offset(5, 5),  # Posición de la sombra
            ),
            
            
        )
