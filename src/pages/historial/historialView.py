import flet as ft
from src.pages.historial.components.tablaHistorial import tablaHistorial
from src.pages.historial.components.campos import campos

class historialClinico(ft.Card):
    def __init__(self):
        super().__init__(
            expand=True,
            elevation= 5,
            color=ft.colors.WHITE,
            content= ft.Container(
                expand=True,
                padding= 20,
                content= ft.Row(
                    spacing= 20,
                    controls= [
                        ft.Column(
                            expand= True,
                            spacing= 20,
                            controls= [
                                campos(),
                                ft.Divider(),
                                tablaHistorial()
                                
                            ]
                        )
                    ]
                )
            )
        )
    
    