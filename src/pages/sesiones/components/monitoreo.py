import flet as ft
from src.components.TextoIcono import TextoIcono
from src.pages.sesiones.components.botons import botonesIU
from src.pages.sesiones.components.FormularioPost import PostSesionIu

class contenido(ft.Container):
    def __init__(self):
        super().__init__(
            padding= 40,
            expand= True,
            content= ft.Column(
                [
                    TextoIcono(
                        'MONITOREO DE SESION TIEMPO REAL',
                        ft.icons.SHOW_CHART_ROUNDED,
                        IconC= "#3f51b5"
                    ),
                    ft.Divider(),
                     # Progreso de la sesión
                    ft.Column(
                        [
                            ft.Row([
                                ft.Text("Progreso de la sesión:", size=14),
                                ft.Text("0:00:00", size=14, weight=ft.FontWeight.W_600)
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.ProgressBar(value=0, bgcolor=ft.colors.GREY_300, color="#3f51b5", height=15),
                             ft.Row([
                                ft.Text("0%", size=12, color=ft.colors.GREY_600),
                                ft.Text("Tiempo estimado: 4:00:00", size=12, color=ft.colors.GREY_600),
                                ft.Text("100%", size=12, color=ft.colors.GREY_600),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ], spacing=10),
                    ft.Divider(),
                     TextoIcono(
                        "OBSERVACIONES",
                        ft.icons.NOTE_ALT_OUTLINED,
                        IconC= "#3f51b5"
                    ),ft.Divider(),
                    ft.TextField(
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        hint_text="Ingrese observaciones o complicaciones durante la sesión",
                        border_radius=5,
                    ),ft.Divider(),
                    PostSesionIu(),
                    ft.Divider(),
                    botonesIU(),
                    
                    
                    
                ]
            )
        )

class MonitoreoIu(ft.Card):
    def __init__(self):
        super().__init__(
            expand= True,
            elevation= 5,
            color= ft.colors.WHITE,
            content= contenido()
        )
        
