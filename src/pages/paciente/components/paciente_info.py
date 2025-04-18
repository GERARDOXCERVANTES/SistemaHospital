import flet as ft
from src.components.TextoIcono import TextoIcono
import datetime as dt


class PacienteInfo(ft.Container):
    def __init__(self):
        self.label_id = ft.Text("ID: ---", size=14, weight=ft.FontWeight.W_600)
        self.label_nombre = ft.Text("NOMBRE: ---", size=14, weight=ft.FontWeight.W_600)
        self.label_edad = ft.Text("EDAD: ---", size=14, weight=ft.FontWeight.W_600)
        self.label_sexo = ft.Text("SEXO: ---", size=14, weight=ft.FontWeight.W_600)
        self.label_tipo_sangre = ft.Text("TIPO DE SANGRE: ---", size=14, weight=ft.FontWeight.W_600)

        super().__init__(
            padding=20,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Column(
                        controls=[
                            TextoIcono(
                                'DATOS DEL PACIENTE',
                                ft.icons.PERSON_3_ROUNDED,
                                ft.colors.BLUE
                            ),
                            ft.Divider(),
                        ]
                    ),
                    ft.Row(
                        spacing=20,
                        controls=[
                            ft.Container(
                                height=100,
                                width=100,
                                content=ft.Container(
                                    content=ft.Icon(ft.icons.PERSON_4_OUTLINED, size=50, color=ft.colors.BLUE),
                                    alignment=ft.alignment.center
                                )
                            ),
                            ft.Container(
                                expand=True,
                                height=150,
                                padding=20,
                                content=ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=60,
                                    controls=[
                                        # Ejemplo: Columna con "ID"
                                        ft.Column(
                                            spacing=10,
                                            controls=[
                                                ft.Row(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Icon(ft.icons.BADGE_ROUNDED, size=16),
                                                        self.label_id
                                                    ]
                                                )
                                            ]
                                        ),
                                        # Columna con NOMBRE y EDAD
                                        ft.Column(
                                            spacing=10,
                                            controls=[
                                                ft.Row(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Icon(ft.icons.PERSON_3_SHARP, size=16),
                                                        self.label_nombre
                                                    ]
                                                ),
                                                ft.Row(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Icon(ft.icons.CAKE_OUTLINED, size=16),
                                                        self.label_edad
                                                    ]
                                                ),
                                            ]
                                        ),
                                        # Columna con SEXO y TIPO DE SANGRE
                                        ft.Column(
                                            spacing=10,
                                            controls=[
                                                ft.Row(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Icon(ft.icons.WC_OUTLINED, size=16),
                                                        self.label_sexo
                                                    ]
                                                ),
                                                ft.Row(
                                                    spacing=10,
                                                    controls=[
                                                        ft.Icon(ft.icons.BLOODTYPE_OUTLINED, size=16),
                                                        self.label_tipo_sangre
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            )
                        ]
                    ),
                ]
            )
        )
        
    
    def update_info(self,paciente_data):
       
        if not paciente_data:
            self.label_id.value = "ID: ---"
            self.label_nombre.value = "NOMBRE: ---"
            self.label_edad.value = "EDAD: ---"
            self.label_sexo.value = "SEXO: ---"
            self.label_tipo_sangre.value = "TIPO DE SANGRE: ---"
        else:
            
            self.label_id.value = f"ID: {paciente_data[0]}"
            self.label_nombre.value = f"NOMBRE: {paciente_data[1]}"
            self.label_edad.value = f"EDAD: {paciente_data[3]}"
            self.label_sexo.value = f"SEXO: {paciente_data[2]}"
            self.label_tipo_sangre.value = f"TIPO DE SANGRE: {paciente_data[4]}"

        # Importante: forzar la actualización de este control
        self.update()

    