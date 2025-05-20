import flet as ft
from src.components.TextoIcono import TextoIcono
from src.pages.sesiones.components.botons import botonesIU
from src.pages.sesiones.components.FormularioPost import PostSesionIu

class contenido(ft.Container):
    def __init__(self):
        # Definición de controles self para poder manipularlos después
        self.titulo = TextoIcono(
            'MONITOREO DE SESION TIEMPO REAL',
            ft.icons.SHOW_CHART_ROUNDED,
            IconC="#3f51b5"
        )
        self.divider1 = ft.Divider()

        # Progreso sesión: textos y barra
        self.text_progreso = ft.Text("Progreso de la sesión:", size=14)
        self.text_tiempo = ft.Text("0:00:00", size=14, weight=ft.FontWeight.W_600)
        self.progress_bar = ft.ProgressBar(value=0, bgcolor=ft.colors.GREY_300, color="#3f51b5", height=15)
        self.text_0 = ft.Text("0%", size=12, color=ft.colors.GREY_600)
        self.text_estimado = ft.Text("Tiempo estimado: 4:00:00", size=12, color=ft.colors.GREY_600)
        self.text_100 = ft.Text("100%", size=12, color=ft.colors.GREY_600)

        self.divider2 = ft.Divider()
        self.observaciones_label = TextoIcono(
            "OBSERVACIONES",
            ft.icons.NOTE_ALT_OUTLINED,
            IconC="#3f51b5"
        )
        self.divider3 = ft.Divider()
        self.observaciones_textfield = ft.TextField(
            multiline=True,
            min_lines=3,
            max_lines=5,
            hint_text="Ingrese observaciones o complicaciones durante la sesión",
            border_radius=5,
        )
        self.divider4 = ft.Divider()
        self.post_sesion = PostSesionIu()
        self.divider5 = ft.Divider()
        self.botones = botonesIU()

        # Construcción del contenido con los controles self
        super().__init__(
            padding=40,
            expand=True,
            content=ft.Column(
                [
                    self.titulo,
                    self.divider1,
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    self.text_progreso,
                                    self.text_tiempo,
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            self.progress_bar,
                            ft.Row(
                                [
                                    self.text_0,
                                    self.text_estimado,
                                    self.text_100,
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                        ],
                        spacing=10
                    ),
                    self.divider2,
                    self.observaciones_label,
                    self.divider3,
                    self.observaciones_textfield,
                    self.divider4,
                    self.post_sesion,
                    self.divider5,
                    self.botones,
                ]
            )
        )

class MonitoreoIu(ft.Card):
    def __init__(self):
        super().__init__(
            expand=True,
            elevation=5,
            color=ft.colors.WHITE,
            content=contenido()
        )
