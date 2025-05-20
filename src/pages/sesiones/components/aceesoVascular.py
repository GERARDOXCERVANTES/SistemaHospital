import flet as ft
from src.components.TextfieldsIcons import vitalField
from src.components.TextoIcono import TextoIcono

class accesoVascularIu(ft.Container):
    def __init__(self):
        # Definir controles como atributos self
        self.tipo_acceso = vitalField(
            "TIPO DE ACCESO",
            ft.Icons.TYPE_SPECIMEN,
            '',
            "Ej fistula",
        )
        self.localizacion = vitalField(
            "LOCALIZACION",
            ft.Icons.LOCATION_ON,
            '',
            "",
        )
        self.estado = ft.Dropdown(
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
        
        self.observaciones_label = TextoIcono(
            "OBSERVACIONES",
            ft.icons.NOTE_ALT_OUTLINED,
            IconC="#3f51b5"
        )
        self.divider = ft.Divider()
        self.observaciones_textfield = ft.TextField(
            multiline=True,
            min_lines=3,
            max_lines=5,
            hint_text="Ingrese observaciones del acceso",
            border_radius=5,
        )
        
        # Ahora sí, el contenido en el super constructor usando self.
        super().__init__(
            expand=True,
            padding=30,
            content=ft.Row(
                spacing=20,
                controls=[
                    ft.Column(
                        spacing=20,
                        controls=[
                            self.tipo_acceso,
                            self.localizacion,
                            self.estado
                        ]
                    ),
                    ft.VerticalDivider(),
                    ft.Column(
                        spacing=10,
                        controls=[
                            self.observaciones_label,
                            self.divider,
                            self.observaciones_textfield,
                        ]
                    )
                ]
            )
        )
