import flet as ft
from src.components.TextoIcono import TextoIcono
import datetime as dt

class content(ft.Container):
    def __init__(self):
        # Definición de los controles self para manipulación futura
        self.titulo = TextoIcono(
            "DATOS DE PACIENTE ",
            icono=ft.Icons.PERSON_SEARCH,
            IconC=ft.Colors.BLUE
        )
        self.divider = ft.Divider()

        self.id_paciente = TextoIcono(
            texto="ID:  ",
            icono=ft.icons.BADGE_ROUNDED,
            IconC=ft.colors.BLUE
        )
        self.nombre = TextoIcono(
            texto="NOMBRE: ",
            icono=ft.Icons.PERSON,
            IconC=ft.Colors.BLUE
        )
        self.inicio_sesion = TextoIcono(
            texto="INICIO DE SESION:  ",
            icono=ft.Icons.TIMELAPSE,
            IconC=ft.Colors.BLUE
        )
        self.fecha_sesion = TextoIcono(
            texto="FECHA SESION:  ",
            icono=ft.Icons.CALENDAR_TODAY,
            IconC=ft.Colors.BLUE
        )

        # Construcción del contenido con los controles self
        super().__init__(
            padding=30,
            expand=True,
            content=ft.Column(
                spacing=20,
                controls=[
                    self.titulo,
                    self.divider,
                    ft.Column(
                        spacing=40,
                        controls=[
                            self.id_paciente,
                            self.nombre,
                            self.inicio_sesion,
                            self.fecha_sesion
                        ]
                    )
                ]
            )
        )

class infoPaciente(ft.Card):
    def __init__(self):
        super().__init__(
            expand=True,
            elevation=5,
            color=ft.colors.WHITE,
            content=content()
        )

def horaA():
    ahora = dt.datetime.now()
    return ahora.strftime("%H:%M:%S")
