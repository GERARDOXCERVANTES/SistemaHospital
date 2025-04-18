import flet as ft
from src.components.TextoIcono import TextoIcono

class tablaHistorial(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Column(
                        controls=[
                            TextoIcono(
                                'HISTORIAL CLÍNICO',
                                ft.icons.MEDICAL_INFORMATION_ROUNDED,
                                ft.colors.BLUE
                            ),
                            ft.Divider()
                        ]
                    ),
                    ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        spacing=0,
                        controls=[
                            ft.DataTable(
                                column_spacing=20,
                                expand=True,
                                columns=[
                                    ft.DataColumn(
                                        label=ft.Row([
                                            ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.BLUE),
                                            ft.Text('FECHA')
                                        ])
                                    ),
                                    ft.DataColumn(
                                        label=ft.Row([
                                            ft.Icon(ft.icons.PERSON, color=ft.colors.GREEN),
                                            ft.Text('MÉDICO')
                                        ])
                                    ),
                                    ft.DataColumn(
                                        label=ft.Row([
                                            ft.Icon(ft.icons.MONITOR_HEART, color=ft.colors.RED),
                                            ft.Text('SIGNOS VITALES')
                                        ])
                                    ),
                                    
                                    ft.DataColumn(
                                        label=ft.Row([
                                            ft.Icon(ft.icons.VISIBILITY, color=ft.colors.BLUE),
                                            ft.Text('ACCIONES')
                                        ])
                                    ),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(
                                                ft.Container(
                                                    content=ft.Text("2023-10-15", text_align=ft.TextAlign.CENTER),
                                                    padding=10
                                                )
                                            ),
                                            
                                            ft.DataCell(
                                                ft.Container(
                                                    content=ft.Text("DR. GARCÍA", text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                    bgcolor=ft.colors.GREEN_50
                                                )
                                            ),
                                            ft.DataCell(
                                                ft.Container(
                                                    content=ft.Text("120/80 | 37°C", text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                    bgcolor=ft.colors.RED_50
                                                )
                                            ),
                                            ft.DataCell(
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.IconButton(
                                                                icon=ft.icons.DOWNLOAD,
                                                                icon_color=ft.colors.GREEN,
                                                                tooltip="Descargar informe",
                                                                on_click=self.descargar_informe
                                                            ),
                                                            ft.IconButton(
                                                                icon=ft.icons.DELETE,
                                                                icon_color=ft.colors.RED,
                                                                tooltip="eliminar consulta",
                                                                on_click=self.eliminar_consulta
                                                            )
                                                        ]
                                                    ),
                                                    padding=5
                                                )
                                            ),
                                        ]
                                    )
                                    for i in range(20)
                                ],
                            )
                        ]
                    )
                ]
            )
        )

    
    def eliminar_consulta(self, e):
        print("Eliminar consulta")
        # Aquí puedes agregar la lógica para eliminar la consulta
            
    def descargar_informe(self, e):
        # Función para descargar el informe médico
        print("Descargar informe médico")
        # Aquí puedes agregar la lógica para generar y descargar el informe médico

