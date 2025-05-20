import flet as ft
from src.components.TextoIcono import TextoIcono

class SesionesHemodialisis(ft.Container):
    def __init__(self):
        
        self.filas = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ]
                    )
        ]
        
        self.tabla_sesiones = ft.DataTable(
            column_spacing=20,
            expand=True,
                columns=[
                    ft.DataColumn(label=ft.Text('FECHA', text_align=ft.TextAlign.CENTER)),
                    ft.DataColumn(label=ft.Text('DURACION', text_align=ft.TextAlign.CENTER)),
                    ft.DataColumn(label=ft.Text('PESO PRE', text_align=ft.TextAlign.CENTER)),
                    ft.DataColumn(label=ft.Text('PESO POST', text_align=ft.TextAlign.CENTER)),
                    ft.DataColumn(label=ft.Text('ULT TOTAL', text_align=ft.TextAlign.CENTER)),
                    ],
                    rows=self.filas
              
                )
        
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
                            self.tabla_sesiones
                        ]
                    )
                ]
            )
        )

        
    def update_sesiones(self, sesiones_data):
        if not sesiones_data:
        
            self.filas = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("----", text_align=ft.TextAlign.CENTER)),
                    ]
                )
            ]
            
        else:
            self.filas.clear()
            for sesiones in sesiones_data:
                self.filas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(sesiones[0], text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(sesiones[1], text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(sesiones[2], text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(sesiones[3], text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(sesiones[4], text_align=ft.TextAlign.CENTER)),
                        ]
                    )
                )
        self.tabla_sesiones.rows = self.filas
        self.update()
    