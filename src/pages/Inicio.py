import flet as ft
from src.components.DataRow import DataRow
from src.components.SectionHeader import SectionHeader
from src.components.StatCard import StatCard
from src.components.ActionButton import ActionButton
from src.components.StatusTag import StatusTag
from src.pages.inicio.components.Caledario import iuCitas


class iuInicio(ft.Card):
    def __init__(self):
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
                        self.create_medico_panel(),
                        self.create_citas_panel()
                    ]
                )
            )
        )
    
    def create_medico_panel(self):
        """Crea el panel de datos del médico"""
        return ft.Container(
            expand=True,
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                spacing=10,
                controls=[
                    # Encabezado de Datos del Médico
                    SectionHeader(ft.icons.MEDICAL_SERVICES, "DATOS DEL MÉDICO"),
                    
                    # Contenido principal
                    ft.Row(
                        spacing=20,
                        controls=[
                            # Columna 1: Foto/avatar del médico
                            ft.Container(
                                height=100,
                                width=100,
                                border_radius=50,
                                bgcolor="#E3F2FD",
                                content=ft.Icon(
                                    ft.icons.PERSON_4_OUTLINED,
                                    size=50,
                                    color="#4355B9"
                                ),
                                alignment=ft.alignment.center
                            ),
                            
                            # Columna 2: Datos del médico
                            ft.Container(
                                padding=10,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                    controls=[
                                        DataRow(ft.icons.BADGE_OUTLINED, 'ID: ---'),
                                        DataRow(ft.icons.PERSON_OUTLINE, 'NOMBRE: ---'),
                                        DataRow(ft.icons.MEDICAL_SERVICES_OUTLINED, 'ESPECIALIDAD: ---'),
                                        DataRow(ft.icons.EMAIL_OUTLINED, 'EMAIL: ---')
                                    ]
                                )
                            ),
                            
                            ft.VerticalDivider(color="#DFDFDF", width=1),
                            
                            # Columna 3: Estadísticas
                            ft.Column(
                                controls=[
                                    # Citas hoy
                                    StatCard(ft.icons.CALENDAR_TODAY, "CITAS HOY", "20"),
                                    ft.Divider(height=1, color="#DFDFDF"),
                                    # Pacientes
                                    StatCard(ft.icons.PEOPLE_OUTLINE, "PACIENTES", "3")
                                ]
                            ),
                            
                            # Columna 4: Pestañas con contenido
                            ft.Container(
                                expand=True,
                                height=400,
                                padding=0,
                                content=ft.Tabs(
                                    tab_alignment=ft.TabAlignment.CENTER,
                                    selected_index=0,
                                    animation_duration=300,
                                    tabs=[
                                        ft.Tab(
                                            tab_content=ft.Icon(ft.icons.CALENDAR_MONTH),
                                            content=iuCitas()
                                        ),
                                        ft.Tab(
                                            tab_content=ft.Icon(ft.icons.DASHBOARD_CUSTOMIZE),
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
    
    def create_citas_panel(self):
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
                                            rows=self.generate_cita_rows(20),
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
    
    def generate_cita_rows(self, count):
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
 

