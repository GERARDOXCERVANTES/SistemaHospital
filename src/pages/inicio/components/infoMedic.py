import flet as ft
from src.components.StatCard import StatCard
from src.components.SectionHeader import SectionHeader
from src.components.DataRow import DataRow
from src.pages.inicio.components.Caledario import iuCitas
from src.models.cita import Cita


class create_medico(ft.Container):
    def __init__(self,medico):
        agendar_cita = iuCitas(medico)
        citas_pendientes = Cita.obtener_citas_pendientes(medico[0])
        self.citas_medico = f"{citas_pendientes}"
        self.id_medico = f"ID: {medico[0]}"
        self.nombre_medico = f"NOMBRE: {medico[1]}"
        self.especialidad_medico = f"ESPECIALIDAD: {medico[2]}"
        self.email_medico = f"EMAIL: {medico[3]}"
        
        self.citas = StatCard(ft.icons.CALENDAR_TODAY, "CITAS HOY", self.citas_medico)

        # Create components
        self.foto_medico = ft.Icon(ft.icons.PERSON_4_OUTLINED, size=50, color="#4355B9")
        # Create data rows
        self.id_row = DataRow(ft.icons.BADGE_OUTLINED, self.id_medico)
        self.nombre_row = DataRow(ft.icons.PERSON_OUTLINE, self.nombre_medico)
        self.especialidad_row = DataRow(ft.icons.MEDICAL_SERVICES_OUTLINED, self.especialidad_medico)
        self.email_row = DataRow(ft.icons.EMAIL_OUTLINED, self.email_medico)
        
        super().__init__(
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
                                content= self.foto_medico,
                                alignment=ft.alignment.center
                            ),
                            
                            # Columna 2: Datos del médico
                            ft.Container(
                                padding=10,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                    controls=[
                                        self.id_row,
                                        self.nombre_row,
                                        self.especialidad_row,
                                        self.email_row,
                                    ]
                                )
                            ),
                            
                            ft.VerticalDivider(color="#DFDFDF", width=1),
                            
                            # Columna 3: Estadísticas
                            ft.Column(
                                controls=[
                                    # Citas hoy
                                    self.citas,
                                    ft.Divider(height=1, color="#DFDFDF"),
                                    
                                    
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
                                            content= agendar_cita
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        
    
        
