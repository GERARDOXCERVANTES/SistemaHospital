import flet as ft

class CitasAgendadas(ft.Container):
    def __init__(self):
        self.filas = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER))
                ]
            )
        ]
        
        self.tabla = ft.DataTable(
            column_spacing=20,
            expand=True,
            columns=[
                ft.DataColumn(label=ft.Text('FECHA', text_align=ft.TextAlign.CENTER)),
                ft.DataColumn(label=ft.Text('HORA', text_align=ft.TextAlign.CENTER)),
                ft.DataColumn(label=ft.Text('MEDICO', text_align=ft.TextAlign.CENTER))
            ],
            rows=self.filas
        )
        
        super().__init__(
            padding=0,
            expand=True,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Container(
                        padding=20,
                        expand=True,
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                ft.Row(
                                    spacing=20,
                                    controls=[
                                        ft.Icon(ft.icons.DATE_RANGE_SHARP, size=20),
                                        ft.Text('CITAS', color='#111184', size=16, weight=ft.FontWeight.BOLD)
                                    ]
                                ),
                                ft.Column(
                                    expand=True,
                                    scroll=ft.ScrollMode.AUTO,
                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                    spacing=0,
                                    controls=[self.tabla]
                                )
                            ]
                        )
                    )
                ]
            )
        )
    
    def update_citas(self, cita_data):
        if not cita_data:
            self.filas = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER)),
                        ft.DataCell(ft.Text("--", text_align=ft.TextAlign.CENTER))
                    ]
                )
            ]
        else:
            self.filas.clear()
            
            for cita in cita_data:
                self.filas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(f"{cita[1]}", text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(f"{cita[2]}", text_align=ft.TextAlign.CENTER)),
                            ft.DataCell(ft.Text(f"{cita[3]}", text_align=ft.TextAlign.CENTER))
                        ]
                    )
                )
        
        self.tabla.rows = self.filas
        self.update()