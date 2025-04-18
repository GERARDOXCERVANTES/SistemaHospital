import flet as ft
from src.components.TextoIcono import TextoIcono

class SesionesHemodialisis(ft.Container):
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
                                'SESIONES DE HEMODIALIS',
                                ft.icons.HEALTH_AND_SAFETY_OUTLINED,
                                ft.colors.BLUE
                            )
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
                                    ft.DataColumn(label=ft.Text('FECHA', text_align=ft.TextAlign.CENTER)),
                                    ft.DataColumn(label=ft.Text('DURACION', text_align=ft.TextAlign.CENTER)),
                                    ft.DataColumn(label=ft.Text('PESO PRE', text_align=ft.TextAlign.CENTER)),
                                    ft.DataColumn(label=ft.Text('PESO POST', text_align=ft.TextAlign.CENTER)),
                                    ft.DataColumn(label=ft.Text('ULT TOTAL', text_align=ft.TextAlign.CENTER)),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("2025-03-10", text_align=ft.TextAlign.CENTER)),
                                            ft.DataCell(ft.Text("5 MINUTOS", text_align=ft.TextAlign.CENTER)),
                                            ft.DataCell(ft.Text("72.00 KG", text_align=ft.TextAlign.CENTER)),
                                            ft.DataCell(ft.Text("70.00 KG", text_align=ft.TextAlign.CENTER)),
                                            ft.DataCell(ft.Text("2.0 L", text_align=ft.TextAlign.CENTER)),
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

        
