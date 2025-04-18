import flet as ft
from src.components.SectionHeader import SectionHeader
from src.components.ActionButton import ActionButton
from src.components.DataRow import DataRow

from src.components.StatusTag import StatusTag



def create_citas_panel():
        """Crea el panel de citas"""
        return ft.Container(
            expand=True,
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Row(
                spacing=20,
                controls=[
                    # Contenedor para la tabla de citas
                    ft.Container(
                        padding=0,
                        expand=True,
                        content=ft.Column(
                            spacing=15,
                            controls=[
                                # Encabezado
                                SectionHeader(ft.icons.DATE_RANGE_ROUNDED, "CITAS"),
                                
                                # Controles de filtrado/búsqueda
                                ft.Row([
                                    ft.TextField(
                                        hint_text="Buscar paciente...",
                                        prefix_icon=ft.icons.SEARCH,
                                        border_color="#DFDFDF",
                                        height=40,
                                        expand=True
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.FILTER_ALT,
                                        icon_color="#4355B9",
                                        tooltip="Filtrar citas"
                                    )
                                ]),
                                
                                # Tabla de citas
                                ft.Column(
                                    expand=True,
                                    scroll=ft.ScrollMode.AUTO,
                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                    spacing=0,
                                    controls=[
                                        ft.DataTable(
                                            expand=True,
                                            heading_row_height=40,
                                            data_row_max_height=40,
                                            data_row_min_height=40,
                                            border_radius=8,
                                            divider_thickness=0,
                                            horizontal_lines=ft.border.BorderSide(1, "#DFDFDF"),
                                            columns=[
                                                ft.DataColumn(label=ft.Checkbox(
                                                    value=False,
                                                    scale=0.9,
                                                    fill_color="#4355B9"
                                                )),
                                                ft.DataColumn(label=ft.Text("ID CITA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                                                ft.DataColumn(label=ft.Text("PACIENTE", weight=ft.FontWeight.BOLD, size=14, color="#444444")),                                                    
                                                ft.DataColumn(label=ft.Text("FECHA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                                                ft.DataColumn(label=ft.Text("HORA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                                                ft.DataColumn(label=ft.Text("ESTADO", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                                            ],
                                            rows=generate_cita_rows(20),
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    
                    ft.VerticalDivider(color="#DFDFDF"),
                    
                    # Contenedor para los botones
                    ft.Container(
                        width=400,
                        padding=20,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            controls=[
                                # Panel de detalles de cita seleccionada
                                ft.Container(
                                    padding=15,
                                    border_radius=8,
                                    border=ft.border.all(1, "#DFDFDF"),
                                    content=ft.Column(
                                        spacing=10,
                                        controls=[
                                            ft.Text("DETALLES DE CITA", size=16, weight=ft.FontWeight.BOLD, color="#444444"),
                                            ft.Divider(height=1, color="#DFDFDF"),
                                            DataRow(ft.icons.PERSON_OUTLINE, "Paciente: Karla Jiménez", size=13),
                                            DataRow(ft.icons.CALENDAR_TODAY, "Fecha: 2025-03-10", size=13),
                                            DataRow(ft.icons.ACCESS_TIME, "Hora: 10:00", size=13),
                                            DataRow(ft.icons.LOCAL_HOSPITAL, "Consultorio: 304", size=13),
                                            DataRow(ft.icons.COMMENT, "Motivo: Consulta general", size=13),
                                        ]
                                    ),
                                    expand=True
                                ),
                                
                                # Botones de acción
                                ActionButton("ACEPTAR", ft.icons.CHECK_CIRCLE_OUTLINE),
                                ActionButton("CANCELAR", ft.icons.CANCEL_OUTLINED)
                            ]
                        )
                    )
                ]
            )
        )
    
def generate_cita_rows(count):
        """Genera filas de citas para la tabla"""
        rows = []
        for i in range(count):
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Checkbox(
                            value=False,
                            scale=0.9,
                            fill_color="#4355B9"
                        )),
                        ft.DataCell(ft.Text(f"{i+1}", size=13, color="#444444")),
                        ft.DataCell(ft.Text("KARLA JIMENEZ GARCIA", size=13, color="#444444")),
                        ft.DataCell(ft.Text("2025-03-10", size=13, color="#444444")),
                        ft.DataCell(ft.Text("10:00", size=13, color="#444444")),
                        ft.DataCell(StatusTag("PENDIENTE", ft.colors.RED)),
                    ]
                )
            )
        return rows
 

