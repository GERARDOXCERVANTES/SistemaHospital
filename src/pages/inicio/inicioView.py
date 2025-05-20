import flet as ft
from src.pages.inicio.components.citasPanel import CitasPanel
from src.pages.inicio.components.infoMedic import create_medico

class iuInicio(ft.Card):
    def __init__(self,medico):
        panel_medico = create_medico(medico)
        panel_citas = CitasPanel(medico)
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
                        panel_medico,
                        panel_citas
                    ]
                )
            )
        )
        
