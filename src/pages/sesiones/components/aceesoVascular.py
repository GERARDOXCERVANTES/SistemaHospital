import flet as ft
from src.components.TextfieldsIcons import vitalField
from src.components.TextoIcono import TextoIcono

class accesoVascularIu(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            padding= 30,
            content= ft.Row(
                
                spacing= 20,
                controls=[
                   ft.Column(
                       spacing= 20,
                       controls=[
                            vitalField(
                                "TIPO DE ACCESO",
                                ft.Icons.TYPE_SPECIMEN,
                                '',
                                "Ej fistula",
                            ),vitalField(
                                "LOCALIZACION",
                                ft.Icons.LOCATION_ON,
                                '',
                                "",
                            ),
                            ft.Dropdown(
                                options=[
                                    ft.dropdown.Option("FUNCIONANDO CORRECTAMENTE"),
                                    ft.dropdown.Option("OCLUSION PARCIAL"),
                                    ft.dropdown.Option("OCLUSION TOTAL"),
                                    ft.dropdown.Option("TROMBOSIS"),
                                    ft.dropdown.Option("INFECCION")
                                ],
                                hint_text="ESTADO",
                                border_radius=8,
                                expand=True
                            )
                       ]
                   ),ft.VerticalDivider(),
                   ft.Column(
                       spacing= 10,
                       controls=[
                           TextoIcono(
                                "OBSERVACIONES",
                                ft.icons.NOTE_ALT_OUTLINED,
                                IconC= "#3f51b5"
                            ),ft.Divider(),
                            ft.TextField(
                                multiline=True,
                                min_lines=3,
                                max_lines=5,
                                hint_text="Ingrese observaciones del acceso",
                                border_radius=5,
                            ),
                       ]
                   )
                   
                ]
            )
        )