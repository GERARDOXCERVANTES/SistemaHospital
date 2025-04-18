import flet as ft
from src.components.StatCard import StatCard
from src.components.SectionHeader import SectionHeader
from src.components.DataRow import DataRow
from src.pages.inicio.components.Caledario import iuCitas


def create_medico_panel():
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