import flet as ft
from src.pages.inicio.components.citasPanel import create_citas_panel
from src.pages.inicio.components.infoMedic import create_medico_panel

class iuInicio(ft.Card):
    def __init__(self):
        super().__init__(
            color=ft.colors.WHITE,
            elevation=5,
            expand=True,
            content=ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        create_medico_panel(),
                        create_citas_panel()
                    ]
                )
            )
        )