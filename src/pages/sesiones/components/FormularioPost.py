import flet as ft
from src.components.TextfieldsIcons import vitalField

class PostSesionIu(ft.Container):
    def __init__(self):
        # Definir los campos como atributos self para manipulación futura
        self.peso_post_sesion = vitalField(
            "PESO POST SESION",
            ft.icons.MONITOR_WEIGHT_ROUNDED,
            'kg',
            '0.0'
        )
        self.presion_arterial_final = vitalField(
            "PRESIÓN ARTERIAL FINAL",
            ft.icons.SPEED,
            "mmHg",
            "120/80"
        )
        self.frecuencia_cardiaca_final = vitalField(
            "FRECUENCIA CARDIACA FINAL",
            ft.icons.FAVORITE,
            "lpm",
            "0"
        )
        self.temperatura_final = vitalField(
            "TEMPERATURA FINAL",
            ft.icons.THERMOSTAT,
            "°C",
            "0.0"
        )
        
        # Construir el contenido usando los self.*
        super().__init__(
            expand=True,
            padding=20,
            content=ft.Row(
                spacing=40,
                controls=[
                    ft.Column(
                        spacing=20,
                        controls=[
                            self.peso_post_sesion,
                            self.presion_arterial_final,
                        ]
                    ),
                    ft.Column(
                        spacing=20,
                        controls=[
                            self.frecuencia_cardiaca_final,
                            self.temperatura_final,
                        ]
                    )
                ]
            )
        )
