import flet as ft
from src.components.TextoIcono import TextoIcono
from src.components.TextfieldsIcons import vitalField

class formulario(ft.Container):
    def __init__(self):
        # Inicialización de los campos como self
        self.peso_inicial = vitalField(
            "PESO INICIAL",
            ft.icons.MONITOR_WEIGHT,
            "kg",
            "0.0"
        )
        self.peso_seco = vitalField(
            "PESO SECO",
            ft.icons.SCALE,
            "kg",
            "0.0"
        )
        self.frecuencia_cardiaca = vitalField(
            "FRECUENCIA CARDIACA",
            ft.icons.FAVORITE,
            "lpm",
            "0"
        )
        
        self.temperatura_actual = vitalField(
            "TEMPERATURA ACTUAL",
            ft.icons.THERMOSTAT,
            "°C",
            "0.0"
        )
        self.duracion_sesion = vitalField(
            "DURACIÓN DE LA SESION",
            ft.icons.TIMELAPSE,
            "horas",
            "0.0"
        )
        self.presion_arterial = vitalField(
            "PRESIÓN ARTERIAL",
            ft.icons.SPEED,
            "mmHg",
            "120/80"
        )
        
        # Ahora construyo el layout usando los self.* y paso todo al super constructor
        super().__init__(
            expand=True,
            padding=30,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.ResponsiveRow(
                        spacing=60,
                        controls=[
                            ft.Column(
                                spacing=30,
                                col={"xs": 12, "sm": 6, "md": 6, "lg": 6},
                                controls=[
                                    self.peso_inicial,
                                    self.peso_seco,
                                    self.frecuencia_cardiaca,
                                ]
                            ),
                            ft.Column(
                                spacing=20,
                                col={"xs": 12, "sm": 6, "md": 6, "lg": 6},
                                controls=[
                                    self.temperatura_actual,
                                    self.duracion_sesion,
                                    self.presion_arterial,
                                ]
                            )
                        ]
                    )
                ]
            )
        )
